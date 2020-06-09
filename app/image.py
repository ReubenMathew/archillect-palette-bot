import colorgram
from PIL import Image, ImageDraw, ImageEnhance
import requests
from io import BytesIO

class Palette:

    def __init__(self,url):
        self.url = url
        response = requests.get(self.url)
        img = Image.open(BytesIO(response.content))

        img = ImageEnhance.Color(img) 
        img = img.enhance(2.8)

        img = img.quantize(colors=16, method=0)
        img.save(f'reducedImage.png')

        self.colors = colorgram.extract(img, 4)
        self.colors.sort(key=lambda c: c.hsl.h)

    def getImages(self):
        imgList = []
        counter = 0
        for color in self.colors:
            counter += 1
            rgb = color.rgb
            img = Image.new('RGB', (1024,1024), rgb)
            imgList.append(img)
        # print(imgList)
        return imgList

    
    def getRGB(self):
        rgbList = []
        counter = 0
        for color in self.colors:
            counter += 1
            rgb = color.rgb
            rgbList.append(rgb)

        out = "RGB Codes:\n"
        for rgb in rgbList:
            out += f'({rgb.r},{rgb.g},{rgb.b})\n'
        return out

