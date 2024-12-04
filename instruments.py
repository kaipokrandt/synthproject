from abc import ABC, abstractmethod
import random
import audio
import math
from typing import List, Tuple

class Instrument(ABC):
    @abstractmethod
    def note(self, freq:float, sustain:float) -> audio.Clip:
        pass

#testing instrument
#randomized math to make it sound crazy (tv static)

class CrazyNoise(Instrument):
    def __init__(self) -> None:
        self.volume = 1.0
        self.default_sustain = 1 / 8

    def note(self, freq: float, sustain: float) -> audio.Clip:
        if sustain == 0:
            sustain = self.default_sustain
        frames = round(sustain * audio.SECS_PER_BEAT * audio.FRAMES_PER_SECOND)
        clip = audio.Clip(frames)

        # Parameters for chaotic behavior
        mod_freq = freq * 0.1  # Frequency for modulation
        noise_intensity = 0.4  # Noise level
        vol_decay = math.pow(1 / 50, 1 / frames)  # Faster decay
        volume = self.volume

        for i in range(frames):
            # Time in seconds
            t = i / audio.FRAMES_PER_SECOND

            # adds a wobbling effect
            modulated_freq = freq + mod_freq * math.sin(2 * math.pi * mod_freq * t)

            # Add random shifts
            phase_shift = random.uniform(0, 2 * math.pi)

            # Generate noise
            amp = math.sin(2 * math.pi * modulated_freq * t + phase_shift)
            amp += random.uniform(-noise_intensity, noise_intensity)  # Add white noise
            amp *= volume  # Apply volume

            # Apply random decay
            volume *= vol_decay
            if random.random() < 0.01:  # Occasional volume spikes
                volume *= 1.1

            # Set the amplitude for this frame
            clip.set(i, amp)

        return clip
    

# A buzzy horn-like instrument
# This instrument has a buzzy attack, a pure sustain, and a buzzy fade
class HornBuzzy(Instrument):
    def __init__(self) -> None:
        self.volume = 1.
        self.sustain = .8
        self.rect = 0.
        self.default_sustain = 1/8

    def note(self, freq:float, sustain:float) -> audio.Clip:
        if sustain == 0:
            sustain = self.default_sustain
        attack_beats = 1/32
        sustain_beats = sustain - attack_beats
        fade_beats = 3/32
        total_beats = attack_beats + sustain_beats + fade_beats
        frames = round(total_beats * audio.SECS_PER_BEAT * audio.FRAMES_PER_SECOND)
        clip = audio.Clip(frames)
        for i in range(frames):
            amp = math.sin(2 * math.pi * freq * i / audio.FRAMES_PER_SECOND)
            beat = i / (audio.FRAMES_PER_SECOND * audio.SECS_PER_BEAT)
            amp = audio.saturate(amp, audio.envelope(beat, [1., 1., 0., 0., 1.], [attack_beats, .04, sustain_beats - .04, fade_beats]))
            amp = audio.rectify(amp, self.rect)
            amp *= self.volume * audio.envelope(beat, [0., 1., self.sustain, self.sustain, 0], [attack_beats / 2, attack_beats / 2, sustain_beats, fade_beats])
            clip.set(i, amp)
        return clip

# A bell-like instrument with vibratto
class Marimba(Instrument):
    def __init__(self) -> None:
        self.volume = 1.
        self.rect = 0
        self.vibratto_freq = 16.
        self.vibratto_depth = .8
        self.default_sustain = 1/8

    def note(self, freq:float, sustain:float) -> audio.Clip:
        if sustain == 0:
            sustain = self.default_sustain
        frames = round(sustain * audio.SECS_PER_BEAT * audio.FRAMES_PER_SECOND)
        clip = audio.Clip(frames)
        for i in range(frames):            
            beat = i / (audio.FRAMES_PER_SECOND * audio.SECS_PER_BEAT)
            vibratto = self.vibratto_depth * math.sin(2 * math.pi * self.vibratto_freq * beat)
            amp = math.sin(2 * math.pi * freq * i / audio.FRAMES_PER_SECOND + vibratto)
            amp = audio.rectify(amp, self.rect)
            amp *= (self.volume * (1 - i / frames))
            clip.set(i, amp)
        return clip

