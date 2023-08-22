from PIL import Image, ImageDraw, ImageFont

TEXT_COLOR = (255, 255, 255)


class TextWatermark:
    def add_text_watermark(self, path, text, watermark_size):
        img = Image.open(path)
        size = img.size

        font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', int(size[0] / watermark_size))
        watermark_pos = (0, int(size[1] / 2))

        drawable_img = ImageDraw.Draw(img)
        drawable_img.text(watermark_pos, (text + ' ') * watermark_size * 2, font=font, fill=TEXT_COLOR)

        return img
