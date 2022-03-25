import matplotlib.pyplot as plt
import json

fig, axs = plt.subplots(3, 1, constrained_layout=True)
fig.suptitle("Bitrate")

filename = "ASTREAM_LOGS/ASTREAM_2022-03-25.16_18_14.json"
bitrate = []
with open(filename) as json_file:
    data = json.load(json_file)
    segment_info = data["segment_info"]
    for info in segment_info:
        bitrate.append(info[1]/1000.0)
axs[0].plot(bitrate)
axs[0].set_ylabel("bitrate/kbps")
axs[0].set_title('basic')

filename = "ASTREAM_LOGS/ASTREAM_2022-03-25.16_24_38.json"
bitrate = []
with open(filename) as json_file:
    data = json.load(json_file)
    segment_info = data["segment_info"]
    for info in segment_info:
        bitrate.append(info[1] / 1000.0)

axs[1].plot(bitrate)
axs[1].set_ylabel("bitrate/kbps")
axs[1].set_title('netflix')

filename = "ASTREAM_LOGS/ASTREAM_2022-03-25.16_35_16.json"
bitrate = []
with open(filename) as json_file:
    data = json.load(json_file)
    segment_info = data["segment_info"]
    for info in segment_info:
        bitrate.append(info[1] / 1000.0)

axs[2].plot(bitrate)
axs[2].set_ylabel("bitrate/kbps")
axs[2].set_title('sara')

plt.show()