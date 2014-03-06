from pippi import dsp

p = 'XxxxXxxxXxxxxXx'

beat = dsp.bpm2frames(100)

length = len(p) * beat

notelength = 0
notes = []
lastnote = 'x'

for i, b in enumerate(p):
    if b == 'X' and lastnote == 'x' and notelength > 0:
        notes += [ notelength ]
        notelength = beat
    else:
        notelength += beat

    if i == len(p) - 1:
        notes += [ notelength ]

    lastnote = b

print notes

