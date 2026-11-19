import re

with open('godrej_godrej-elanor.html', encoding='utf-8') as f:
    html = f.read()

# Let's find nav links in header
nav_links = re.findall(r'<a[^>]*href=[\"\']([^\"\']+)[\"\'][^>]*>(.*?)</a>', html)
print("Nav links found in godrej-elanor:")
for href, text in nav_links:
    clean_text = re.sub(r'<[^>]+>', '', text).strip()
    if clean_text and any(k in href for k in ['godrej-elanor', 'overview', 'price', 'gallery', 'floor', 'amenities', 'location']):
        print(f" - {clean_text}: {href}")
