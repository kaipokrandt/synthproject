import wave
from typing import List, Tuple
import struct
import math

FRAMES_PER_SECOND = 44100
SAMPLE_WIDTH = 2
SOME_CONST = 1. / math.log(2.)
SECS_PER_BEAT = 1.

# Squashes the underside of the wave
# 0 = no rectification
# 1 = total rectification
def rectify(val:float, amount:float) -> float:
    return val * (1. - amount) if val < 0. else val

# Makes the wave more square (and therefore more harsh, electric, and buzzy)
# amount ranges from -1 to 1. 
def saturate(val:float, amount:float) -> float:
    amount = max(-.99, min(0.99, amount))
    a = 1. - SOME_CONST * math.log(1. + amount)
    #return math.copysign(math.pow(math.fabs(val), a))
    return math.copysign(1. - math.pow(1. - math.pow(math.fabs(val), a), 1. / a), val)

# Smooths a transition from 0 to 1
def smooth(x:float) -> float:
    return 0.5 - 0.5 * math.cos(math.pi * x)

# Generates a smooth envelope shape from a list of values and durations.
# values should have one element longer than durations.
# This function uses the smooth function to interpolate values
def envelope(t:float, values:List[float], durations:List[float]) -> float:
    assert len(durations) + 1 == len(values)
    i = 0
    while i < len(durations):
        if t < durations[i]:
            a = smooth(t / durations[i])
            return (1. - a) * values[i] + a * values[i + 1]
        t -= durations[i]
        i += 1
    return values[-1]

# Reads a little-endian signed 16-bit sample from a bytearray
# and returns a floating point value from -1 to 1.
def read_sample(arr:bytearray, pos:int) -> float:
    return int(struct.unpack('<h', arr[2 * pos : 2 * pos + 2])[0]) / 32768

# Encodes a floating point value from -1 to 1 into a little-endian signed 16-bit sample
# and writes it to a bytearray.
def write_sample(f:float, arr:bytearray, pos:int) -> None:
    arr[2 * pos : 2 * pos + 2] = struct.pack('<h', max(-32768, min(32767, round(f * 32768))))

# Represents a snip of audio
class Clip():
    def __init__(self, frames:int) -> None:
        self.bytes = bytearray(SAMPLE_WIDTH * frames)

    def size(self) -> int:
        return len(self.bytes) // SAMPLE_WIDTH

    def set(self, pos:int, val:float) -> None:
        write_sample(val, self.bytes, pos)

    def add(self, pos:int, clip:'Clip', volume:float=1.) -> None:
        while(self.size() < pos + clip.size()):
            self.bytes.append(0)
            self.bytes.append(0)
        for i in range(clip.size()):
            p = pos + i
            a = read_sample(self.bytes, p)
            b = read_sample(clip.bytes, i)
            write_sample(a + volume * b, self.bytes, p)

    def save(self, filename:str) -> None:
        with wave.open(filename, mode="wb") as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(SAMPLE_WIDTH)
            wav_file.setframerate(FRAMES_PER_SECOND)
            wav_file.writeframes(bytes(self.bytes))
