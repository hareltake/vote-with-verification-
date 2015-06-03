from pytesser import *  
from PIL import Image
im = Image.open('crop3.jpg')  
textcode = image_to_string(im)  
print textcode  