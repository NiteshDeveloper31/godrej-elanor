import json

with open('godrej_pageProps.json', encoding='utf-8') as f:
    data = json.load(f)

item = data.get('pageProps', {}).get('item', {})
print("Item keys:")
for k in item.keys():
    if any(w in k.lower() for w in ['banner', 'header', 'nav', 'price', 'hero', 'project']):
        print("-", k)

print("\nBanner carousel:")
print(json.dumps(item.get('banner_carousel'), indent=2))
