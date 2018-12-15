# SimpleTSMusicGenerator
Tensorflow-Powered Midi Song Generator from traning songs. But output is not even a song yet :(

In this repo you will find 3 folders , one for rock music , one for jazz music and one is a blank template that you can use to train with any music you like , but it won't sound anywhere near what you think.

### Warning : DO NOT open the sample output files if you cannot withstand a VERY BAD music.

## Requirements
python3 , numpy , tensorflow , mido , midiutil , h5py and maybe some other library I might forgot , sorry for that.

Also , all input,output is based on midi , so your traning data must coms from midi song.

## How to

1.Edit model.py and insert your traning midi files into the list(feel free to add other settings , I'm just a beginner in Tensorflow so currently it is quite a bad setting). Then just run it. This will generate and train the model.

2.If it's successful , then there should appear 3 .h5 files. you can proceed

3.Modify the gensong.py (Currently it does generate many songs in a row , you can make it into only 1 song). And run it , outputs will be in output/ folder

4.Prepare your ears and go listen.

### Congratulations

If you made it thorough the testing output phase , congrats , It's very bad I know. But this project is my breakthrough into machine-learning field. So forgive me if you're looking for something more serious.

Thanks
PoomrokC
