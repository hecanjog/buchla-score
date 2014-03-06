from pippi import dsp
from noise import pnoise1
import seq

freqs = [200, 350, 500, 700, 1000, 1400, 2000, 3500]

bpm = 100.0
beat = int(dsp.bpm2frames(bpm) * 0.25)

nump = 100

def make_pulse(snd):
    snd_len = dsp.flen(snd)
    blip = dsp.cut(snd, 0, dsp.mstf(20))
    blip = dsp.env(blip, 'sine')
    blip = dsp.pad(blip, 0, snd_len - dsp.flen(blip))

    return blip

def make_vary(index, length, freq):
    def i(index, offset):
        return ((index + offset) % nump) / float(nump) 

    pulsewidth = int(pnoise1(i(index, 100), 2) * (length / 2))
    
    snd = dsp.tone(pulsewidth, freq, amp=pnoise1(i(index, 99), 3) * 0.5)
    snd = dsp.env(snd, 'sine')

    snd = dsp.pad(snd, 0, length - pulsewidth)

    return snd

p = 'XxxXxxxXxXxxXxxxxXx'

beats = seq.toFrames(p, beat) * 100

layers = []

for l in range(2):
    beats = dsp.rotate(beats, dsp.randint(50, 100))
    layers += [ ''.join([ make_pulse(dsp.tone(length, freqs[i % len(freqs)], amp=dsp.rand(0.1, 0.5))) for i, length in enumerate(beats) ]) ]

out = dsp.mix(layers)

dsp.write(out, 'buchla-perlin')

