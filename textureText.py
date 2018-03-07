#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import PIL.ImageOps

import math
import os

def make_borders(text1, text2, margin, font, size):
    # DRAW BORDERS
    img = Image.new("RGBA", size, (255,255,255,0))
    draw = ImageDraw.Draw(img)
    
    borders = [
        {'size': int(math.floor(font.size/10)), 'opacity': 25},
        {'size': int(math.floor(font.size/20)), 'opacity': 50},
        {'size': int(math.floor(font.size/30)), 'opacity': 100},
        {'size': int(math.floor(font.size/40)), 'opacity': 170}
    ]

    for border in borders:
        size = border['size']
        opacity = border['opacity']
    
        # TEXT 1
        draw.text((margin - size, margin - size), text1, (255,255,255,opacity), font=font)
        draw.text((margin + size, margin - size), text1, (255,255,255,opacity), font=font)
        draw.text((margin - size, margin + size), text1, (255,255,255,opacity), font=font)
        draw.text((margin + size, margin + size), text1, (255,255,255,opacity), font=font)
        
        # TEXT 2 (refatorar depois essa repetição toda de código)
        draw.text((margin - size, margin + font.getsize("A")[0] - size), text2, (255,255,255,opacity), font=font)
        draw.text((margin + size, margin + font.getsize("A")[0] - size), text2, (255,255,255,opacity), font=font)
        draw.text((margin - size, margin + font.getsize("A")[0] + size), text2, (255,255,255,opacity), font=font)
        draw.text((margin + size, margin + font.getsize("A")[0] + size), text2, (255,255,255,opacity), font=font)
        
    img.save("borders.png")
    return img


def newText(texture, text1, text2, margin = 10):

    cwd = os.getcwd()
    textureImage = Image.open("textures/" + texture + ".jpg")
    maskImage = Image.new('RGBA', textureImage.size, (255, 255, 255, 0))

    font = ImageFont.truetype(cwd + "/fonts/precious/Precious.ttf", 50, encoding="unic")
    draw = ImageDraw.Draw(maskImage)
    
    # BORDERS
    borders_image = make_borders(text1, text2, margin=margin, font=font, size=textureImage.size)

    # MAIN TEXT
    draw.text((margin, margin), text1, (0,0,0,255), font=font)
    draw.text((margin, margin+font.getsize("A")[0]), text2,(0,0,0,255), font=font)

    # BLEND BORDERS AND MAIN TEXT
    texturized = Image.composite(textureImage, maskImage, maskImage)
    borders_image.paste(texturized, (0, 0), texturized)
    
    # CROP IMAGE
    invertedMask = PIL.ImageOps.invert(maskImage.convert('RGB'))
    box = invertedMask.getbbox()
    
    # add extra space to avoid cropping borders
    extra_space = int(math.floor(font.size/10))
    box = (0, 0, box[2] + extra_space, box[3] + extra_space)
    
    # SAVE
    result = borders_image.crop(box)
    result.save("text.png")
    

# newText("texture", "Bom dia, amantes", "do Palestrinha", 20)
