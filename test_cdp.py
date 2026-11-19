import os
import subprocess

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cwd = os.path.abspath(".")

# We can inject scroll script or capture full page using --default-background-color=0 or CDP, 
# or capture at different window heights.
# Let's write an html wrapper or use a python script with CDP to take a full page screenshot.
import urllib.request
import json

# Or we can launch chrome with remote debugging and take full page screenshot via CDP!
print("Starting CDP full-page capture...")
cmd = [
    chrome_path,
    "--headless=new",
    "--remote-debugging-port=9222",
    "about:blank"
]
proc = subprocess.Popen(cmd)

import time
time.sleep(2)

try:
    tabs = json.loads(urllib.request.urlopen("http://localhost:9222/json").read())
    ws_url = tabs[0]["webSocketDebuggerUrl"]
    print("WS URL:", ws_url)
except Exception as e:
    print("CDP err:", e)
finally:
    proc.terminate()
