#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import PIL.ImageOps
import os


def newText(texture, adjective, substantive, margin = 10):

    cwd = os.getcwd()
    textureImage = Image.open("textures/" + texture + ".jpg")
    maskImage = Image.new('RGBA', textureImage.size, (255, 255, 255, 0))


    font = ImageFont.truetype(cwd + "/fonts/precious/Precious.ttf", 65, encoding="unic")
    draw = ImageDraw.Draw(maskImage)


    draw.text((margin, margin),"Bom dia " + adjective,(0,0,0,255), font=font)
    draw.text((margin, margin+font.getsize("A")[0]), substantive,(0,0,0,255), font=font)

    result = Image.composite(textureImage, maskImage, maskImage)


    invertedMask = PIL.ImageOps.invert(maskImage.convert('RGB'))
    box = invertedMask.getbbox()
    result = result.crop(box)

    result.save("resultado.png")

newText("glitter", "entusiastas", "das telonas", 20)
