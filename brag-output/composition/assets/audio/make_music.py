import numpy as np
import soundfile as sf
import sys

SR = 48000
DUR = 24.0
BPM = 120
BEAT = 60 / BPM
N = int(SR * DUR)
t = np.arange(N) / SR
rng = np.random.default_rng(7)
out = sys.argv[1]


def midi(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def saw(freq, tt):
    ph = (freq * tt) % 1.0
    return 2 * ph - 1


def env_adsr(n, a, d, s, r):
    e = np.ones(n) * s
    na, nd, nr = int(a * SR), int(d * SR), int(r * SR)
    na = min(na, n)
    e[:na] = np.linspace(0, 1, na)
    e[na:na + nd] = np.linspace(1, s, len(e[na:na + nd]))
    if nr > 0:
        e[-nr:] *= np.linspace(1, 0, nr)
    return e


# A minor: Am - F - C - G, 4 s per chord
chords = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]
roots = [45, 41, 48, 43]

pad = np.zeros(N)
bass = np.zeros(N)
for ci in range(6):
    start = ci * 4.0
    if start >= DUR:
        break
    s0, s1 = int(start * SR), min(int((start + 4.0) * SR), N)
    tt = t[s0:s1] - start
    chord = chords[ci % 4]
    seg = np.zeros(s1 - s0)
    for note in chord:
        for det in (-0.08, 0.08):
            seg += saw(midi(note + 12) * (1 + det / 100), tt)
    pad[s0:s1] += seg * env_adsr(s1 - s0, 0.6, 0.5, 0.8, 0.5) / 6
    # 8th-note pulsing bass
    r = roots[ci % 4]
    for k in range(8):
        b0 = s0 + int(k * BEAT / 2 * SR)
        b1 = min(b0 + int(BEAT / 2 * SR), s1)
        if b0 >= s1:
            break
        tb = np.arange(b1 - b0) / SR
        note = saw(midi(r), tb) * 0.6 + np.sin(2 * np.pi * midi(r - 12) * tb) * 0.6
        bass[b0:b1] += note * np.exp(-tb * 6.0)

drums = np.zeros(N)
kick_len = int(0.35 * SR)
tk = np.arange(kick_len) / SR
kick = np.sin(2 * np.pi * (48 * tk + 90 * (1 - np.exp(-tk * 30)) / 30)) * np.exp(-tk * 9)
hat_len = int(0.05 * SR)
th = np.arange(hat_len) / SR
beat_t = 0.0
i = 0
while beat_t < 22.6:
    s = int(beat_t * SR)
    if beat_t >= 0.15:
        drums[s:s + kick_len] += kick[: max(0, min(kick_len, N - s))] * 0.9
    for sub in (0.25, 0.5, 0.75):
        hs = int((beat_t + sub * BEAT) * SR)
        if hs + hat_len < N:
            amp = 0.22 if sub == 0.5 else 0.1
            drums[hs:hs + hat_len] += rng.standard_normal(hat_len) * np.exp(-th * 90) * amp
    beat_t += BEAT
    i += 1

# riser into the outro (18.6 -> 19.6), then a sub drop at 19.6
riser = np.zeros(N)
r0, r1 = int(18.4 * SR), int(19.6 * SR)
tr = np.arange(r1 - r0) / (r1 - r0)
riser[r0:r1] = rng.standard_normal(r1 - r0) * tr ** 2 * 0.35
d0 = int(19.6 * SR)
td = np.arange(N - d0) / SR
riser[d0:] += np.sin(2 * np.pi * 42 * td) * np.exp(-td * 1.6) * 0.8

# gentle sidechain pump on pad and bass from the kick grid
pump = np.ones(N)
bt = 0.15
while bt < 22.6:
    s = int(bt * SR)
    ln = min(int(0.3 * SR), N - s)
    pump[s:s + ln] = 0.55 + 0.45 * (np.arange(ln) / ln) ** 0.6
    bt += BEAT

master_env = np.ones(N)
fi = int(0.2 * SR)
master_env[:fi] = np.linspace(0, 1, fi)
fo0 = int(22.2 * SR)
master_env[fo0:] = np.linspace(1, 0, N - fo0)

stems = np.stack([
    pad * pump * master_env,
    bass * pump * master_env,
    drums * master_env,
    riser * master_env,
], axis=1)
sf.write(out, stems.astype(np.float32), SR, subtype="FLOAT")
