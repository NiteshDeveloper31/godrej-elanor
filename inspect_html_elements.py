import re

with open('index.html', encoding='utf-8') as f:
    html = f.read()

print("Forms:")
for m in re.finditer(r'<form[^>]*>', html):
    print(m.group(0))

print("\nButtons with data-* or onclick or class containing toggle/trigger/tab/modal:")
for m in re.finditer(r'<button[^>]*>', html):
    b = m.group(0)
    if any(k in b for k in ['modal', 'tab', 'toggle', 'trigger', 'drawer', 'calc', 'open', 'close', 'accordion']):
        print(b)

print("\nAccordion triggers:")
for m in re.finditer(r'<[^>]*class="[^"]*acc[^"]*"[^>]*>', html):
    print(m.group(0))

print("\nScript tags in index.html:")
for m in re.finditer(r'<script[^>]*src="([^"]+)"[^>]*>', html):
    print(m.group(0))
