from PIL import Image

ref_im = Image.open(r"C:/Users/Nikhil/.gemini/antigravity/brain/e83ab009-8a6b-48d4-b405-ee8035b4490e/.user_uploaded/media_1795093841503_d35198e2.png")
print("Ref image size:", ref_im.size)
ref_im.crop((0, 0, ref_im.width, 120)).save('ref_header_crop.png')
print("Saved ref_header_crop.png")
