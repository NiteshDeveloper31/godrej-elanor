import os
import subprocess

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cwd = os.path.abspath(".")

mobile_out = os.path.join(cwd, "new_mobile_capture.png")
desktop_out = os.path.join(cwd, "new_desktop_capture.png")

# Mobile
cmd = [
    chrome_path,
    "--headless=new",
    f"--screenshot={mobile_out}",
    "--window-size=390,844",
    "--hide-scrollbars",
    "http://localhost:8000/"
]
res1 = subprocess.run(cmd, capture_output=True, text=True)

# Desktop
cmd = [
    chrome_path,
    "--headless=new",
    f"--screenshot={desktop_out}",
    "--window-size=1440,900",
    "--hide-scrollbars",
    "http://localhost:8000/"
]
res2 = subprocess.run(cmd, capture_output=True, text=True)

print("Mobile:", res1.returncode, os.path.exists(mobile_out), os.path.getsize(mobile_out) if os.path.exists(mobile_out) else 0)
print("Desktop:", res2.returncode, os.path.exists(desktop_out), os.path.getsize(desktop_out) if os.path.exists(desktop_out) else 0)
