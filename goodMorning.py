from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import PIL.ImageOps

import math
import os

from textureText import newText
from phrase import getAdjective, getSubstantive
from maurilio import calculate_maurilio_size, calculate_maurilio_position



adjective = getAdjective()
substantive = getSubstantive()

newText("texture", "Bom dia, " + adjective, substantive, 20)


img = Image.open("./background.jpg")
maurilio = Image.open("./maurilios/03.png")
text = Image.open("./text.png")

# resize maurilio
size = calculate_maurilio_size(img.size, maurilio.size)
maurilio = maurilio.resize(size, Image.ANTIALIAS)

# place maurilio in the right position
position = calculate_maurilio_position(img.size, maurilio.size)
img.paste(maurilio, position, maurilio)

# place text
text = text.resize((img.size[0] / 2, img.size[1] / 2), Image.ANTIALIAS)
img.paste(text, (20,20), text)


img.save("final.jpg")
