# Click and drag the mouse
import pyautogui
import math
import time

# 5 seconds cooldown to allow user to terminate the program by moving the mouse to one of the 4 corners
time.sleep(5)
# Radius 
R = 100
# measuring screen size
(x,y) = pyautogui.size()
# locating center of the screen 
(X,Y) = (int(x/2), int(y/2))

#click the paint window tab
#pyautogui.click(300,1064)
# offsetting by radius 
pyautogui.moveTo(X,Y+R)


# converts angle(degrees) to radians
# Radians = π * angle / 180 
# x = radius * Sin(Radian(angle))
# y = radius * Cos(Radian(angle));

for i in range(361):
    if i%6==0: #adjust speed
        pyautogui.dragTo(X+R*math.sin(math.radians(i)), Y+R*math.cos(math.radians(i)))
