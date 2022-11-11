import win32api as wapi
import time

keyList = ["\b"]

for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\":
	keyList.append(char)


def GetKeys():
	keys = []
	for key in keyList :
		if wapi.GetAsyncKeyState(ord(key)):
			keys.append(key)

	return keys