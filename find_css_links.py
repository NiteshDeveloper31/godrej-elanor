import re

with open('godrej_gallery.html', encoding='utf-8') as f:
    html = f.read()

css_links = re.findall(r'<link[^>]*href=[\"\']([^\"\']+\.css)[\"\'][^>]*>', html)
print("CSS links in gallery page:")
for l in css_links:
    print(" - ", l)
