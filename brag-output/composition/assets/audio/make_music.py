import numpy as np
import soundfile as sf
import sys

SR = 48000
DUR = 25.8
BPM = 90
BEAT = 60 / BPM
N = int(SR * DUR)
t = np.arange(N) / SR
out = sys.argv[1]


def midi(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def tri(freq, tt):
    ph = (freq * tt) % 1.0
    return 4 * np.abs(ph - 0.5) - 1


# C major, calm: Fmaj7 - C/E - Am7 - G, 4 s per chord
chords = [[53, 57, 60, 64], [52, 55, 60, 67], [57, 60, 64, 67], [55, 59, 62, 67]]
roots = [41, 40, 45, 43]
CH = 4.0

pad = np.zeros(N)
arp = np.zeros(N)
sub = np.zeros(N)
ci = 0
while ci * CH < DUR:
    start = ci * CH
    s0, s1 = int(start * SR), min(int((start + CH + 1.0) * SR), N)
    tt = t[s0:s1] - start
    ln = s1 - s0
    env = np.minimum(1, tt / 1.2) * np.clip((CH + 1.0 - tt) / 1.2, 0, 1)
    chord = chords[ci % 4]
    seg = np.zeros(ln)
    for note in chord:
        for det in (-0.12, 0.0, 0.12):
            f = midi(note) * (1 + det / 100)
            seg += np.sin(2 * np.pi * f * tt) * 0.7 + tri(f * 2, tt) * 0.12
    pad[s0:s1] += seg * env / 12

    r = roots[ci % 4]
    sub[s0:s1] += np.sin(2 * np.pi * midi(r - 12) * tt) * env * 0.35

    pattern = [0, 2, 1, 3, 2, 1]
    step = BEAT / 2
    k = 0
    while k * step < CH and s0 + int(k * step * SR) < N:
        a0 = s0 + int(k * step * SR)
        a1 = min(a0 + int(1.2 * SR), N)
        ta = np.arange(a1 - a0) / SR
        note = chord[pattern[k % len(pattern)]] + 12
        f = midi(note)
        pluck = (np.sin(2 * np.pi * f * ta) + 0.3 * np.sin(2 * np.pi * 2 * f * ta)) * np.exp(-ta * 4.5)
        arp[a0:a1] += pluck * (0.16 if k % 2 == 0 else 0.1)
        k += 1
    ci += 1

master = np.ones(N)
fi = int(1.0 * SR)
master[:fi] = np.linspace(0, 1, fi) ** 1.5
fo0 = int(23.6 * SR)
master[fo0:] = np.linspace(1, 0, N - fo0) ** 1.5

stems = np.stack([pad * master, arp * master, sub * master], axis=1)
sf.write(out, stems.astype(np.float32), SR, subtype="FLOAT")
