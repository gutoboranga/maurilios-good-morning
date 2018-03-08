#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import PIL.ImageOps

import math
import os

from phrase import getAdjective, getSubstantive
from textureText import newText, calculate_text_size
from maurilio import get_maurilio, calculate_maurilio_size, calculate_maurilio_position
from background import get_background


adjective = unicode(getAdjective(), "utf-8")
substantive = unicode(getSubstantive(), "utf-8")

newText("texture", "Bom dia, " + adjective, substantive, 20)

# load images
img = Image.open(get_background())
maurilio = Image.open(get_maurilio())
text = Image.open("./text.png")


# resize maurilio
size = calculate_maurilio_size(img.size, maurilio.size)
maurilio = maurilio.resize(size, Image.ANTIALIAS)


# place maurilio in the right position
position = calculate_maurilio_position(img.size, maurilio.size)
img.paste(maurilio, position, maurilio)


# place text
text_size = calculate_text_size(img.size, text.size)
text = text.resize(text_size, Image.ANTIALIAS)
img.paste(text, (20,20), text)


# save result
img.save("bom-dia.jpg")
