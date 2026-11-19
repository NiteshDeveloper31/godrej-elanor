with open('godrej_gallery.html', encoding='utf-8') as f:
    html = f.read()

pos = html.find('<h2>Gallery</h2>')
if pos == -1:
    pos = html.find('Gallery</h2>')
print(html[pos:pos+3000])
