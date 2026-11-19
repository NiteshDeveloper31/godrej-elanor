with open('styles.css', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('.hero-section')
if pos != -1:
    print(text[pos:pos+1500])
