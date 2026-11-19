with open('styles.css', encoding='utf-8') as f:
    text = f.read()

import re
matches = [line for line in text.splitlines() if 'hero' in line.lower() and '{' in line]
for m in matches:
    print(m)
