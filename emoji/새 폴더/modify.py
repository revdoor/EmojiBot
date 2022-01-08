import os
import glob
from PIL import Image

files = glob.glob('./*')

for f in files:
    title, ext = os.path.splitext(f)
    if ext in ['.jpg', '.png']:
        img = Image.open(f)
        print(img.width, img.height)
        img_transpose = img.transpose(Image.FLIP_LEFT_RIGHT)
        img_transpose.save(title + '_transpose' + ext)
