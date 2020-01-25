import os
import soundfile


### Track-States ###########################################
NONE = -1
STOPPED = 0
RECORDING = 1
OVERDUBBING = 2
PLAYING = 3
MUTED = 4


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



class Metronome(Track):
    beatsPerBar = 0
    bpm = 0
    fs = 0

    data_h = []
    data_l = []

    def generatePattern(self):
        framesPerBeat = int(self.fs / (self.bpm/60))
        click = []
        for i in range(self.beatsPerBar):
            if i == 0:
                click = self.data_l
            else:
                click = self.data_h
            for j in range(framesPerBeat):
                if j < len(click):
                    self.data.append([click[j], click[j]])
                else:
                    self.data.append([0, 0])

    def __init__(self, beatsPerBar, bpm, fs):
        self.beatsPerBar = beatsPerBar
        self.bpm = bpm
        self.fs = fs

        self.data_h, _ = soundfile.read("./res/metronome_h.wav", dtype='float32')
        self.data_l, _ = soundfile.read("./res/metronome_l.wav", dtype='float32')

        self.generatePattern()

    def nextState(self):
        if self.state == NONE:
            self.state = PLAYING
        
        elif self.state == PLAYING:
            self.state = MUTED

        elif self.state == MUTED:
            self.state = PLAYING


tracks = [Track('First'),
        Track('Second'),
        Track('Third')]

metronome = Metronome(4, 120, 44100)