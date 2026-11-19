import urllib.request
import json
import subprocess
import time

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
proc = subprocess.Popen([
    chrome_path,
    "--headless=new",
    "--remote-debugging-port=9222",
    "http://localhost:8000/"
])

time.sleep(2)

try:
    tabs = json.loads(urllib.request.urlopen("http://localhost:9222/json").read())
    ws_url = tabs[0]["webSocketDebuggerUrl"]
    print("WebSocket URL:", ws_url)
    
    # We can use python websocket to evaluate expression
    import urllib.parse
    # Or simple node script
except Exception as e:
    print("Error:", e)
finally:
    proc.terminate()
