def audioLoop(indata, outdata, frames, time, status):
    outdata[:] = 0
    outdata[:len(indata)] += indata