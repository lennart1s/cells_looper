import Track

latency = 0.295


def latencyCompensation(track):
    track.toSkip += int(latency * 44100)
    track.toRecord += int(latency * 44100)