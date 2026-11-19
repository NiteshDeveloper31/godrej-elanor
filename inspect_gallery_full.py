import re

with open('godrej_gallery.html', encoding='utf-8') as f:
    html = f.read()

# Let's inspect the entire body of godrej_gallery.html
# Find the div structure
for line in html.split('\n'):
    if any(k in line for k in ['gallery-lightbox', 'parent-div', 'children-dev', 'tab-list']):
        print(line[:300])
