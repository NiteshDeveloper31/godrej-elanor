with open('godrej_godrej-elanor.html', encoding='utf-8') as f:
    html = f.read()

import re

# Find header tag
header_match = re.search(r'<header[^>]*>.*?</header>', html, re.DOTALL)
if header_match:
    print("Found <header> tag:")
    header_html = header_match.group(0)
    print(header_html[:2000])
    with open('official_header.html', 'w', encoding='utf-8') as out:
        out.write(header_html)
else:
    print("Header tag not found with simple regex, search for header class or nav")
    for m in re.finditer(r'<nav[^>]*>.*?</nav>', html, re.DOTALL):
        print("Nav found:", m.group(0)[:500])
