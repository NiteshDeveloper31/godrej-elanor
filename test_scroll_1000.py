script = """
<script>
window.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => {
    window.scrollTo(0, 1000);
  }, 100);
});
</script>
"""
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('scrolled_test2.html', 'w', encoding='utf-8') as f:
    f.write(html.replace('</head>', script + '</head>'))

import subprocess
import os
import tempfile
import shutil

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_scroll2 = os.path.join(tempfile.gettempdir(), "test_scrolled_1000.png")

cmd = f'"{chrome_path}" --headless=new --window-size=1440,900 --virtual-time-budget=2000 --screenshot="{temp_scroll2}" http://localhost:8000/scrolled_test2.html'
subprocess.run(cmd, shell=True)

if os.path.exists(temp_scroll2):
    shutil.copy(temp_scroll2, "scrolled_desktop_1000.png")
    print("Scrolled 1000px saved!")
