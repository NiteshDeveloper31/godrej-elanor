import os
import subprocess

cwd = os.getcwd()
print("CWD:", cwd)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# Let's run chrome in cwd
cmd = f'"{chrome_path}" --headless=new --screenshot=new_mobile.png --window-size=390,844 http://localhost:8000/'
subprocess.run(cmd, shell=True, cwd=cwd)

cmd2 = f'"{chrome_path}" --headless=new --screenshot=new_desktop.png --window-size=1440,900 http://localhost:8000/'
subprocess.run(cmd2, shell=True, cwd=cwd)

print("new_mobile.png exists:", os.path.exists("new_mobile.png"))
print("new_desktop.png exists:", os.path.exists("new_desktop.png"))
