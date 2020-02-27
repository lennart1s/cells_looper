package main

import "github.com/gordonklaus/portaudio"

func main() {
	portaudio.Initialize()
	defer portaudio.Terminate()
	in := make([]int32, 64)
	out := make([]int32, 64)
	stream, err := portaudio.OpenDefaultStream(1, 1, 44100, len(in), in, out)
	if err != nil {
		panic(err)
	}
	defer stream.Close()
	stream.Start()
	for {
		stream.Read()
		out = in
		stream.Write()
	}
}
