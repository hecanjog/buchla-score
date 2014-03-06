from pippi import dsp

freqs = [200, 350, 500, 700, 1000, 1400, 2000, 3500]

bpm = 400.0
beat = dsp.bpm2frames(bpm)

def make_pulse(snd):
    snd_len = dsp.flen(snd)
    blip = dsp.cut(snd, 0, dsp.mstf(10))
    blip = dsp.env(blip, 'sine')
    blip = dsp.pad(blip, 0, snd_len - dsp.flen(blip))

    return blip

def make_vary(length, freq):

    if dsp.rand(0, 100) > 50:
        return make_pulse(dsp.tone(length, freq, amp=dsp.rand()))

    minlen = dsp.mstf(1)

    pulsewidth = int(dsp.rand(minlen, length / 2))
    
    snd = dsp.tone(pulsewidth, freq, amp=dsp.rand(0, 0.2))
    snd = dsp.env(snd, dsp.randchoose(['sine', 'tri', 'hann']))

    snd = dsp.pad(snd, 0, length - pulsewidth)

    return snd


def make_layer(freq):
    out = ''

    for i in range(500):
        out += make_vary(beat * dsp.randint(1, 8), freq)

    return out

out = dsp.mix([ make_layer(freq) for freq in freqs ])

dsp.write(out, 'buchla-pat10ms')

