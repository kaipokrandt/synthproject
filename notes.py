from abc import ABC, abstractmethod
import random
import audio
import math
from typing import List, Tuple

# Define the frequencies of notes to use for composition
sharp = math.pow(2, 1/12)


#some things about this scale are rather offputting according to musicians
a0 = 13.75
b0b = a0 * sharp
b0 = b0b * sharp
c0 = b0 * sharp
d0b = c0 * sharp
d0 = d0b * sharp
e0b = d0 * sharp
e0 = d0b * sharp # This is about where human audibility begins
f0b = d0 * sharp
f0 = f0b * sharp
g0b = f0 * sharp
g0 = g0b * sharp
a0b = g0 / sharp

a1 = a0 * 2 # 27.5 Hz
b1b = a1 * sharp
b1 = b1b * sharp
c1 = b1 * sharp
d1b = c1 * sharp
d1 = d1b * sharp
e1b = d1 * sharp
e1 = d1b * sharp
f1b = d1 * sharp
f1 = f1b * sharp
g1b = f1 * sharp
g1 = g1b * sharp
a1b = g1 / sharp

a2 = a1 * 2 # 55 Hz
b2b = a2 * sharp
b2 = b2b * sharp
c2 = b2 * sharp
d2b = c2 * sharp
d2 = d2b * sharp
e2b = d2 * sharp
e2 = d2b * sharp
f2b = d2 * sharp
f2 = f2b * sharp
g2b = f2 * sharp
g2 = g2b * sharp
a2b = g2 / sharp

a3 = a2 * 2 # 110 Hz
b3b = a3 * sharp
b3 = b3b * sharp
c3 = b3 * sharp
d3b = c3 * sharp
d3 = d3b * sharp
e3b = d3 * sharp
e3 = d3b * sharp
f3b = d3 * sharp
f3 = f3b * sharp
g3b = f3 * sharp
g3 = g3b * sharp
a3b = g3 / sharp

a4 = a3 * 2 # 220 Hz
b4b = a4 * sharp
b4 = b4b * sharp
c4 = b4 * sharp
d4b = c4 * sharp
d4 = d4b * sharp
e4b = d4 * sharp
e4 = d4b * sharp
f4b = d4 * sharp
f4 = f4b * sharp
g4b = f4 * sharp
g4 = g4b * sharp
a4b = g4 / sharp

a5 = a4 * 2 # 440 Hz
b5b = a5 * sharp #BFLAT
b5 = b5b * sharp #B
c5 = b5 * sharp #
d5b = c5 * sharp # 
d5 = d5b * sharp #
e5b = d5 * sharp #
e5 = d5b * sharp #
f5b = d5 * sharp # 
f5 = f5b * sharp #
g5b = f5 * sharp #
g5 = g5b * sharp #
a5b = g5 / sharp #f

a6 = a5 * 2 # 880 Hz
b6b = a6 * sharp
b6 = b6b * sharp
c6 = b6 * sharp
d6b = c6 * sharp
d6 = d6b * sharp
e6b = d6 * sharp
e6 = d6b * sharp
f6b = d6 * sharp
f6 = f6b * sharp
g6b = f6 * sharp
g6 = g6b * sharp
a6b = g6 / sharp

a7 = a6 * 2 # 1760 Hz
b7b = a7 * sharp
b7 = b7b * sharp
c7 = b7 * sharp
d7b = c7 * sharp
d7 = d7b * sharp
e7b = d7 * sharp
e7 = d7b * sharp
f7b = d7 * sharp
f7 = f7b * sharp
g7b = f7 * sharp
g7 = g7b * sharp
a7b = g7 / sharp

a8 = a7 * 2 # 3520 Hz
b8b = a8 * sharp
b8 = b8b * sharp
c8 = b8 * sharp
d8b = c8 * sharp
d8 = d8b * sharp
e8b = d8 * sharp
e8 = d8b * sharp
f8b = d8 * sharp
f8 = f8b * sharp
g8b = f8 * sharp
g8 = g8b * sharp
a8b = g8 / sharp

a9 = a8 * 2 # 7040 Hz
b9b = a9 * sharp
b9 = b9b * sharp
c9 = b9 * sharp
d9b = c9 * sharp
d9 = d9b * sharp
e9b = d9 * sharp
e9 = d9b * sharp
f9b = d9 * sharp
f9 = f9b * sharp
g9b = f9 * sharp
g9 = g9b * sharp
a9b = g9 / sharp

a10 = a9 * 2 # 14080
b10b = a10 * sharp
b10 = b10b * sharp
c10 = b10 * sharp
d10b = c10 * sharp
d10 = d10b * sharp
e10b = d10 * sharp
e10 = d10b * sharp
f10b = d10 * sharp # This is about where human audibility ends
f10 = f10b * sharp
g10b = f10 * sharp
g10 = g10b * sharp
a10b = g10 / sharp