# A simple sine wave instrument with volume-based vibratto
class Flute(Instrument):
    def __init__(self) -> None:
        self.volume = 1.
        self.rect = 0.3
        self.vibratto_freq = 5.
        self.vibratto_depth = .3
        self.default_sustain = 1

    def note(self, freq:float, sustain:float) -> audio.Clip:
        if sustain == 0:
            sustain = self.default_sustain
        frames = round(sustain * audio.SECS_PER_BEAT * audio.FRAMES_PER_SECOND)
        clip = audio.Clip(frames)
        for i in range(frames):            
            beat = i / (audio.FRAMES_PER_SECOND * audio.SECS_PER_BEAT)
            amp = math.sin(2 * math.pi * freq * i / audio.FRAMES_PER_SECOND)
            amp = audio.rectify(amp, self.rect)
            vibratto = self.vibratto_depth * (0.5 * math.sin(2 * math.pi * self.vibratto_freq * beat) + 0.5) + 1 - self.vibratto_depth
            amp *= vibratto * audio.envelope(i / frames, [0., 1., 1., 0.], [0.3, 0.4, 0.3])
            clip.set(i, amp)
        return clip

# An experiment
class Flout(Instrument):
    def __init__(self) -> None:
        self.volume = 1.
        self.rect = 0.3
        self.vibratto_freq = 4.
        self.vibratto_depth = 0.
        self.vol_vibratto_depth = 0.8
        self.vol_vibratto_freq = 4.
        self.default_sustain = 1

    def note(self, freq:float, sustain:float) -> audio.Clip:
        if sustain == 0:
            sustain = self.default_sustain
        frames = round(sustain * audio.SECS_PER_BEAT * audio.FRAMES_PER_SECOND)
        clip = audio.Clip(frames)
        for i in range(frames):            
            beat = i / (audio.FRAMES_PER_SECOND * audio.SECS_PER_BEAT)
            amp = math.sin(2 * math.pi * freq * i / audio.FRAMES_PER_SECOND)
            freq_vibratto = math.sin(2 * math.pi * self.vibratto_freq * beat)
            audio.saturate(amp, self.vibratto_depth * freq_vibratto)
            #amp = audio.rectify(amp, self.rect)
            amp *= audio.envelope(i / frames, [0., 1., 1., 0.], [0.3, 0.4, 0.3])
            vol_vibratto = self.vol_vibratto_depth * (0.5 * math.sin(2 * math.pi * self.vol_vibratto_freq * beat) + 0.5) + 1 - self.vibratto_depth
            amp *= vol_vibratto
            clip.set(i, amp)
        return clip

# This drum has a decaying volume and a frequency with increasing jitter.
# I think it sounds like a snare drum.
class Xylophone(Instrument):
    def __init__(self) -> None:
        self.volume = 1.
        self.default_sustain = 1/4

    def note(self, freq:float, sustain:float) -> audio.Clip:
        if sustain == 0:
            sustain = self.default_sustain
        frames = round(sustain * audio.SECS_PER_BEAT * audio.FRAMES_PER_SECOND)
        vol_decay = math.pow(1 / 100, 1 / frames)
        clip = audio.Clip(frames)
        volume = self.volume
        for i in range(frames):
            amp = math.sin(2 * math.pi * freq * math.exp(random.gauss(0, 0 * i / frames)) * i / audio.FRAMES_PER_SECOND)
            amp *= volume
            volume *= vol_decay
            clip.set(i, amp)
        return clip

# This drum has a rapidly-decaying frequency.
# I think it sounds like a pad drum.
class DrumDoo(Instrument):
    def __init__(self) -> None:
        self.volume = 1.
        self.default_sustain = 1/8

    def note(self, freq:float, sustain:float) -> audio.Clip:
        if sustain == 0:
            sustain = self.default_sustain
        frames = round(sustain * audio.SECS_PER_BEAT * audio.FRAMES_PER_SECOND)
        vol_decay = math.pow(1 / 100, 1 / frames)
        freq_decay = math.pow(vol_decay, 1 / 8)
        clip = audio.Clip(frames)
        volume = self.volume
        frequency = freq
        for i in range(frames):
            amp = math.sin(2 * math.pi * frequency * i / audio.FRAMES_PER_SECOND)
            amp *= volume
            volume *= vol_decay
            frequency *= freq_decay
            clip.set(i, amp)
        return clip

