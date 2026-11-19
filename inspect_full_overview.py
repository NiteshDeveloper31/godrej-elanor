import json

with open('godrej_pageProps.json', encoding='utf-8') as f:
    props = json.load(f)

item = props.get('item', {})

overview = item.get('overview', {}).get('document', [])
for block in overview:
    for child in block.get('children', []):
        print(child.get('text', ''))

print("\n--- NEARBY PLACES ---")
near = item.get('neighbourhood', {}).get('nearByPlaces', [])
for n in near:
    icon_name = n.get('icon', {}).get('name', '')
    name = n.get('name', '')
    dist = ''
    dist_doc = n.get('name_rich_text', {}).get('document', [])
    for d in dist_doc:
        for c in d.get('children', []):
            dist += c.get('text', '')
    print(f"* {name} ({icon_name}): {dist}")

print("\n--- AMENITIES LIST ---")
ams = item.get('amenities', [])
for a in ams:
    img = a.get('image', {}).get('url', '')
    desc = ''
    for d in a.get('description', {}).get('document', []):
        for c in d.get('children', []):
            desc += c.get('text', '')
    title = a.get('title', '')
    print(f"* Title: {title} | Desc: {desc} | Img: {img}")
