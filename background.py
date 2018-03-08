from os import listdir
from random import uniform


urls = [
    "http://s1.bwallpapers.com/thumbs2/2014/01/27/beautiful-spring-desktop-wallpaper_123205919.jpg",
    "http://s966.info/library/f/flowers-background/flowers-background-17.jpg",
    "https://wallpaper.wiki/wp-content/uploads/2017/04/wallpaper.wiki-Wallpaper-Flowers-Background-Widescreen-PIC-WPB003038.jpg",
    "https://wallpapertag.com/wallpaper/middle/9/2/4/615861-purple-flowers-background-2560x1600-for-hd.jpg",
    "http://s966.info/library/f/flowers-background/flowers-background-14.jpg"
]


def get_background():
    folder_path = "./backgrounds"

    backgrounds = listdir(folder_path)
    index = int(uniform(0, len(backgrounds)-1));

    return folder_path + "/" + backgrounds[index]
    