# This drum has a decaying volume and a frequency with increasing jitter.
# I think it sounds like a snare drum.
class DrumSnare(Instrument):
    def __init__(self) -> None:
        self.volume = 1.
        self.default_sustain = 1/8

    def note(self, freq:float, sustain:float) -> audio.Clip:
        if sustain == 0:
            sustain = self.default_sustain
        frames = round(sustain * audio.SECS_PER_BEAT * audio.FRAMES_PER_SECOND)
        vol_decay = math.pow(1 / 100, 1 / frames)
        clip = audio.Clip(frames)
        volume = self.volume
        for i in range(frames):
            amp = math.sin(2 * math.pi * freq * math.exp(random.gauss(0, 0.5 * i / frames)) * i / audio.FRAMES_PER_SECOND)
            amp *= volume
            volume *= vol_decay
            clip.set(i, amp)
        return clip

class DrumTss(Instrument):
    def __init__(self) -> None:
        self.volume = 1.
        self.default_sustain = 1/4
        self.scatter = .8

    def note(self, freq:float, sustain:float) -> audio.Clip:
        if sustain == 0:
            sustain = self.default_sustain
        frames = round(sustain * audio.SECS_PER_BEAT * audio.FRAMES_PER_SECOND)
        vol_decay = math.pow(1 / 100, 1 / frames)
        clip = audio.Clip(frames)
        volume = self.volume
        for i in range(frames):
            amp = math.sin(2 * math.pi * freq * math.exp(random.gauss(0, self.scatter)) * i / audio.FRAMES_PER_SECOND)
            amp *= volume
            volume *= vol_decay
            clip.set(i, amp)
        return clip

# Composes music from a list of instruments and some notes
def compose(
    instr_vols:List[Tuple['Instrument',float]],
    score:List[List[Tuple[float, float]]],
    beat_interval:float=1/8,
) -> audio.Clip:
    # Compose all the tracks
    tracks = [ audio.Clip(0) for _ in instr_vols ]
    for beat, list_of_notes in enumerate(score):
        for instr, freq_dur in enumerate(list_of_notes):
            if instr > len(instr_vols):
                raise ValueError(f'beat {beat} specifies notes for more than {len(instr_vols)} instruments, but only {len(instr_vols)} instruments were defined')
            frequency, duration = freq_dur
            if frequency > 0:
                instrument = instr_vols[instr][0]
                sound = instrument.note(frequency, duration)
                frame = round(beat * beat_interval * audio.SECS_PER_BEAT * audio.FRAMES_PER_SECOND)
                tracks[instr].add(frame, sound)

    # Mix the tracks
    composition = audio.Clip(0)
    for i in range(len(instr_vols)):
        composition.add(0, tracks[i], instr_vols[i][1])
    return composition


class UniversalInstrument(Instrument):
    def __init__(self) -> None:
        self.volume = 1.
        self.rect = 0.3
        self.vibratto_freq = 4.
        self.vibratto_depth = 0.
        self.vol_vibratto_depth = 0.8
        self.vol_vibratto_freq = 4.
        self.default_sustain = 1

    def note(self, freq:float, sustain:float) -> audio.Clip:
        if sustain == 0:
            sustain = self.default_sustain
        frames = round(sustain * audio.SECS_PER_BEAT * audio.FRAMES_PER_SECOND)
        clip = audio.Clip(frames)
        for i in range(frames):            
            beat = i / (audio.FRAMES_PER_SECOND * audio.SECS_PER_BEAT)
            amp = math.sin(2 * math.pi * freq * i / audio.FRAMES_PER_SECOND)
            freq_vibratto = math.sin(2 * math.pi * self.vibratto_freq * beat)
            audio.saturate(amp, self.vibratto_depth * freq_vibratto)
            #amp = audio.rectify(amp, self.rect)
            amp *= audio.envelope(i / frames, [0., 1., 1., 0.], [0.3, 0.4, 0.3])
            vol_vibratto = self.vol_vibratto_depth * (0.5 * math.sin(2 * math.pi * self.vol_vibratto_freq * beat) + 0.5) + 1 - self.vibratto_depth
            amp *= vol_vibratto
            clip.set(i, amp)
        return clip
