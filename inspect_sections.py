import re

with open('godrej_godrej-elanor.html', encoding='utf-8') as f:
    html = f.read()

# Let's find sections or nav elements
sections = re.findall(r'<section[^>]*id=[\"\']([^\"\']+)[\"\'][^>]*>', html)
print("Sections with IDs:", sections)

# Also find headings
headings = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', html, re.DOTALL)
print("\nHeadings found:")
for h in headings[:25]:
    clean = re.sub(r'<[^>]+>', '', h).strip()
    if clean:
        print(" - ", clean)
