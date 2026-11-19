with open('godrej_fcbe.css', encoding='utf-8') as f:
    css = f.read()

import re

for sel in ['.property-details-info', '.property-details-hero-section', '.single-page-scroll', '.back-block']:
    print(f"=== {sel} ===")
    for m in re.finditer(re.escape(sel) + r'[^\{]*\{[^\}]+\}', css):
        print(m.group(0))
