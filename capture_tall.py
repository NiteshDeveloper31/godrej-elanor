import os
import subprocess

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cwd = os.path.abspath(".")

mobile_tall = os.path.join(cwd, "mobile_full_page.png")
cmd = [
    chrome_path,
    "--headless=new",
    f"--screenshot={mobile_tall}",
    "--window-size=390,6500",
    "--hide-scrollbars",
    "http://localhost:8000/"
]
res = subprocess.run(cmd, capture_output=True, text=True)
print("Mobile tall captured:", res.returncode, os.path.exists(mobile_tall), os.path.getsize(mobile_tall) if os.path.exists(mobile_tall) else 0)
