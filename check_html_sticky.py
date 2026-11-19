with open('index.html', encoding='utf-8') as f:
    text = f.read()

pos = text.find('mobile-sticky-footer-bar')
print("Position in index.html:", pos)
if pos != -1:
    print(text[pos-100:pos+800])
