with open('styles.css', encoding='utf-8') as f:
    css = f.read()

import re
selectors = re.findall(r'([.#][a-zA-Z0-9_-]+)\s*\{', css)
print("Total unique CSS selectors:", len(set(selectors)))
for s in sorted(set(selectors))[:40]:
    print(s)
