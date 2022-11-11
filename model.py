import pandas as pd
import numpy as np

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

import tensorflow as tf

from grabscreen import GrabScreen

import cv2

#from self_driver import ReadyDataForModel


def GetBaselineModel(screen):
	inputs = keras.Input(shape = (160, 128, 1))

	x = Conv2D(filters = 32, kernel_size = 3, activation = "relu")(inputs)
	x = MaxPooling2D(pool_size = 2)(x)
	x = Conv2D(filters = 64, kernel_size = 3, activation = "relu")(x)
	x = MaxPooling2D(pool_size = 2)(x)
	x = Conv2D(filters = 128, kernel_size = 3, activatopm = "relu")(x)
	x = MaxPooling2D(pool_size = 2)(x)

	outputs = Dense(4, activation = "relu")

	model = keras.Model(name = "CustomModelv1", inputs = inputs, outputs = outputs)

	model.compile(
		loss = "categorical_crossentropy",
		optimizer = "adam",
		metrics = ["accuracy"]
		)

	return model


def GetPretrainedModel(path):
	xception_custom = keras.models.load_model(path)
	return xception_custom


def GetInput():
	screen = GrabScreen(region = (0, 0, 1920, 1080))
	screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
	screen = cv2.resize(screen, (160,128))
		
	return screen


