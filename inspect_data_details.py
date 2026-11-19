import json

with open('godrej_pageProps.json', encoding='utf-8') as f:
    props = json.load(f)

item = props.get('item', {})

print("=== BANNER CAROUSEL ===")
print(json.dumps(item.get('banner_carousel'), indent=2)[:500])

print("\n=== OVERVIEW ===")
print(json.dumps(item.get('overview'), indent=2)[:500])

print("\n=== AMENITIES ===")
print(json.dumps(item.get('amenities'), indent=2)[:500])

print("\n=== STARTING PRICES ===")
print(json.dumps(item.get('starting_prices'), indent=2))
print("Minimum price:", json.dumps(item.get('minimum_price'), indent=2))

print("\n=== NEIGHBOURHOOD / LOCATION ===")
print(json.dumps(item.get('neighbourhood'), indent=2)[:800])

print("\n=== RERA DETAILS ===")
print(json.dumps(item.get('rera_details_rich'), indent=2))
