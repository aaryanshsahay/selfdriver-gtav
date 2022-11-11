import numpy as np
import cv2
import time
import keyboard


import os

from grabscreen import GrabScreen
from getkeys import GetKeys


def KeysToOutput(keys):
	# [w, a, s, d]
	output = [0, 0, 0, 0]

	if 'W' in keys:
		output[0] = 1

	if 'A' in keys:
		output[1] = 1

	if 'S' in keys:
		output[2] = 1

	if 'D' in keys:
		output[3] = 1

	if 'E' in keys:
		print("Sleeping for 15 seconds")
		Countdown(15)

	else:
		pass

	return output


def Countdown(z):
	for i in range(z+1)[::-1]:
		print(i)
		time.sleep(1)

def GetData():
	screen = GrabScreen(region = (0, 0, 1920, 1080))
	screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
	screen = cv2.resize(screen, (160,128))
	keys = GetKeys()
	output = KeysToOutput(keys)
	
	#return screen, keys
	training_data.append([screen,output])


if __name__ == "__main__":

	file_name = "training_data_"

	#if os.path.isfile(file_name):
	#	print("File already exists, loading previous data.")
	#	training_data = list(np.load(file_name, allow_pickle = True))

	#else:
	#	print("File does not exist, starting fresh")
	#	training_data = []

	training_data = []

	print("Press 'E' to stop program for 15 seconds.")
	
	time.sleep(1)

	print("Starting data collection !!!!!!!!")
	Countdown(z = 10)

	count = 2
	while True:
		initial_time = time.time()
		#screen,keys = GetData()
		GetData()
		print(f"Frame took {time.time()-initial_time} seconds")
		#cv2.imshow("screen", screen)
		#if cv2.waitKey(25) & 0xFF == ord('q'):
		#	cv2.destroyAllWindows()
		#	break

		#print(keys)

		if len(training_data) % 2000 == 0:
			print("="*50, len(training_data), "="*50)
			pass

		if len(training_data)  % 10000 == 0:
			print("="*50,len(training_data),"="*50)
			print("Saving Data")
			np.save(str(file_name)+str(count)+".npy", training_data)
			count+=1