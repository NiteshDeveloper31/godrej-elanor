with open('styles.css') as f:
    text = f.read()

import re
matches = re.findall(r'min-width:\s*[^;]+;', text)
print("min-widths in styles.css:")
for m in set(matches):
    print(m)
