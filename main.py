from workers.summarize import summarize
from util.format import prepare
from util.gpt import generate
from workers.planner import planAgain, initialPlan
from workers.executor import execute

import json
import requests


x = [
  {"step": "chrome"},
  {"step": "youtube.com"},
  {"step": "click on the search box"},
  {"step": "type Rick Astley - Never Gonna Give You Up"},
  {"step": "press enter"},
  {"step": "click on the first video result"}
]

x = r"" + str(x)

execute(x)



# print(json.loads(initialPlan("open the rick roll video on youtube"))["choices"][0]["message"]["content"])


