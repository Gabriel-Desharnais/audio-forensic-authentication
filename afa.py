#! /usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import moviepy
import moviepy.editor
import argparse

# This file launch is the interface to launch the tests. It runs python 3 and is developed for linux platform.

def openAudioFile(fileName):
	# This function will open the file @ fileName and prepare for manipulation with the help of moviepy
	
	# Open file in a clip
	clip = moviepy.editor.VideoFileClip(fileName)
	return clip.audio.to_soundarray(nbytes=4), clip.duration
	
def showInViewer(raw, duration):
	# This function will show data in a pyplot instance
	l = raw[:,0]
	r = raw[:,1]
	t = np.linspace(0,duration,raw.shape[0])
	plt.plot(t, l)
	plt.xlabel("temps (s)")
	plt.show()

if __name__=="__main__":
	# Stuff to parse the input of the program
	parser = argparse.ArgumentParser(description='Forensic analysis of audio file.')
	parser.add_argument('audioFileName',type=str, help='path to an audio file')
	parser.add_argument('--Viewer', '-V', help='Open a pyplot Viewer', action='store_true')
	args = parser.parse_args()
	
	# open audio file
	raw, duration = openAudioFile(args.audioFileName)
	
	# Show results
	if args.Viewer:
		showInViewer(raw, duration)
