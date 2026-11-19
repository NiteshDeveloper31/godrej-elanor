import re

with open('godrej_gallery.html', encoding='utf-8') as f:
    html = f.read()

# Let's find classes or tags in gallery
m = re.findall(r'<div[^>]*class=[\"\']([^\"\']*gallery[^\"\']*)[\"\'][^>]*>', html, re.IGNORECASE)
print("Gallery classes in HTML:")
for c in set(m):
    print(" - ", c)

# Let's find tabs or categories in gallery
tabs = re.findall(r'<button[^>]*>(.*?)</button>', html)
print("\nButtons / Tabs in gallery page:")
for t in tabs[:20]:
    clean = re.sub(r'<[^>]+>', '', t).strip()
    if clean:
        print(" - ", clean)
