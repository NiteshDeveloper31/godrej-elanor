import json
import urllib.request
import os

with open('godrej_pageProps.json', encoding='utf-8') as f:
    data = json.load(f)

item = data.get('item', {})

headers = {'User-Agent': 'Mozilla/5.0'}

def download_file(url, target_path):
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    if os.path.exists(target_path) and os.path.getsize(target_path) > 1000:
        return
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(target_path, 'wb') as f:
            f.write(resp.read())
        print(f"Downloaded: {target_path} ({os.path.getsize(target_path)} bytes)")
    except Exception as e:
        print(f"Failed {url}: {e}")

# 1. Overview image
if 'overview_image' in item and item['overview_image'] and 'url' in item['overview_image']:
    download_file(item['overview_image']['url'], 'assets/images/godrej-cdn/overview-image-1740x810.webp')

# 2. Amenity banner image
if 'amenity_banner_image' in item and item['amenity_banner_image'] and 'url' in item['amenity_banner_image']:
    download_file(item['amenity_banner_image']['url'], 'assets/images/godrej-cdn/amenity-banner-1440x210.webp')

# 3. Amenities
amenities = item.get('amenities', [])
for idx, a in enumerate(amenities):
    img = a.get('image', {})
    if img and 'url' in img:
        download_file(img['url'], f'assets/images/godrej-cdn/amenities/official-amenity-{idx+1}.webp')

# 4. Galleries
galleries = item.get('galleries', [])
for idx, g in enumerate(galleries):
    img = g.get('image', {})
    if img and 'url' in img:
        download_file(img['url'], f'assets/images/godrej-cdn/gallery/official-gal-{idx+1}.webp')

print("Finished downloading official assets!")
