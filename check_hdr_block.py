with open('styles.css') as f:
    text = f.read()

pos = text.find('.godrej-site-header {')
print(text[pos:pos+1500])
