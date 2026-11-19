with open('styles.css', encoding='utf-8') as f:
    text = f.read()

import re
for m in re.finditer(r'@media[^{]+', text):
    start = m.start()
    block = text[start:start+1200]
    if 'mobile-sticky-footer-bar' in block:
        print("Found in media query:")
        print(block[:400])
