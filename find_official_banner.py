import json
import re

with open('godrej_pageProps.json', encoding='utf-8') as f:
    data = json.load(f)

# Let's search for banner, hero, or gallery images
def find_urls(obj, key_path=""):
    results = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            results.extend(find_urls(v, f"{key_path}.{k}"))
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            results.extend(find_urls(item, f"{key_path}[{idx}]"))
    elif isinstance(obj, str):
        if any(ext in obj.lower() for ext in ['.jpg', '.jpeg', '.png', '.webp']):
            results.append((key_path, obj))
    return results

urls = find_urls(data)
print(f"Total image URLs in pageProps: {len(urls)}")
for path, u in urls:
    if any(term in path.lower() or term in u.lower() for term in ['banner', 'hero', 'desktop', 'mobile', 'main', 'elanor', 'cover']):
        print(f"{path} -> {u}")
