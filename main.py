from PIL import Image, ImageDraw, ImageFont

img_path = 'img/image.jpg'
font_path = '/System/Library/Fonts/Supplemental/Arial.ttf'
watermark_pos = (0, 0)
watermark_text = 'sample text'
color = (255, 255, 255)

font = ImageFont.truetype(font_path, 100)
img = Image.open(img_path)

drawable_img = ImageDraw.Draw(img)
drawable_img.text(watermark_pos, watermark_text, font=font, fill=color)

img.show()