with open('godrej_godrej-elanor.html', encoding='utf-8') as f:
    html = f.read()

import re

# Search for "Godrej Elanor" in html
for m in re.finditer(r'Godrej Elanor', html):
    pos = m.start()
    snippet = html[pos-200:pos+800]
    if 'banner' in snippet.lower() or 'overview' in snippet.lower() or 'carousel' in snippet.lower() or 'possession' in snippet.lower():
        print("=== Match ===")
        print(snippet)
        print("="*40)
