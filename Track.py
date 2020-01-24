import os
import soundfile

NONE = -1
STOPPED = 0
RECORDING = 1
OVERDUBBING = 2
PLAYING = 3

class Track:

    state = NONE

    data = []
    pos = 0
    
    name = ''


    def __init__(self, name):
        self.name = name
        self.data = []
        self.pos = 0

    def getCurrentFrameData(self, frames):
        return self.data[self.pos:self.pos+frames]

    def toNextFrameset(self, frames):
        self.pos += frames
        if self.pos >= len(self.data):
            self.pos -= len(self.data)

    def nextState(self):
        if self.state == NONE:
            self.state = RECORDING
        
        elif self.state == RECORDING:
            self.state = OVERDUBBING

        elif self.state == OVERDUBBING:
            self.state = PLAYING

        elif self.state == PLAYING:
            self.state = OVERDUBBING

        elif self.state == STOPPED:
            self.state = PLAYING

    def saveToFile(self, filename, fs, ch):
        if len(self.data) > 0:
            if os.path.isfile(filename):
                os.remove(filename)
            file = soundfile.SoundFile(filename, mode='x', samplerate=fs, channels=ch)
            file.write(self.data)


tracks = [Track('First'),
        Track('Second'),
        Track('Third')]