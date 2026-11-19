import re

with open('godrej_gallery.html', encoding='utf-8') as f:
    html = f.read()

# Let's extract all image URLs in godrej_gallery.html
images = re.findall(r'https%3A%2F%2F[^\s&"\']+\.webp', html)
if not images:
    images = re.findall(r'https://gplwebsitecdnblob\.blob\.core\.windows\.net/godrej-cdn/Images/[^\s"\']+\.webp', html)

import urllib.parse
decoded_imgs = [urllib.parse.unquote(img) for img in images]
print(f"Total decoded webp images in gallery: {len(decoded_imgs)}")
for u in set(decoded_imgs):
    print(" - ", u)

# Let's inspect the layout structure:
# Search for parent-div and children
pos = html.find('class="parent-div"')
if pos != -1:
    print("\nParent-div HTML snippet:")
    print(html[pos:pos+2500])
