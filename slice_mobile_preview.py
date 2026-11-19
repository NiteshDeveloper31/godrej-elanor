from PIL import Image

im = Image.open('mobile_full_page.png')
w, h = im.size
print(f"Original dimensions: {w} x {h}")

# Slices:
# Slice 1: 0 - 1500 (Header, Hero, Breadcrumb, Overview)
# Slice 2: 1500 - 3000 (Neighbourhood, Price, EMI calc)
# Slice 3: 3000 - 4500 (Gallery, Floor plans, Amenities)
# Slice 4: 4500 - end (RERA, Get In Touch, Footer)

im.crop((0, 0, w, min(h, 1500))).save('mobile_slice_1.png')
im.crop((0, 1500, w, min(h, 3000))).save('mobile_slice_2.png')
im.crop((0, 3000, w, min(h, 4500))).save('mobile_slice_3.png')
im.crop((0, 4500, w, h)).save('mobile_slice_4.png')

print("Saved slices 1 to 4 successfully!")
