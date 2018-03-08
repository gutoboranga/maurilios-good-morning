#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import random
from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont


adjectives = ["amantes", "entusiastas", "guerreiros",
                    "apreciadores", "simpatizantes", "devotos",
                    "estudiosos", "adeptos", "aficionados",
                    "adoradores", "apaixonados", "veneradores",
                    "enamorados", "comungantes", "partidários",
                    "seguidores", "fiéis", "idólatras", "tietes"];

substantives = ["da sétima arte", "do audio-visual", "da indústria dramaturga",
                    "das telonas", "do cinema", "da arte em movimento", "das produções multimídia",
                    "da arte televisiva", "do Tony Ramos", "da cinegrafia", "da cinematografia",
                    "do transporte televisivo", "da cinematurgia", "dos spinoffs",
                    "do drama televisivo", "das películas", "dos longa-metragens"];


def getPhrase():

    adjectiveIndex = int(random.uniform(0, len(adjectives)-1));
    substantiveIndex = int(random.uniform(0, len(substantives)-1));

    return adjectives[adjectiveIndex] + " " + substantives[substantiveIndex];

def getAdjective():
    i = int(random.uniform(0, len(adjectives)-1))
    return adjectives[i]
    
def getSubstantive():
    i = int(random.uniform(0, len(substantives)-1))
    return substantives[i]

# def text_with_stroke(draw,width,height,line,font,fillcolor,shadowcolor):
#     draw.text((width-1, height), line, font=font, fill=shadowcolor)
#     draw.text((width+1, height), line, font=font, fill=shadowcolor)
#     draw.text((width, height-1), line, font=font, fill=shadowcolor)
#     draw.text((width, height+1), line, font=font, fill=shadowcolor)
#     draw.text((width, height), line, font=font, fill=fillcolor)
#
# source = Image.open("./input.jpg")
# img = Image.new("RGBA", source.size, (255,255,255,0))
#
# draw = ImageDraw.Draw(img)
# base_width, base_height = img.size
# fillcolor = "white"
# shadowcolor = "black"
# font = "arial"
#
# width, height = font.getsize("testando")
# x = (base_width - width) / 2
# text_with_stroke(draw,x,y,"testando",font,fillcolor,shadowcolor)
# y += height

# print(getPhrase());
