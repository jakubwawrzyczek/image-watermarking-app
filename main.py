from PIL import Image, ImageDraw, ImageFont

FONT_PATH = '/System/Library/Fonts/Supplemental/Arial.ttf'
TEXT_COLOR = (255, 255, 255)


def choose_text_size():
    size = input('Select text size: ')

    match size:
        case 'S':
            return 24
        case 'M':
            return 20
        case 'L':
            return 14
        case 'XL':
            return 10


def add_text_watermark(path, text):
    img = Image.open(path)
    size = img.size
    text_size = choose_text_size()

    font = ImageFont.truetype(FONT_PATH, int(size[0] / text_size))
    watermark_pos = (0, int(size[1] / 2))

    drawable_img = ImageDraw.Draw(img)
    drawable_img.text(watermark_pos, (watermark_text + ' ') * text_size * 2, font=font, fill=TEXT_COLOR)

    return img


img_path = input('Path to image: ')
watermark_text = input('Watermark text: ')

img = add_text_watermark(img_path, watermark_text)
img.show()
