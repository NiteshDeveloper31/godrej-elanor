with open('build_godrej_clone.py', encoding='utf-8') as f:
    text = f.read()

import re
matches = [line for line in text.splitlines() if 'sticky' in line.lower() or 'bottom-bar' in line.lower()]
print("Matches for sticky / bottom-bar in build_godrej_clone.py:")
for m in matches:
    print(m)
