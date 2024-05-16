from openai import OpenAI 
from util.screenshot import screenshot
import os

MODEL="gpt-4o"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "keyhere"))



def assist(task):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful vision assistant that responds in JSON. You have 3 commands at your disposal. Click, Press, and Type. You are meant to analyze the image that is provided and try to accomplish the the task provided. The image will be a screenshot of te user's current screen with yellow boxes with 1-2 character sequences inside of them which are placed near elements you can interact with. You can control the screen using these elements. To click an element, you will output the 1-2 character sequence that corresponds to that element. To press a certain key, output the key that needs to be pressed. To type something, output the thing that needs to be typed. You only respond in JSON or bad things will happen. Make sure that the sequences you reference are actually on the screen."},
            {"role": "user", "content": [
                {"type": "text", "text": task},
                {"type": "image_url", "image_url": {
                    "url": screenshot()
                }
                }
            ]}
        ],
        temperature=0.0,
    )

    return (response.choices[0].message.content)