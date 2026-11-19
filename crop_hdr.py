from PIL import Image

im_mob = Image.open('verified_mobile.png')
im_mob.crop((0, 0, im_mob.width, 100)).save('crop_hdr_mob.png')

im_dsk = Image.open('verified_desktop.png')
im_dsk.crop((0, 0, im_dsk.width, 100)).save('crop_hdr_dsk.png')

print("Cropped headers saved!")
