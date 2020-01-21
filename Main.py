import sounddevice
import time

import KeyboardControlls as controlls

from Loop import audioLoop



audioStream = sounddevice.Stream(samplerate=44100, callback=audioLoop)


controlls.addControll('q', audioStream.stop, None)



# MAIN - LOOP #################################################################
audioStream.start()

while audioStream.active:
    controlls.checkForInput()
    
    time.sleep(0.005)
