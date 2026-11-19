import os

for root, dirs, files in os.walk('assets'):
    for f in files:
        if f.lower().endswith(('.webp', '.jpg', '.jpeg', '.png', '.svg')):
            print(os.path.join(root, f).replace('\\', '/'))
