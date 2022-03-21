# Visualization

This repository contains the scripts to analyze the results obtained by DASH player [AStream](https://github.com/CSc579s22/AStream).

***Original results analysis scripts provided by SABR can be obtained [here](https://github.com/CSc579s22/SABR/tree/master/results_parse), but the logic in their scripts are not 100% related
to the actual logs we obtained. So we need to rewrite analysis scripts on our own.***

## Example results

### DASH_BUFFER_LOG_[date].csv

```
EpochTime,CurrentPlaybackTime,CurrentBufferSize,CurrentPlaybackState,Action,Bitrate
```

### ASTREAM_[date].json

```json
{
    "playback_type": "basic",
    "segment_info": [
        [
            "BigBuckBunny_2s_init.mp4",  # segment name
            89283,                       # current_bitrate (bps)
            879,                         # segment_size (bytes)
            0.010067224502563477         # segment_download_time (seconds)
        ],
        [
            "BigBuckBunny_2s1.m4s",
            262537.0,
            72386,
            0.2049400806427002
        ],
        ...
        [
            "BigBuckBunny_2s150.m4s",
            4219897.0,
            910253,
            1.760321855545044
        ]
    ],
    "playback_info": {
        "start_time": 1647901688.912854,
        "down_shifts": 35,
        "end_time": null,
        "initial_buffering_duration": 0.04209589958190918,
        "interruptions": {
            "count": 2,
            "events": [
                [
                    1647901700.954816,
                    1647901700.990341
                ],
                [
                    1647901703.031903,
                    1647901703.056623
                ]
            ],
            "total_duration": 0.06024479866027832
        },
        "up_shifts": 39
    },
    "video_metadata": {
        "playback_duration": 298.46,
        "available_bitrates": [
            89283,
            262537,
            791182,
            2484135,
            4219897
        ],
        "mpd_file": "BigBuckBunny_2s_mod1.mpd"
    }
}
```

`up_shifts` and `down_shifts` are corresponding to quality/bitrate switching, related code: https://github.com/CSc579s22/AStream/blob/master/dist/client/dash_client.py#L388-L392
```python
if previous_bitrate < current_bitrate:
    config_dash.JSON_HANDLE['playback_info']['up_shifts'] += 1
elif previous_bitrate > current_bitrate:
    config_dash.JSON_HANDLE['playback_info']['down_shifts'] += 1
```
