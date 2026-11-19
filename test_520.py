import subprocess
import tempfile
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_out = os.path.join(tempfile.gettempdir(), "test_500.png")

cmd = f'"{chrome_path}" --headless=new --window-size=520,844 --screenshot="{temp_out}" http://localhost:8000/'
subprocess.run(cmd, shell=True)

if os.path.exists(temp_out):
    from PIL import Image
    im = Image.open(temp_out)
    im.crop((0, 0, im.width, 100)).save("crop_hdr_520.png")
    print("Saved crop_hdr_520.png, width:", im.width)
