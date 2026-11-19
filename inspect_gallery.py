import json
import re

with open('godrej_gallery.html', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html)
if m:
    data = json.loads(m.group(1))
    props = data.get('props', {}).get('pageProps', {})
    item = props.get('item', {})
    print("Gallery keys in item:")
    galleries = item.get('galleries', [])
    print(f"Total galleries: {len(galleries)}")
    for i, g in enumerate(galleries):
        cat = g.get('category') or g.get('title') or g.get('name')
        img = g.get('image', {})
        url = img.get('url') if isinstance(img, dict) else ''
        print(f"[{i}] {cat} - {url}")
        
    # Also print header, nav and structure
    print("\nPage structure / component hierarchy:")
else:
    print('__NEXT_DATA__ not found in gallery')
