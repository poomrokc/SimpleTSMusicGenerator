from mido import Message, MidiFile, MidiTrack
import mido
import time

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

x=0
for i in range(2000):
	gg=input().strip().split()
	j="note_on"
	if(gg[0]=='1'):
		j="note_off"
	message = mido.Message(j,channel=int(gg[1]),note=int(gg[2]),velocity=int(gg[3]),time=float(gg[4]));
	track.append(message)
mid.save('new_song.mid')