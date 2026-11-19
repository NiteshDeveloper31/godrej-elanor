with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos1 = html.find('<header')
pos2 = html.find('</header>')
print(html[pos1:pos2+9])
