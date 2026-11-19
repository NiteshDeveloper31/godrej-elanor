import json

with open('godrej_pageProps.json', encoding='utf-8') as f:
    data = json.load(f)

item = data.get('item', {})
print("item keys:", list(item.keys()))
for k in item:
    val = str(item[k])
    if len(val) > 100:
        val = val[:100] + '...'
    print(f"  {k}: {val}")
