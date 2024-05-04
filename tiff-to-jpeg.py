import sys
import os
from PIL import Image
import re


print("\n TIFF to JPG Conversion \n")
print("\n Developed by A Rajasekaran\n")
print("\n Date: 22 April 2022 \n\n")

# pillow library used

directory = "JPEG"

output = os.getcwd() + "\\" + directory

if os.path.exists(output):
    pass
else:
    os.mkdir(output)


for fname in os.listdir():
    if not fname.endswith(".tif"):
        continue
    print(fname)
    test = os.path.splitext(fname)[0]

    # open the tif image
    image = Image.open(fname)

    # define jpg file name as same tif image name
    name1 = test + ".jpg"
    name2 = output + "\\" + name1

    # get the tif image resolution value
    img_dpi = str(image.info['dpi'])
    patn = re.sub(r"[\(\)]", "", img_dpi)
    sp = patn.split(",")[0]
    dpi_val = round(float(sp))  

    # convert to jpeg image, resolution value assigned from tiff image
    image.save(name2, 'jpeg', dpi=(dpi_val,dpi_val), quality=90)
    
print(" \n\nJPG Conversion Completed\n\n")