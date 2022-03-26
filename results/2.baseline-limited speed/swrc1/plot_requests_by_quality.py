import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import json
from collections import defaultdict

fig, axs = plt.subplots(1, 3)
fig.suptitle("Total requests by quality")


def get_bitrate_percentage(filename):
    print(filename)
    with open(filename) as json_file:
        data = json.load(json_file)
        available_bitrates = data["video_metadata"]["available_bitrates"]

        bitrate = defaultdict()
        bitrate_map = dict.fromkeys(available_bitrates)
        i = 0
        for k in sorted(bitrate_map.keys()):
            bitrate_map[k] = i
            i += 1
        for rate in available_bitrates:
            bitrate[bitrate_map[rate]] = 0
        segment_info = data["segment_info"]
        for info in segment_info:
            bitrate[bitrate_map[info[1]]] += 1

    print(bitrate)
    return bitrate


bitrate_array = [get_bitrate_percentage("ASTREAM_LOGS/ASTREAM_2022-03-25.16_18_14.json"),
                 get_bitrate_percentage("ASTREAM_LOGS/ASTREAM_2022-03-25.16_24_38.json"),
                 get_bitrate_percentage("ASTREAM_LOGS/ASTREAM_2022-03-25.16_35_16.json")]
title = ["basic", "netflix", "sara"]

for i in range(len(bitrate_array)):
    rect1 = axs[i].bar(i, bitrate_array[i][0], color='cyan', label='Q1')
    rect2 = axs[i].bar(i, bitrate_array[i][1], bottom=bitrate_array[i][0], color='green', label='Q2')
    rect3 = axs[i].bar(i, bitrate_array[i][2], bottom=bitrate_array[i][0] + bitrate_array[i][1], color='red', label='Q3')
    rect4 = axs[i].bar(i, bitrate_array[i][3], bottom=bitrate_array[i][0] + bitrate_array[i][1] + bitrate_array[i][2], color='yellow', label='Q4')
    rect5 = axs[i].bar(i, bitrate_array[i][4], bottom=bitrate_array[i][0] + bitrate_array[i][1] + bitrate_array[i][2] + bitrate_array[i][3], color='blue', label='Q5')

    axs[i].bar_label(rect1)
    axs[i].bar_label(rect2)
    axs[i].bar_label(rect3)
    axs[i].bar_label(rect4)
    axs[i].bar_label(rect5)
    axs[i].set_title(title[i])

plt.legend()
fig.tight_layout()
plt.show()
