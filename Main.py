import sounddevice
import time

import KeyboardControlls as controlls
import Track

from Loop import audioLoop


def saveTracks():
    Track.tracks[0].saveToFile("yeah.wav", 44100, 2)


audioStream = sounddevice.Stream(samplerate=44100, callback=audioLoop)


controlls.addControll('q', audioStream.stop, None)
controlls.addControll('s', saveTracks, None)


controlls.addControll('1', Track.tracks[0].nextState, None)



# MAIN - LOOP #################################################################
audioStream.start()

while audioStream.active:
    controlls.checkForInput()
    
    time.sleep(0.005)
