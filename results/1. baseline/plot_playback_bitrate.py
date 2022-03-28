import matplotlib.pyplot as plt
import json

alg = ["basic", "netflix", "sara"]
for j in range(3):
    fig, axs = plt.subplots(4, 1, constrained_layout=True)
    fig.suptitle("Playback bitrate w.r.t playback time")
    for i in range(4):
        filename = "sw1c{}/ASTREAM_LOGS/ASTREAM_{}.json".format(i+1, alg[j])

        bitrate = []
        with open(filename) as json_file:
            data = json.load(json_file)
            segment_info = data["segment_info"]
            for info in segment_info:
                bitrate.append(info[1]/1000.0)
        axs[i].plot(bitrate)
        axs[i].set_ylabel("bitrate/kbps")
        axs[i].set_title(alg[j])
    plt.show()
