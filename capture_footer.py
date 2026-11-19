import os
import subprocess

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cwd = os.path.abspath(".")

mobile_full = os.path.join(cwd, "mobile_all_sections.png")
cmd = [
    chrome_path,
    "--headless=new",
    f"--screenshot={mobile_full}",
    "--window-size=390,9500",
    "--hide-scrollbars",
    "http://localhost:8000/"
]
subprocess.run(cmd, capture_output=True, text=True)

from PIL import Image
im = Image.open(mobile_full)
w, h = im.size
print("Mobile all sections size:", w, h)

# Crop from 5500 to bottom
im.crop((0, 5500, w, h)).save('mobile_slice_footer.png')
print("Saved mobile_slice_footer.png")
