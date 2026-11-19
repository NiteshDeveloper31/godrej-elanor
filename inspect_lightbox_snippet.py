import re

with open('godrej_gallery.html', encoding='utf-8') as f:
    html = f.read()

pos = html.find('gallery-lightbox')
if pos != -1:
    print(html[pos-100:pos+1500])
else:
    print('gallery-lightbox not found')
