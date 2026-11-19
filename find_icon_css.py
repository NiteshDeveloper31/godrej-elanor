with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = [line for line in css.splitlines() if 'hdr-icon-circle' in line]
for m in matches:
    print(m)
