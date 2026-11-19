import subprocess
import json

cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--window-size=390,844",
    "--run-all-compositor-stages-before-draw",
    "http://localhost:8000/"
]
# We can evaluate JavaScript in Chrome headless by creating an HTML inspector or injecting a script!
