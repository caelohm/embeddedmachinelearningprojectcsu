import librosa
import os
import numpy as np
import soundfile as sf

file_paths = []

for dirpath, dnames, fnames in os.walk("./Database/"):
    for f in fnames:
        file_paths.append(dirpath + f)


samples, sample_rate = librosa.load(file_paths[0])

print(sample_rate)

amp_sum = []
for s in range(0, len(samples), sample_rate*30):
    amp_sum.append( np.abs(samples[s:s+(sample_rate*30)]).mean())

print(amp_sum)

# These numbers should be the same (with the first rounded up)
print("Total number of 30 sec. slices: " + str(len(samples)/(30*sample_rate)))
print(len(amp_sum))
print()
# this index is what 30 second snippit will be picked
index = amp_sum.index(np.max(amp_sum))

beg_index = index*sample_rate*30
new_samples = samples[beg_index:beg_index + (sample_rate*30)]

# save to ogg. guess I can't save an opus file with librosa. d:
sf.write('NEW' + file_paths, new_samples, sample_rate, format='opus', subtype='vorbis')