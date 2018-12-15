import tensorflow as tf
import process
import numpy as np
from tensorflow.keras import layers,optimizers,models
from random import randint

def generateUntil(timeMax,posMax):
	modelType = models.load_model('rock44Type.h5')
	modelNote = models.load_model('rock44Note.h5')
	modelTime = models.load_model('rock44Time.h5')
	start=[
			[randint(0,1),randint(0,127),randint(0,599)],
			[randint(0,1),randint(0,127),randint(0,599)],
			[randint(0,1),randint(0,127),randint(0,599)],
			[randint(0,1),randint(0,127),randint(0,599)],
			[randint(0,1),randint(0,127),randint(0,599)],
			[randint(0,1),randint(0,127),randint(0,599)],
			[randint(0,1),randint(0,127),randint(0,599)],
			[randint(0,1),randint(0,127),randint(0,599)],
			[randint(0,1),randint(0,127),randint(0,599)],
			[randint(0,1),randint(0,127),randint(0,599)]
		]
	nowtime=0
	pos=5
	while(nowtime<timeMax and pos<posMax):
		dat=[]
		for j in range(1,11):
			dat+=start[pos-j]
		input=[dat]
		input=np.asarray(input)
		resultType=list(modelType.predict(input)[0])
		resultNote=list(modelNote.predict(input)[0])
		resultTime=list(modelTime.predict(input)[0])
		start.append([np.argmax(resultType),np.argmax(resultNote),np.argmax(resultTime)])
		nowtime+=np.argmax(resultTime)
		pos+=1
	return start[10:]