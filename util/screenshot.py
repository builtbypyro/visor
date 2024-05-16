import base64
from mss import mss
import os
import pyautogui


def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return str("data:image/jpeg;base64," + base64.b64encode(image_file.read()).decode('utf-8'))



def screenshot():
    pyautogui.press("f")
    with mss() as sct:
      sct.shot()
    ss = encode_image("monitor-1.png")
    os.remove("monitor-1.png")
    pyautogui.press("esc")
    return ss
        
    