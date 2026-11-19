with open('styles.css', encoding='utf-8') as f:
    text = f.read()

pos = text.find('.godrej-hero-section')
print(text[pos:pos+1500])
