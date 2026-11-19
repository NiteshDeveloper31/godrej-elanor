import subprocess
import tempfile
import os
import shutil

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_dir = tempfile.gettempdir()
temp_mobile = os.path.join(temp_dir, "test_mob_ua.png")

# Use mobile UA and touch emulation
cmd = [
    chrome_path,
    "--headless=new",
    '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    "--window-size=390,844",
    f"--screenshot={temp_mobile}",
    "http://localhost:8000/"
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Mobile UA exit:", res.returncode)
if os.path.exists(temp_mobile):
    shutil.copy(temp_mobile, "verified_mobile_ua.png")
    print("Saved verified_mobile_ua.png, size:", os.path.getsize(temp_mobile))

    # Also crop header
    from PIL import Image
    im = Image.open(temp_mobile)
    print("Actual image dimensions:", im.size)
    im.crop((0, 0, im.width, 100)).save("crop_hdr_ua.png")
    print("Saved crop_hdr_ua.png")
