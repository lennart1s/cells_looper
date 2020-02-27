package main

import "github.com/gordonklaus/portaudio"

func main() {
	portaudio.Initialize()
	defer portaudio.Terminate()
	data := make([]int32, 64)
	stream, err := portaudio.OpenDefaultStream(1, 1, 44100, len(data), data)
	if err != nil {
		panic(err)
	}
	defer stream.Close()
	stream.Start()
	for {
		stream.Read()
		stream.Write()
	}
}
