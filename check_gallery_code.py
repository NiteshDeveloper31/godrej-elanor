with open('build_godrej_clone.py', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('id="gallery"')
if pos != -1:
    print(text[pos-100:pos+1500])
else:
    print("gallery not found")
