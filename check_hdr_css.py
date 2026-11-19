with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
pos = css.find('.header-logo-script')
print(css[pos-100:pos+300])

pos2 = css.find('.godrej-site-header')
print(css[pos2:pos2+600])
