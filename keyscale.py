#!/usr/local/bin/python3
import random

KEY = ['C','C#/Db','D','D#/Eb','E','F','F#/Gb','G','G#/Ab','A','A#/Bb','B']

rKey = random.choice(KEY)
print(rKey)

SCALE = {
    'Major' : 'W W h W W W h',
    'Natural Minor' : 'W h W W h W W',
    'Harmonic Minor' : 'W h W W h W+h h',
    'Melodic Minor' : 'W h W W W W h'
    }

rScale = random.choice(list(SCALE.keys()))
print(rScale)
print(SCALE[rScale])
