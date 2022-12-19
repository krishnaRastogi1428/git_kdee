import pyautogui, time

def clear():
	pyautogui.typewrite("cls")
	pyautogui.hotkey("enter")

time.sleep(5)
print(pyautogui.size())

pyautogui.moveTo(683, 384, 0.5)

clear()
