from PIL import Image, ImageDraw, ImageFont
import textwrap
 
def create_logpost(text): # create Image object with the input image
    image = Image.open('logpostingtemplate.png') 
    draw = ImageDraw.Draw(image)
    font_size = max(15, round(45/(len(text)/10)))
    font = ImageFont.truetype('Roboto-Bold.ttf', size=font_size, encoding="unic")
    margin = offset = max(40, 100-len(text))
    color = 'rgb(0, 0, 0)' # black color
    for line in textwrap.wrap(text, width=font_size*3):
        draw.text((margin, offset), line, fill=color, font=font)
        offset += font.getsize(line)[1]
    image.save('newlogpost.png')
