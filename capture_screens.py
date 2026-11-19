import os
import subprocess

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

browser = chrome_path if os.path.exists(chrome_path) else (edge_path if os.path.exists(edge_path) else None)
print("Browser path:", browser)

if browser:
    # Mobile screenshot
    cmd = [
        browser,
        "--headless=new",
        "--screenshot=mobile_capture.png",
        "--window-size=390,844",
        "http://localhost:8000/"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Mobile res:", res.returncode)

    # Desktop screenshot
    cmd = [
        browser,
        "--headless=new",
        "--screenshot=desktop_capture.png",
        "--window-size=1440,900",
        "http://localhost:8000/"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Desktop res:", res.returncode)
