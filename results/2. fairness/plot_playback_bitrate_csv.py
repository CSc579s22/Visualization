import matplotlib.pyplot as plt
import json
import numpy

alg = ["basic"]
fig, axs = plt.subplots(4, 1, constrained_layout=True)
max_time = -1
for j in range(1):
    fig.suptitle("Playback bitrate w.r.t playback time")
    for i in range(4):
        filename = "sw1c{}/DASH_BUFFER_LOG_{}.csv".format(i+1, alg[j])

        bitrate = []
        timestamp = []
        with open(filename) as csv_file:
            lines = csv_file.readlines()
            for line in lines:
                line_arr = line.strip("\n").split(",")
                if len(line_arr) != 6:
                    continue
                t = line_arr[0]
                action = line_arr[4]
                if action == "StillPlaying":
                    b = float(line_arr[5])
                    bitrate.append(b/1000.0)
                    timestamp.append(round(float(t), 3))
        axs[i].plot(timestamp, bitrate)
        axs[i].set_ylabel("bitrate/kbps")
        axs[i].set_title(alg[j])
        if timestamp[-1] > max_time:
            max_time = timestamp[-1]
    for _, subplot in numpy.ndenumerate(axs):
        subplot.set_xlim(0, max_time)
    plt.show()


# plot in the same figure
# alg = ["basic"]
# fig = plt.plot()
# # fig, axs = plt.subplots(4, 1, constrained_layout=True)
# max_time = -1
# for j in range(1):
#     # fig.title("Playback bitrate w.r.t playback time")
#     for i in range(4):
#         filename = "sw1c{}/DASH_BUFFER_LOG_{}.csv".format(i+1, alg[j])
#
#         bitrate = []
#         timestamp = []
#         with open(filename) as csv_file:
#             # data = json.load(csv_file)
#             lines = csv_file.readlines()
#             for line in lines:
#                 # print(line)
#                 line_arr = line.strip("\n").split(",")
#                 if len(line_arr) != 6:
#                     continue
#                 t = line_arr[0]
#                 action = line_arr[4]
#                 if action == "StillPlaying":
#                     b = float(line_arr[5])
#                     bitrate.append(b/1000.0)
#                     timestamp.append(round(float(t), 3))
#             # segment_info = data["segment_info"]
#             # for info in segment_info:
#             #     bitrate.append(info[1]/1000.0)
#         plt.plot(timestamp, bitrate, label="sw1c{}".format(i+1))
#         # axs[i][j].set_xscale()
#         plt.ylabel("bitrate/kbps")
#         plt.title(alg[j])
#         if timestamp[-1] > max_time:
#             max_time = timestamp[-1]
#     # for _, subplot in numpy.ndenumerate(axs):
#     #     subplot.set_xlim(0, max_time)
#     # plt.xticks(range(0, int(max_time)))
#     plt.legend()
#     plt.show()
