with open('styles.css', encoding='utf-8') as f:
    text = f.read()

import re
matches = [line for line in text.splitlines() if 'mobile-sticky-footer-bar' in line]
print("Matches in styles.css:", len(matches))
for m in matches:
    print(m)

pos = text.find('.mobile-sticky-footer-bar')
if pos != -1:
    print(text[pos:pos+500])
