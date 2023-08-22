from PIL import Image, ImageDraw, ImageFont

TEXT_COLOR = (255, 255, 255)


class TextWatermark:
    def add_text_watermark(self, path, text, size_option):
        img = Image.open(path)
        img_size = img.size

        font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', int(img_size[0] / size_option))
        watermark_pos = (0, int(img_size[1] / 2))

        drawable_img = ImageDraw.Draw(img)
        drawable_img.text(watermark_pos, (text + ' ') * size_option * 2, font=font, fill=TEXT_COLOR)

        return img
