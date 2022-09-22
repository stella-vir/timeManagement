# Optical character recognition
# brew install pytesseract
# brew list tesseract

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd ='/usr/local/Cellar/tesseract/5.2.0/bin/tesseract'
img_file = 'schedule.jpg'


img = Image.open(img_file)

orc_res = pytesseract.image_to_string(img)

print(orc_res[:-1])
