import json

with open('godrej_pageProps.json', encoding='utf-8') as f:
    data = json.load(f)

item = data.get('item', {})
print("banner_carousel:", json.dumps(item.get('banner_carousel'), indent=2))
print("mobile_banner_carousel:", json.dumps(item.get('mobile_banner_carousel'), indent=2))
