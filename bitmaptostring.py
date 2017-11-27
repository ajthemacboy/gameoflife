import numpy, pathlib, sys
from PIL import Image

path = pathlib.Path(sys.argv[1])

img = Image.open(path)
img_array = numpy.array(img)

img_str = ''.join(str(int(x / 255)) for x in img_array.flatten().tolist())

print(hex(int(img_str)))