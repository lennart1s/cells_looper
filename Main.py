import sounddevice
import time

import KeyboardControlls as controlls
import Track

from Loop import audioLoop


def saveTracks():
    Track.tracks[1].saveToFile("yeah.wav", 44100, 2)
    Track.tracks[0].saveToFile("met.wav", 44100, 2)


### Initialize Audio-Stream ###################################################
audioStream = sounddevice.Stream(samplerate=44100, callback=audioLoop)



### Controlls #################################################################
controlls.addControll('q', audioStream.stop, None)
controlls.addControll('s', saveTracks, None)

controlls.addControll('1', Track.tracks[1].nextState, None)
controlls.addControll('m', Track.tracks[0].nextState, None)


### MAIN - LOOP ###############################################################
audioStream.start()

while audioStream.active:
    controlls.checkForInput()
    
    time.sleep(0.005)
