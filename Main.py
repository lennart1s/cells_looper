import sounddevice
import time

import GPIOControlls as controlls
import Track

from Loop import audioLoop


def saveTracks():
    #Track.tracks[0].saveToFile("yeah.wav", 44100, 2)
    #Track.tracks[0].saveToFile("met.wav", 44100, 2)


### Initialize Audio-Stream ###################################################
audioStream = sounddevice.Stream(samplerate=44100, callback=audioLoop)



### Controlls #################################################################
#controlls.addControll('q', audioStream.stop, None)
#controlls.addControll('s', saveTracks, None)

#controlls.addControll('1', Track.tracks[0].nextState, None)
controlls.addControll('2', Track.tracks[0].nextState, None)
#controlls.addControll('2', Track.tracks[1].nextState, None)
controlls.addControll('3', Track.tracks[1].nextState, None)
#controlls.addControll('m', Track.metronome.nextState, None)
controlls.addControll('4', Track.metronome.nextState, None)




### MAIN - LOOP ###############################################################
audioStream.start()

while audioStream.active:
    controlls.checkForInput()
    
    time.sleep(0.005)

    print(Track.metronome.pos,"/",len(Track.metronome.data), "   ",Track.tracks[0].pos,"/",len(Track.tracks[0].data), "   ",Track.tracks[1].pos,"/",len(Track.tracks[1].data))
