import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import time
import cv2

#import matplotlib.pyplot as plt

start = time.time()

data_1 = np.load("training_data.npy", allow_pickle = True)
data_2 = np.load("training_data_0.npy", allow_pickle = True)
data_3 = np.load("training_data_1.npy", allow_pickle = True)
data_4 = np.load("training_data_2.npy", allow_pickle = True)
print(data_1[0][0].shape)

print("="*100)
training_data = np.concatenate((data_1,data_2, data_3, data_4), axis=0)

#print(len(training_data))
'''
for data in training_data:
	img = data[0]
	choice = data[1]
	cv2.imshow('test',img)
	print(choice)

	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
'''

df = pd.DataFrame(training_data)
print(Counter(df[1].apply(str)))
# [W, A, S, D]

# 1) [1, 0, 0, 0] => W
# 2) [0, 0, 0, 0] => No keys pressed (drop)
# 3) [1, 1, 0, 0] => A only (set all 0 index vals to 0)
# 4) [1, 0, 0, 1] => D only (set all 0 index vals to 0)
# 5) [0, 0, 1, 0] => S 
# 6) [0, 0, 0, 1] => D
# 7) [0, 1, 0, 0] => A
# 8) [0, 0, 1, 1] => D only (set all 2 index vals to 0)
# 9) [0, 1, 1, 0] => A only (set all 2 index vals to 0)
# 10) [1, 1, 1, 1] => Drop
# 11) [1, 1, 0, 1] => Drop
# 12) [1, 0, 1, 0] => Drop
# 13) [0, 1, 1, 1] => Drop
# 14) [1, 1, 1, 0] => Drop


for i in range(len(df[1])):
  # Dropping useless ones
  # 10, 11, 12, 13, 14
  
  if (df.iloc[i][1] == [1,1,1,0]) or (df.iloc[i][1] == [1,0,1,0]) or (df.iloc[i][1] == [1,1,1,1]) or (df.iloc[i][1] == [0,0,0,0]) or (df.iloc[i][1] == [0,1,0,1]) or (df.iloc[i][1] == [0,1,1,1]) or (df.iloc[i][1] == [1,1,0,1]):
  	df.iloc[i][1] = np.nan 
  
  # A only
  # 9
  if (df.iloc[i][1] == [0, 1, 1, 0]):
    df.iloc[i][1] = [0, 1, 0, 0]
  
  # D only
  # 8 
  if (df.iloc[i][1] == [0, 0, 1, 1]):
    df.iloc[i][1] = [0, 0, 0, 1]
  
  # D only 
  # 4
  if (df.iloc[i][1] == [1, 0, 0, 1]):
    df.iloc[i][1] = [0, 0, 0, 1]
  
  # A only
  # 3
  if (df.iloc[i][1] == [1, 1, 0, 0]):
    df.iloc[i][1] = [0, 1, 0, 0]

df.dropna(inplace = True)


print(Counter(df[1].apply(str)))


output = df.to_numpy()
print(output)



## balacing data

rights = []
lefts = []
forwards = []
brakes = []


shuffle(output)

for data in output:
	img = data[0]
	choice = data[1]

	if choice == [1,0,0,0]:
		forwards.append([img,choice])

	elif choice == [0,1,0,0]:
		lefts.append([img,choice])
	
	elif choice == [0,0,1,0]:
		brakes.append([img,choice])
	
	elif choice == [0,0,0,1]:
		rights.append([img,choice])

	else:
		print("No Matches")


forwards = forwards[:len(lefts)][:len(rights)]
lefts = lefts[:len(forwards)]
rights = rights[:len(rights)]

final_data = forwards + lefts + rights + brakes

shuffle(final_data)
print(len(final_data))
np.save("balanced_data.npy", final_data)


end = time.time()
print("Time Taken : ",end-start)