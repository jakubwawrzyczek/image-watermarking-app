import tkinter
from tkinter import messagebox

from PIL import Image, ImageDraw, ImageFont


class TextWatermark:
    def add_text_watermark(self, path, text, size_option, color, border):

        try:
            img = Image.open(path)
        except AttributeError:
            tkinter.messagebox.showerror(title='Error!', message='Browse for file path!')
            return None

        img_size = img.size

        font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', int(img_size[0] / size_option))
        watermark_pos = (0, int(img_size[1] / 2))

        drawable_img = ImageDraw.Draw(img)

        if color == 'Black':
            text_color = 'black'
            shadow_color = 'white'
        else:
            text_color = 'white'
            shadow_color = 'black'

        # Border thickness
        if border == 'Thick':
            drawable_img.text((watermark_pos[0] - 1, watermark_pos[1] - 1), (text + ' ') * size_option * 2, font=font,
                              fill=shadow_color)
            drawable_img.text((watermark_pos[0] + 1, watermark_pos[1] - 1), (text + ' ') * size_option * 2, font=font,
                              fill=shadow_color)
            drawable_img.text((watermark_pos[0] - 1, watermark_pos[1] + 1), (text + ' ') * size_option * 2, font=font,
                              fill=shadow_color)
            drawable_img.text((watermark_pos[0] + 1, watermark_pos[1] + 1), (text + ' ') * size_option * 2, font=font,
                              fill=shadow_color)
        else:
            drawable_img.text((watermark_pos[0] - 1, watermark_pos[1]), (text + ' ') * size_option * 2, font=font,
                              fill=shadow_color)
            drawable_img.text((watermark_pos[0] + 1, watermark_pos[1]), (text + ' ') * size_option * 2, font=font,
                              fill=shadow_color)
            drawable_img.text((watermark_pos[0], watermark_pos[1] - 1), (text + ' ') * size_option * 2, font=font,
                              fill=shadow_color)
            drawable_img.text((watermark_pos[0], watermark_pos[1] + 1), (text + ' ') * size_option * 2, font=font,
                              fill=shadow_color)

        # Adding text
        drawable_img.text(watermark_pos, (text + ' ') * size_option * 2, font=font, fill=text_color)

        return img
