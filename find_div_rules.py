import re

with open('godrej_fcbe.css', encoding='utf-8') as f:
    css = f.read()

div_rules = re.findall(r'(\.div-\d+\s*\{[^}]+\})', css)
print("Div rules found:")
for r in div_rules:
    print(" - ", r)
