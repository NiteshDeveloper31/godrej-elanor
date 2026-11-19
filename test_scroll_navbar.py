import subprocess
import tempfile
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_scroll = os.path.join(tempfile.gettempdir(), "test_scrolled.png")

# Run chrome with a scroll script
script = """
<script>
window.addEventListener('load', () => {
  window.scrollTo(0, 350);
});
</script>
"""
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('scrolled_test.html', 'w', encoding='utf-8') as f:
    f.write(html.replace('</head>', script + '</head>'))

cmd = f'"{chrome_path}" --headless=new --window-size=1440,900 --screenshot="{temp_scroll}" http://localhost:8000/scrolled_test.html'
subprocess.run(cmd, shell=True)

if os.path.exists(temp_scroll):
    import shutil
    shutil.copy(temp_scroll, "scrolled_desktop.png")
    print("Scrolled desktop screenshot saved!")
