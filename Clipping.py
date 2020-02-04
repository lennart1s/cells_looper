import Track
import Loop

threshhold = 0.35

def startClipping(track, referenceTracks):
    for referenceTrack in referenceTracks:
        if referenceTrack.state != Track.NONE and referenceTrack != track:
            # EARLY
            if referenceTrack.pos >= len(referenceTrack.data) - threshhold*44100:
                track.toSkip += len(referenceTrack.data) - referenceTrack.pos
                break
            # LATE
            elif referenceTrack.pos <= threshhold*44100:
                track.toSkip -= referenceTrack.pos
                if track.toSkip < 0:
                    for i in range(track.toSkip, 0):
                        track.data.append(Loop.lastSecond[len(Loop.lastSecond)+i])
                break

def endClipping(track, referenceTracks):
    for referenceTrack in referenceTracks:
        if referenceTrack.state != Track.NONE and referenceTrack != track:
            # EARLY
            if referenceTrack.pos >= len(referenceTrack.data) - threshhold*44100:
                track.toRecord += len(referenceTrack.data) - referenceTrack.pos
                break
            # LATE
            elif referenceTrack.pos <= threshhold*44100:
                track.toRecord -= referenceTrack.pos
                if track.toRecord < 0:
                    track.data = track.data[:len(track.data)+track.toRecord]
                track.pos = referenceTrack.pos
                break