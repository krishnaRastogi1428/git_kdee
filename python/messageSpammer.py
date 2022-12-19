import time, pyautogui 

msg = input("Enter the message: ")
n = input("How many times ?: ")
time.sleep(5) # This will pause program for 5 seconds... 

for i in range(0,int(n)):
  pyautogui.typewrite(msg + '\n')