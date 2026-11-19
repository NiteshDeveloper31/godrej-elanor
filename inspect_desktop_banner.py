with open('godrej_godrej-elanor.html', encoding='utf-8') as f:
    html = f.read()

pos = html.find('Godrej Elanor Property Banner Image')
if pos != -1:
    print(html[pos-100:pos+3000])
else:
    print("Desktop banner not found by name")
