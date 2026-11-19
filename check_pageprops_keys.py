import json

with open('godrej_pageProps.json', encoding='utf-8') as f:
    data = json.load(f)

print("Root keys:", list(data.keys()))
if 'pageProps' in data:
    print("pageProps keys:", list(data['pageProps'].keys()))
    for k in data['pageProps']:
        print(f"Key: {k}, type: {type(data['pageProps'][k])}")
