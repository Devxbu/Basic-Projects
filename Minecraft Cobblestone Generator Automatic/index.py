import pyautogui
import time

while True:
    # Fare sol tuşa bas
    pyautogui.mouseDown(button='left')
    
    # 5 saniye boyunca beklemek için
    time.sleep(5)
    
    # Fare sol tuşu bırak
    pyautogui.mouseUp(button='left')
    
    # 5 saniye daha beklemek için
    time.sleep(5)
