import pyautogui
import time

i = 1
while True:
    # Fare sol tuşa bas
    pyautogui.mouseDown(button='left')
    
    # 5 saniye boyunca beklemek için
    time.sleep(1.3)
    
    # Fare sol tuşu bırak
    pyautogui.mouseUp(button='left')
    
    # 1 saniye daha beklemek için
    time.sleep(0.4)

    pyautogui.press(str(i))

    if i == 9:
        i = 1
    else:
        i += 1
