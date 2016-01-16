from PIL import Image, ImageEnhance
import random
import os

_greyscale = [' ',
              '`',
              '.\'',
              '-',
              '^,',
              '\/:"',
              '~!_<>',
              ';',
              '=',
              'i',
              'j',
              'l17{}',
              'tv[]',
              'crI',
              'fuJ2',
              'oxLO3%',
              '*',
              'V',
              'Y4569',
              'ehNTZ0&',
              'bdkwAFP',
              'DX8$',
              'pqGU',
              'gKQS',
              'BE',
              'mRW#',
              'H',
              'M@'][::-1]

def _proportion(min1, max1, min2, max2, val):
    diff1 = max1-min1
    diff2 = max2-min2
    val = float(val)
    return ((val-min1)/diff1)*diff2 + min2


def get_ascii_art(imagePath, scale):
    if not isinstance(imagePath, str) or not os.path.isfile(imagePath):
         raise ValueError("Image path must be valid file path")
    if not isinstance(scale, int) or scale < 0 or scale > 100:
         raise ValueError("Scale must be an integer value between 0 and 100")

    #Open the image file
    image = Image.open(imagePath)
    #Convert to greyscale
    image = image.convert("L")
    #Scale the image
    image = image.resize((int(image.width*scale/100 * 1.5), int(image.height*scale/100)))
    #Object to enhance contrast
    contrast = ImageEnhance.Contrast(image)
    #Enhance contrast
    image = contrast.enhance(2)

    #The resulting ASCII Art
    out = ""
    #Horizontal position of the current pixel
    pos = 0
    #Cycle through all pixel values
    pixels = list(image.getdata())
    #pixels = [x[2] for x in pixels]
    for x in pixels:
        #Add the correct character to the output string
        out += random.choice(_greyscale[int(_proportion(0, 255, 0, len(_greyscale) - 1, x))])
        pos += 1
        if pos >= image.width:
            out += "\n"
            pos = 0

    return out


if __name__ == "__main__":
    with open("output.txt", "w") as f:
        f.write(get_ascii_art("image.png", 50))
    print("ASCII Art succesfully created")
