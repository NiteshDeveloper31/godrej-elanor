with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

debug_script = """
<script>
window.addEventListener('load', () => {
  const wideElements = [];
  document.querySelectorAll('*').forEach(el => {
    const rect = el.getBoundingClientRect();
    if (rect.width > 390 || rect.right > 390) {
      wideElements.push({
        tag: el.tagName,
        id: el.id,
        className: el.className,
        width: rect.width,
        right: rect.right
      });
    }
  });
  document.title = 'WIDE:' + JSON.stringify(wideElements.slice(0, 15));
});
</script>
"""

html_with_debug = html.replace('</head>', debug_script + '</head>')
with open('debug_wide.html', 'w', encoding='utf-8') as f:
    f.write(html_with_debug)

import subprocess
import re

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = f'"{chrome_path}" --headless=new --dump-dom --window-size=390,844 http://localhost:8000/debug_wide.html'
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)

m = re.search(r'<title>(.*?)</title>', res.stdout)
if m:
    print(m.group(1))
