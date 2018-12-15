from mido import MidiFile
import mido
import time
import numpy as np

def getEmptyList(size):
	lol = []
	for i in range(size):
		lol.append(0)
	return lol

def getMessages(name):
	mid = mido.MidiFile(name)
	output = mido.open_output()
	ans=[]
	nxt=set()
	for track in mid.tracks:
		t=0
		for msg in track:
			t+=msg.time
			if msg.type=='note_on':
				if msg.channel==9:
					ans.append([t,1,msg.note])
				else:
					ans.append([t,0,msg.note])
	ans=sorted(ans)
	n=len(ans)
	for i in range(n-1,0,-1):
		ans[i][0]=ans[i][0]-ans[i-1][0]
	ans[0][0]=0
	realoutput = []
	for t in ans:
		tt=[t[1],t[2],t[0]]
		realoutput.append(tt)
	return realoutput
	
def getData(name):
	messages=getMessages(name)
	data=[]
	labelType=[]
	labelNote=[]
	labelTime=[]
	n=len(messages)
	for i in range(10,n):
		jack=messages[i]
		#type
		type=getEmptyList(2)
		type[jack[0]]=1
		labelType.append(type)
		
		#Note
		Note=getEmptyList(128)
		Note[jack[1]]=1
		labelNote.append(Note)
		
		#Time
		if jack[2]>599:
			jack[2]=599
		Time=getEmptyList(600)
		Time[jack[2]]=1
		labelTime.append(Time)
		
		#data
		dat=[]
		for j in range(1,11):
			dat+=messages[i-j]
		data.append(dat)
	return data,labelType,labelNote,labelTime
	
	
def getNumpyAllData(songlist):
	data=[]
	labelType=[]
	labelNote=[]
	labelTime=[]
	for e in songlist:
		d,l,n,t=getData(e)
		data+=d
		labelType+=l
		labelNote+=n
		labelTime+=t
	return np.asarray(data),np.asarray(labelType),np.asarray(labelNote),np.asarray(labelTime)