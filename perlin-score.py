from pippi import dsp
from noise import pnoise1

freqs = [200, 350, 500, 700, 1000, 1400, 2000, 3500]

bpm = 50.0
beat = dsp.bpm2frames(bpm)

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


def make_layer(freq):
    out = ''

    for i in range(nump):
        out += make_vary(i, beat, freq)

    return out

out = dsp.mix([ make_layer(freq) for freq in freqs ])

dsp.write(out, 'buchla-perlin')

