with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

pos = css.find('@media (max-width: 768px)')
print(css[pos:pos+1200])
