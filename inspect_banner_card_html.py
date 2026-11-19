with open('godrej_godrej-elanor.html', encoding='utf-8') as f:
    html = f.read()

pos = html.find('Property Banner Image')
print(html[pos+500:pos+2500])
