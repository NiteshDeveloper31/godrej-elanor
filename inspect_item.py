import json

with open('godrej_pageProps.json', encoding='utf-8') as f:
    props = json.load(f)

item = props.get('item', {})
print("Item title:", item.get('title'))
print("Item name:", item.get('name'))
print("Item location:", item.get('location'))
print("Item sections / components:")

for k in item.keys():
    v = item[k]
    if isinstance(v, (list, dict)):
        print(f" - {k}: {type(v).__name__} (len: {len(v) if isinstance(v, list) else len(v.keys())})")
    else:
        print(f" - {k}: {str(v)[:60]}")
