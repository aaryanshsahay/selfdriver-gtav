import cv2
import os
import time 
import keyboard
import numpy as np


from grabscreen import GrabScreen


from model import GetPretrainedModel
from datacollection import Countdown
from getkeys import GetKeys


from tensorflow import keras


def GetPrediction(model):
	screen = GrabScreen(region = (0, 0, 1920, 1080))
	screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
	screen = cv2.resize(screen, (160,128))
	#print("Original shape => ",screen.shape)
	screen = screen.reshape(1,160,128,1)
	#print("Reshaped => ",screen.shape)
	return model.predict(screen)


#print(GetPrediction(keras.models.load_model("models/xception_custom_model.h5")))



def TurnRight():
	#keyboard.release("w")
	#keyboard.release("s")
	#keyboard.release("a")
	#keyboard.press("d")
	#keyboard.release("w")
	keyboard.press("d")
	time.sleep(0.4)
	keyboard.release("d")
	

def TurnLeft():
	#keyboard.release("w")
	#keyboard.release("s")
	#keyboard.release("d")
	#keyboard.press("a")
	#keyboard.release("w")
	keyboard.press("a")
	time.sleep(0.4)
	keyboard.release("a")
	

def MoveForward():
	keyboard.press("w")
	#time.sleep(0.5)
	#keyboard.release("w")

def GoStraight():
	keyboard.press("w")
	time.sleep(0.2)
	keyboard.release("w")
	

def Brakes():
	keyboard.release("w")
	keyboard.release("a")
	keyboard.release("d")
	keyboard.press("s")
	#keyboard.press("s")
	time.sleep(1)
	keyboard.release("s")
	


if __name__ == "__main__":
	is_paused = False
	path_to_model = "models/xception_custom_model.h5"
	nn_model = GetPretrainedModel(path_to_model)
	print("="*50,"STARING AI","="*50)
	Countdown(2)
	while True:
		if not is_paused:
		
			
			preds = GetPrediction(nn_model)[0]
			output_map = ['forward','left','slow','right']
			print(preds)
			result = output_map[np.argmax(np.around(preds))] 
			print(result)
			



			#MoveForward()

			if result == 'forward':
				#GoStraight()
				pass
			
			elif result == 'left':
				TurnLeft()

			elif result == 'slow':
				Brakes()	
			
			elif result == 'right':
				TurnRight()
			#prediction = GetPrediction(nn_model)[0]

			#Countdown(4)

			

		
			keys = GetKeys()
		
			if 't' in keys:
				if is_paused :
					print("resuming pause phase")
					is_paused = False
					time.sleep(1)
				else:
					print("entering pause phase")
					is_paused = True
					time.sleep(1)
			