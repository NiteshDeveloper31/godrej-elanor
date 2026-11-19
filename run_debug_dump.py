import subprocess

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = f'"{chrome_path}" --headless=new --dump-dom --window-size=390,844 http://localhost:8000/debug.html'
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)

import re
m = re.search(r'<title>(.*?)</title>', res.stdout)
if m:
    print(m.group(1))
else:
    print("Title not found")
