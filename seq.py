from pippi import dsp

p = 'XxxxXxxxXxxxxXx'

beat = dsp.bpm2frames(100)
beat = 1

length = len(p) * beat

notelength = 0
notes = []
lastnote = 'x'

for i, b in enumerate(p):
    if (i == len(p) - 1 or b == 'X') and lastnote == 'x' and notelength > 0:
        notes += [ notelength ]
        notelength = beat
    else:
        notelength += beat

    lastnote = b

print notes

