import urllib.request
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

logos = [
    ("https://www.godrejproperties.com/images/revamp/godrej_properties_logo.svg", "assets/images/godrej_properties_logo.svg"),
    ("https://www.godrejproperties.com/images/revamp/godrejsignature.svg", "assets/images/godrejsignature.svg")
]

os.makedirs('assets/images', exist_ok=True)

for url, dest in logos:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(dest, 'wb') as f:
            f.write(resp.read())
        print(f"Downloaded {dest}: {os.path.getsize(dest)} bytes")
    except Exception as e:
        print(f"Failed {url}: {e}")
