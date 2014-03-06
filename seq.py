from pippi import dsp

def toFrames(seq, beat):
    notelength = 0
    notes = []
    lastnote = 'x'

    for i, b in enumerate(seq):
        if b == 'X' and lastnote == 'x' and notelength > 0:
            notes += [ notelength ]
            notelength = beat
        else:
            notelength += beat

        if i == len(seq) - 1:
            notes += [ notelength ]

        lastnote = b

    return notes

