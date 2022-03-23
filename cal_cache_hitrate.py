import matplotlib.pyplot as plt
import json

filename = "example_results/basic/cache/ASTREAM_2022-03-23.15_20_41.json"
cache_hit = 0
cache_miss = 0
with open(filename) as json_file:
    data = json.load(json_file)
    segment_info = data["segment_info"]
    for info in segment_info:
        if info[4] is True:
            cache_hit += 1
        else:
            cache_miss += 1
    assert (cache_hit+cache_miss == len(segment_info))
    print("cache-hit rate")
    print(cache_hit/(cache_miss+cache_hit))
