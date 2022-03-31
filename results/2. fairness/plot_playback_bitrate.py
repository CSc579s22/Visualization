import matplotlib.pyplot as plt
import json

alg = ["basic"]
fig, axs = plt.subplots(4, 3, constrained_layout=True)
for j in range(len(alg)):
    fig.suptitle("Playback bitrate w.r.t playback time")
    for i in range(4):
        filename = "sw1c{}/ASTREAM_{}.json".format(i+1, alg[j])

        bitrate = []
        with open(filename) as json_file:
            data = json.load(json_file)
            segment_info = data["segment_info"]
            for info in segment_info:
                bitrate.append(int(info[1])/1000.0)
        axs[i][j].plot(bitrate)
        axs[i][j].set_ylabel("bitrate/kbps")
        axs[i][j].set_title(alg[j])
plt.show()
