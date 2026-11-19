import re

with open('godrej_gallery.html', encoding='utf-8') as f:
    html = f.read()

# Let's search for inline styles or style tags
styles = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
print(f"Total style tags: {len(styles)}")
for s in styles:
    if 'parent-div' in s or 'gallery' in s or 'children-dev' in s:
        print("Found matching style block:")
        for line in s.split('\n'):
            if any(k in line for k in ['parent-div', 'children-dev', 'div-1', 'grid', 'column']):
                print("  ", line.strip())
