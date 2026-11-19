import re

with open('index.html', encoding='utf-8') as f:
    text = f.read()

ids = set(re.findall(r'id="([^"]+)"', text))
print("Total IDs found:", len(ids))
for i in sorted(ids):
    print("-", i)
