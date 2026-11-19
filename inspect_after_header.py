with open('godrej_godrej-elanor.html', encoding='utf-8') as f:
    html = f.read()

pos = html.find('</header>')
if pos != -1:
    print(html[pos:pos+3500])
else:
    print("</header> not found")
