import re

with open('godrej_fcbe.css', encoding='utf-8') as f:
    css = f.read()

# Let's search for price table classes
prices = re.findall(r'(\.[a-zA-Z0-9_-]*price[^{]*\{[^}]*\})', css, re.IGNORECASE)
print(f"Price classes: {len(prices)}")
for p in prices[:8]:
    print(" - ", p)

# Search for emi calculator classes
emis = re.findall(r'(\.[a-zA-Z0-9_-]*emi[^{]*\{[^}]*\})', css, re.IGNORECASE)
print(f"\nEMI classes: {len(emis)}")
for e in emis[:8]:
    print(" - ", e)
