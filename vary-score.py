from pippi import dsp

freqs = [200, 350, 500, 700, 1000, 1400, 2000, 3500]

length = dsp.stf(300)

def make_pulse(snd):
    snd_len = dsp.flen(snd)
    blip = dsp.cut(snd, 0, dsp.mstf(1))
    blip = dsp.env(blip, 'sine')
    blip = dsp.pad(blip, 0, snd_len - dsp.flen(blip))

    return blip

def make_vary(snd):
    numpoints = dsp.flen(snd) / 40
    curve = dsp.breakpoint([0] + [ dsp.rand(0, 1) for i in range(dsp.randint(5, numpoints / 100)) ] + [0], numpoints)
    
    snd = dsp.split(snd, 40)

    snd = [ dsp.amp(snd[i], curve[i]) for i in range(numpoints) ]

    snd = ''.join(snd)

    return snd


def make_layer(freq):
    out = dsp.tone(length, freq, amp=0.2)

    out = dsp.vsplit(out, dsp.mstf(10), dsp.mstf(2500))

    for i, o in enumerate(out):
        if dsp.randint(0, 100) > 50:
            out[i] = make_pulse(o)
        else:
            out[i] = make_vary(o)

    out = [ dsp.amp(o, dsp.rand(0, 1)) for o in out ]

    out = ''.join(out)

    return out

out = dsp.mix([ make_layer(freq) for freq in freqs ])

dsp.write(out, 'buchla-vary')
