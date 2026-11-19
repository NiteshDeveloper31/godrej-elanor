import json
import re

with open('godrej_godrej-elanor.html', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html)
if m:
    data = json.loads(m.group(1))
    props = data.get('props', {}).get('pageProps', {})
    print('Keys in pageProps:', list(props.keys()))
    with open('godrej_pageProps.json', 'w', encoding='utf-8') as pf:
        json.dump(props, pf, indent=2)
    print('Saved pageProps to godrej_pageProps.json')
else:
    print('__NEXT_DATA__ not found')
