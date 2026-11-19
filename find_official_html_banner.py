with open('godrej_godrej-elanor.html', encoding='utf-8') as f:
    html = f.read()

import re
# Find banner or header in html
pos = html.find('INR 1.89')
if pos != -1:
    print("Found INR 1.89 in official HTML:")
    print(html[pos-300:pos+500])
else:
    print("INR 1.89 not found directly, let's search in pageProps")
