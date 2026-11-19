from PIL import Image

try:
    im = Image.open('assets/images/godrej-cdn/hero-banner-main.webp')
    print("hero-banner-main.webp size:", im.size)
except Exception as e:
    print("Error:", e)
