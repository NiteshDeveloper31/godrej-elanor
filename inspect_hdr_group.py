with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('header-right-group')
print(html[pos:pos+1000])
