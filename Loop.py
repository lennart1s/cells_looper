import Track
from Track import tracks


def record(track, indata):
    for frame in indata:
        track.data.append(frame)

def play(track, outdata):
    trackData = track.getCurrentFrameData(len(outdata))
    outdata[:len(trackData)] += trackData
    track.toNextFrameset(len(outdata))

def overdubb(track, outdata, indata):
    trackData = track.getCurrentFrameData(len(outdata))
    outdata[:len(trackData)] += trackData

    for x in range(len(indata)):
        if track.pos+x >= len(track.data):
            x -= len(track.data)
        track.data[track.pos+x] += indata[x]

    track.toNextFrameset(len(outdata))


def audioLoop(indata, outdata, frames, time, status):
    outdata[:] = 0

    for track in tracks:

        if track.state == Track.RECORDING:
            record(track, indata.copy())

        elif track.state == Track.OVERDUBBING:
            overdubb(track, outdata, indata.copy())

        elif track.state == Track.PLAYING:
            play(track, outdata)