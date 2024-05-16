
import json
from util.chrome import get_driver
import validators
import pyautogui
from workers.vision import assist


def execute(steps):
    x = str(steps).replace("'", '"')
    steps = json.loads(x)
    for step in steps:
        print(step["step"])
        if step["step"] == "chrome":
            driver = get_driver()
            driver.get("https://google.com") 
        elif validators.url("https://" + step["step"]):
            print(step["step"])
            driver.get(str("https://" + step["step"]))
        else:
            print("Executing Vision Assist.")
            print(assist(step["step"]))
            
    