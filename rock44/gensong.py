import tensorflow as tf
import process
import numpy as np
from tensorflow.keras import layers,optimizers,models
from random import randint
import predict
from midiutil import MIDIFile
import datetime

def gensong():
	channelDrum  = 9
	channelNote = 0
	duration = 1
	tempo	= 300
	volume   = 115

	MyMIDI = MIDIFile(1)
	MyMIDI.addTempo(0, 0, tempo)

	nlist = predict.generateUntil(5000,5000)
	print(nlist)

	time=0
	for e in nlist:
		time+=e[2]
		if e[0]==1:
			MyMIDI.addNote(0, channelDrum, e[1], time/100, duration, volume)
		else:
			MyMIDI.addNote(0, channelNote, e[1], time/100, duration, volume)
	now = datetime.datetime.now()
	with open("output/"+now.strftime("%B_%d_%Y_%H_%M_%S")+".mid", "wb") as output_file:
		MyMIDI.writeFile(output_file)

for i in range(10):
	gensong()
