import matplotlib.pyplot as plt
import json

fig, axs = plt.subplots(4, 3, constrained_layout=True)
fig.suptitle("Playback bitrate w.r.t playback time")
alg = ["basic", "netflix", "sara"]
for i in range(4):
    for j in range(3):
        filename = "swrc{}/ASTREAM_LOGS/ASTREAM_{}.json".format(i+1, alg[j])

        bitrate = []
        with open(filename) as json_file:
            data = json.load(json_file)
            segment_info = data["segment_info"]
            for info in segment_info:
                bitrate.append(info[1]/1000.0)
        axs[i][j].plot(bitrate)
        axs[i][j].set_ylabel("bitrate/kbps")
        axs[i][j].set_title(alg[j])

plt.show()
