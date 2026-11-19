import urllib.request
import os

headers = {'User-Agent': 'Mozilla/5.0'}

desktop_url = "https://gplwebsitecdnblob.blob.core.windows.net/godrej-cdn/Images/overview-banner-1920x900-cmwkgd3og0003mcph3t6f2ggh.webp"
mobile_url = "https://gplwebsitecdnblob.blob.core.windows.net/godrej-cdn/Images/overview-banner-720x1600-cmwkgdj7m0004mcph87goggp9.webp"

os.makedirs('assets/images/godrej-cdn', exist_ok=True)

print("Downloading desktop banner...")
req = urllib.request.Request(desktop_url, headers=headers)
with urllib.request.urlopen(req) as resp, open('assets/images/godrej-cdn/banner-desktop-1920x900.webp', 'wb') as f:
    f.write(resp.read())

print("Downloading mobile banner...")
req = urllib.request.Request(mobile_url, headers=headers)
with urllib.request.urlopen(req) as resp, open('assets/images/godrej-cdn/banner-mobile-720x1600.webp', 'wb') as f:
    f.write(resp.read())

print("Desktop banner size:", os.path.getsize('assets/images/godrej-cdn/banner-desktop-1920x900.webp'))
print("Mobile banner size:", os.path.getsize('assets/images/godrej-cdn/banner-mobile-720x1600.webp'))
