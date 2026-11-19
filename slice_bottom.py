from PIL import Image

im = Image.open('mobile_full_page.png')
w, h = im.size
print("Size:", w, h)

# Let's crop 4000 to 6500
im.crop((0, 4200, w, h)).save('mobile_slice_bottom.png')
print("Saved mobile_slice_bottom.png")
