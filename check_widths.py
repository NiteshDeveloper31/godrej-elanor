with open('styles.css') as f:
    text = f.read()

import re
fixed_widths = re.findall(r'width:\s*([0-9]+px)', text)
print("Fixed pixel widths in styles.css:", set(fixed_widths))
