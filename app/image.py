import colorgram
from PIL import Image, ImageDraw, ImageEnhance
import requests
from io import BytesIO

class Palette:

    def __init__(self,url):
        self.url = url

    def process(self):

        response = requests.get(self.url)
        img = Image.open(BytesIO(response.content))

        img = ImageEnhance.Color(img) 
        img = img.enhance(2.8)

        img = img.quantize(colors=16, method=0)
        img.save(f'reducedImage.png')

        colors = colorgram.extract(img, 4)
        colors.sort(key=lambda c: c.hsl.h)

        print(colors)

        imgList = []
        counter = 0
        for color in colors:
            counter += 1
            rgb = color.rgb
            img = Image.new('RGB', (1024,1024), rgb)
            imgList.append(img)
        return imgList

