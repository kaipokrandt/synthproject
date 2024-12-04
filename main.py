import math
import audio
import instruments
# be careful listening :)
# Import all the notes
from notes import a0,b0b,b0,c0,d0b,d0,e0b,e0,f0b,f0,g0b,g0,a0b
from notes import a1,b1b,b1,c1,d1b,d1,e1b,e1,f1b,f1,g1b,g1,a1b
from notes import a2,b2b,b2,c2,d2b,d2,e2b,e2,f2b,f2,g2b,g2,a2b
from notes import a3,b3b,b3,c3,d3b,d3,e3b,e3,f3b,f3,g3b,g3,a3b
from notes import a4,b4b,b4,c4,d4b,d4,e4b,e4,f4b,f4,g4b,g4,a4b
from notes import a5,b5b,b5,c5,d5b,d5,e5b,e5,f5b,f5,g5b,g5,a5b
from notes import a6,b6b,b6,c6,d6b,d6,e6b,e6,f6b,f6,g6b,g6,a6b
from notes import a7,b7b,b7,c7,d7b,d7,e7b,e7,f7b,f7,g7b,g7,a7b
from notes import a8,b8b,b8,c8,d8b,d8,e8b,e8,f8b,f8,g8b,g8,a8b
from notes import a9,b9b,b9,c9,d9b,d9,e9b,e9,f9b,f9,g9b,g9,a9b
from notes import a10,b10b,b10,c10,d10b,d10,e10b,e10,f10b,f10,g10b,g10,a10b

#import notes issue, __ not defined, replace __ (functions as rest or silence) with
__ = 0

xylo = instruments.Xylophone()
flout = instruments.Flout()
flute = instruments.Flute()
tss = instruments.DrumTss()
snare = instruments.DrumSnare()
doo = instruments.DrumDoo()
horn = instruments.HornBuzzy()
marimba = instruments.Marimba()

#added new randomized instrument
crazynoise = instruments.CrazyNoise()

composition = instruments.compose(
# (instrument, volume), ...
[(flout,0.2), (flute, 0.2), (crazynoise,.5), (flute,0.2), (flout,0.2), (snare,0.8)],
[
# (Note, duration), ...
[( a5, 1), ( b6b, 1),  ( b7, 1),  ( a7, .5),  ( a5b, 1),  ( c2, 1)],
[( b5b, 1), ( b6, 1),  ( c7, 1),  ( a6b, .5),  ( g5, 1),  ( c2, 1)],
[( b5, 1), ( c6, 1),  ( d7b, 1),  ( g6, .5),  ( g5b, 1),  ( c2, 1)],
[( c5, 1), ( d6b, 1),  ( d7, 1),  ( g6b, .5),  ( f5, 1),  ( c2, 1)],
[( d5b, 1),  ( d6, 1), ( e7b, 1),  ( f6, .5),  ( f5b, 1),  ( c2, 1)],
[( d5, 1),  ( e6b, 1), ( e7, 1),  ( f6b, .5),  ( e5, 1),  ( c2, 1)],
[( e5b, 1), ( e6, 1),  ( f7b, 1),  ( e6, .5),  ( e5b, 1),  ( c2, 1)],
[( e5, 1),  ( f6b, 1), ( f7, 1),  ( e6b, .5),  ( d5, 1),  ( c2, 1)],
# Measure 2
[( f5b, 1), ( f6, 1),  ( g7b, 1),  ( d6, .5),  ( d5b, 1),  ( c2, 1)],
[( f5, 1), ( g6b, 1),  ( g7, 1),  ( d6b, .5),  ( c5, 1),  ( c2, 1)],
[( g5b, 1), ( g6, 1),  ( a7b, 1),  ( c6, .5),  ( b5, 1),  ( c2, 1)],
[( g5, 1), ( a6b, 1),  ( a8, 1),  ( b6, .5),  ( b5b, 1),  ( c2, 1)],
[( a5b, 1),  ( a7, 1), ( b8b, 1),  ( b6b, .5),  ( a5, 1),  ( c2, 1)],
[( a5, 1), ( b6b, 1),  ( b7, 1),  ( a7, .5),  ( a5b, 1),  ( c2, 1)],
[( b5b, 1), ( b6, 1),  ( c7, 1),  ( a6b, .5),  ( g5, 1),  ( c2, 1)],
[( b5, 1), ( c6, 1),  ( d7b, 1),  ( g6, .5),  ( g5b, 1),  ( c2, 1)],
# Measure 3
[( c5, 1), ( d6b, 1),  ( d7, 1),  ( g6b, .5),  ( f5, 1),  ( c2, 1)],
[( d5b, 1),  ( d6, 1), ( e7b, 1),  ( f6, .5),  ( f5b, 1),  ( c2, 1)],
[( d5, 1),  ( e6b, 1), ( e7, 1),  ( f6b, .5),  ( e5, 1),  ( c2, 1)],
[( e5b, 1), ( e6, 1),  ( f7b, 1),  ( e6, .5),  ( e5b, 1),  ( c2, 1)],
[( e5, 1),  ( f6b, 1), ( f7, 1),  ( e6b, .5),  ( d5, 1),  ( c2, 1)],
[( f5b, 1), ( f6, 1),  ( g7b, 1),  ( d6, .5),  ( d5b, 1),  ( c2, 1)],
[( f5, 1), ( g6b, 1),  ( g7, 1),  ( d6b, .5),  ( c5, 1),  ( c2, 1)],
[( g5b, 1), ( g6, 1),  ( a7b, 1),  ( c6, .5),  ( b5, 1),  ( c2, 1)],
# Measure 4
[( g5, 1), ( a6b, 1),  ( a8, 1),  ( b6, .5),  ( b5b, 1),  ( c2, 1)],
[( a5b, 1),  ( a7, 1), ( b8b, 1),  ( b6b, .5),  ( a5, 1),  ( c2, 1)],
[( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __),  ( __, __)],
[( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __),  ( __, __)],
[( __, __),  ( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __)],
[( __, __),  ( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __)],
[( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __),  ( __, __)],
[( __, __),  ( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __)],
# Measure 3
[( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __),  ( __, __)],
[( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __),  ( __, __)],
[( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __),  ( __, __)],
[( __, __), ( c5, 1),  ( __, __),  ( __, __),  ( __, __),  ( f5, 1)],
[( __, __),  ( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __)],
[( __, __),  ( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __)],
[( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __),  ( __, __)],
[( __, __),  ( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __)],
# Measure 4
[( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __),  ( __, __)],
[( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __),  ( __, __)],
[( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __),  ( __, __)],
[( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __),  ( __, __)],
[( __, __),  ( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __)],
[( __, __),  ( d10, 1), ( __, __),  ( __, __),  ( __, __),  ( e10, 1)],
[( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __),  ( __, __)],
[( __, __),  ( __, __), ( __, __),  ( __, __),  ( __, __),  ( __, __)],
])

composition.save('audio.wav')
