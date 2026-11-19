import re

with open('godrej_godrej-elanor.html', encoding='utf-8') as f:
    html = f.read()

tags = re.findall(r'<section[^>]*class=[\"\']([^\"\']+)[\"\'][^>]*>', html)
print("Sections found:")
for t in tags:
    print(" - section class:", t)

divs = re.findall(r'<(?:div|section)[^>]*(id=[\"\'][^\"\']+[\"\'])[^>]*>', html)
print("\nElements with IDs:")
for d in divs:
    print(" - ", d)
