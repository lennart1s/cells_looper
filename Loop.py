import Track
import LatencyCompensation

lastSecond = []

### Record a track ###############################################
def record(track, indata):
    for frame in indata:
        if track.toSkip > 0:
            track.toSkip -= 1
            continue
        track.data.append(frame)

### Play back a track ############################################
def play(track, outdata):
    trackData = track.getCurrentFrameData(len(outdata))
    outdata[:len(trackData)] += trackData
    track.toNextFrameset(len(outdata))

### Overdubb a track #############################################
def overdubb(track, outdata, indata):
    trackData = track.getCurrentFrameData(len(outdata))
    outdata[:len(trackData)] += trackData

    for x in range(len(indata)):
        y = x
        x -= int(LatencyCompensation.latency * 44100)
        if track.pos+x >= len(track.data):
            x -= len(track.data)
        elif track.pos+x < 0:
            x += len(track.data)
        track.data[track.pos+x] += indata[y]

    track.toNextFrameset(len(outdata))



### MAIN AUDIO-LOOP ##############################################
def audioLoop(indata, outdata, frames, time, status):
    global lastSecond
    lastSecond.extend(indata)
    if len(lastSecond) > 44100:
        lastSecond = lastSecond[len(lastSecond)-44100:]

    outdata[:] = 0

    if Track.metronome.state == Track.PLAYING:
        play(Track.metronome, outdata)
    elif Track.metronome.state == Track.MUTED:
        Track.metronome.toNextFrameset(len(outdata))

    for track in Track.tracks:

        if track.state == Track.RECORDING:
            record(track, indata.copy())
        elif track.toRecord > 0:
            data = indata.copy()[:track.toRecord]
            record(track, data)
            track.toRecord -= len(data)
            if track.toRecord == 0:
                track.pos = Track.metronome.pos

        elif track.state == Track.OVERDUBBING:
            overdubb(track, outdata, indata.copy())

        elif track.state == Track.PLAYING:
            track.pos = Track.metronome.pos
            play(track, outdata)