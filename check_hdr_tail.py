with open('styles.css') as f:
    text = f.read()

pos = text.find('width: 106px;')
print(text[pos:pos+600])
