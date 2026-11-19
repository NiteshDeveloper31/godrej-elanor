import subprocess
import json

# Let's run a script in node or python to check the elements bounding box
script = """
const puppeteer = require('puppeteer');
"""
# Since node/puppeteer might not be installed, let's use python with a simple test page or inspect styles.css
print("Let's check styles.css for mobile-header rules")
with open('styles.css') as f:
    text = f.read()

import re
matches = re.findall(r'@media\s*\(max-width:\s*768px\)\s*\{([^}]+(?:\{[^}]+\}[^}]*)*)\}', text)
for idx, m in enumerate(matches):
    print(f"--- Media query {idx+1} ---")
    if 'header' in m.lower() or 'logo' in m.lower():
        print(m)
