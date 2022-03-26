import json
from collections import defaultdict

import matplotlib.pyplot as plt


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


fig, axs = plt.subplots(4, 3)
fig.suptitle("Total requests by quality")
title = ["basic", "netflix", "sara"]

for j in range(4):
    bitrate_array = [get_bitrate_percentage("swrc{}/ASTREAM_LOGS/ASTREAM_basic.json".format(j+1)),
                     get_bitrate_percentage("swrc{}/ASTREAM_LOGS/ASTREAM_netflix.json".format(j+1)),
                     get_bitrate_percentage("swrc{}/ASTREAM_LOGS/ASTREAM_sara.json".format(j+1))]

    for i in range(len(bitrate_array)):
        rect1 = axs[j][i].bar(i, bitrate_array[i][0], color='cyan', label='Q1')
        rect2 = axs[j][i].bar(i, bitrate_array[i][1], bottom=bitrate_array[i][0], color='green', label='Q2')
        rect3 = axs[j][i].bar(i, bitrate_array[i][2], bottom=bitrate_array[i][0] + bitrate_array[i][1], color='red',
                              label='Q3')
        rect4 = axs[j][i].bar(i, bitrate_array[i][3],
                              bottom=bitrate_array[i][0] + bitrate_array[i][1] + bitrate_array[i][2], color='yellow',
                              label='Q4')
        rect5 = axs[j][i].bar(i, bitrate_array[i][4],
                              bottom=bitrate_array[i][0] + bitrate_array[i][1] + bitrate_array[i][2] + bitrate_array[i][
                                  3],
                              color='blue', label='Q5')

        axs[j][i].bar_label(rect1)
        axs[j][i].bar_label(rect2)
        axs[j][i].bar_label(rect3)
        axs[j][i].bar_label(rect4)
        axs[j][i].bar_label(rect5)
        axs[j][i].set_title(title[i])

plt.legend()
fig.tight_layout()
plt.show()
