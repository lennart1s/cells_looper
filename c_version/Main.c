#include "portaudio.h"
#include <stdio.h>

int main() {
    printf("Hello World\n");
    Pa_Initialize();
    return 0;
}

static int callback(const void *inputBuffer, void *outputBuffer, unsigned long framesPerBuffer, 
                        const PaStreamCallbackTimeInfo* timeInfo, PaStreamCallbackFlags statusFlags,
                        void *userData) {

    printf(framesPerBuffer);
}

