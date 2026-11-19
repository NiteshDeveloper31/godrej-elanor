import re

with open('index.html', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section[^>]*id="([^"]+)"[^>]*>', html)
print("Sections in order:")
for idx, s in enumerate(sections, 1):
    print(f"{idx}. #{s}")
