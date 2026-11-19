with open('godrej_fcbe.css', encoding='utf-8') as f:
    css = f.read()

import re

for sel in ['.main-header', '.headroom', 'header', '.single-page-scroll', '.back-block']:
    print(f"=== {sel} ===")
    matches = re.findall(re.escape(sel) + r'[^\{]*\{[^\}]+\}', css)
    for m in matches[:6]:
        print(m)
