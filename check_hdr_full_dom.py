with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'<div class="header-right-group">.*?</div>\s*</div>\s*</header>', text, re.DOTALL)
if m:
    print(m.group(0))
else:
    print("Match failed")
