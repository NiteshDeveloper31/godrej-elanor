import re

with open('build_godrej_clone.py', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'https://gplstorageaccount.blob.core.windows.net/[^\s"\']+', text)
print('Total Azure blob images in build_godrej_clone.py:', len(matches))
for m in matches[:5]:
    print('-', m)
