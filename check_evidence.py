import os

folder = r"C:/Users/Nikhil/.gemini/antigravity/brain/e83ab009-8a6b-48d4-b405-ee8035b4490e/browser_evidence/ec7070aa-1d7f-4f71-9bd7-af77422953ee"
if os.path.exists(folder):
    files = os.listdir(folder)
    print("Files in subagent evidence folder:", len(files))
    for f in sorted(files):
        print(f, os.path.getsize(os.path.join(folder, f)))
else:
    print("Folder does not exist")
