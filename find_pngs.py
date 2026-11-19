import os

for f in os.listdir('.'):
    if f.endswith('.png'):
        print(f, os.path.getsize(f))
