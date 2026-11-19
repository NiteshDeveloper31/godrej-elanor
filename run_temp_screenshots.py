import os
import subprocess
import tempfile
import shutil

temp_dir = tempfile.gettempdir()
temp_mobile = os.path.join(temp_dir, "new_mobile_test.png")
temp_desktop = os.path.join(temp_dir, "new_desktop_test.png")

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Mobile
cmd1 = f'"{chrome_path}" --headless=new --screenshot="{temp_mobile}" --window-size=390,844 http://localhost:8000/'
res1 = subprocess.run(cmd1, shell=True)

# Desktop
cmd2 = f'"{chrome_path}" --headless=new --screenshot="{temp_desktop}" --window-size=1440,900 http://localhost:8000/'
res2 = subprocess.run(cmd2, shell=True)

print("Temp mobile exists:", os.path.exists(temp_mobile))
print("Temp desktop exists:", os.path.exists(temp_desktop))

if os.path.exists(temp_mobile):
    shutil.copy(temp_mobile, "verified_mobile.png")
    print("Copied to verified_mobile.png")

if os.path.exists(temp_desktop):
    shutil.copy(temp_desktop, "verified_desktop.png")
    print("Copied to verified_desktop.png")
