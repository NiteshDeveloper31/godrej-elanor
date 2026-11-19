from PIL import Image

ref2 = Image.open(r"C:/Users/Nikhil/.gemini/antigravity/brain/e83ab009-8a6b-48d4-b405-ee8035b4490e/.user_uploaded/media_1795095536336_5ec03fb4.png")
print("Ref 2 size:", ref2.size)
ref2.crop((0, 0, ref2.width, 140)).save('ref2_header_crop.png')
print("Saved ref2_header_crop.png")
