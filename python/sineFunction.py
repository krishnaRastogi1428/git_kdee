import math, pyautogui, time

def rad2deg(rad2degVar):
	rad2degVar = rad2degVar * (180/3.14159265358)
	return rad2degVar
	
def deg2rad(deg2radVar):
	deg2radVar = deg2radVar * (3.14159265358/180)
	return deg2radVar

def n2p(Number):
	if (Number < 0):
		Number = (-1) * Number
	return Number

	
#pyautogui.moveTo(683,384)
#pyautogui.dragRel(100,0, 1)

#print(pyautogui.size())

frequency = 1
waveLength = 1
amplitude = 10


time.sleep(1)
for i in range(int(361*frequency)):
	pxMove = int(amplitude * math.sin(deg2rad((90 + i) / waveLength)))
	
	X =  n2p(384 + int(i/2))
	Y = 300 + (1 * pxMove)
	
	#print(X, Y)
	#pyautogui.moveTo(X, Y)
	pyautogui.click(X, Y)

