from PIL import Image, ImageDraw, ImageFont

TEXT_COLOR = 'white'
SHADOW_COLOR = 'black'


class TextWatermark:
    def add_text_watermark(self, path, text, size_option):
        img = Image.open(path)
        img_size = img.size

        font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', int(img_size[0] / size_option))
        watermark_pos = (0, int(img_size[1] / 2))

        drawable_img = ImageDraw.Draw(img)

        # light border
        # drawable_img.text((watermark_pos[0] - 1, watermark_pos[1]), (text + ' ') * size_option * 2, font=font,
        #                   fill=SHADOW_COLOR)
        # drawable_img.text((watermark_pos[0] + 1, watermark_pos[1]), (text + ' ') * size_option * 2, font=font,
        #                   fill=SHADOW_COLOR)
        # drawable_img.text((watermark_pos[0], watermark_pos[1] - 1), (text + ' ') * size_option * 2, font=font,
        #                   fill=SHADOW_COLOR)
        # drawable_img.text((watermark_pos[0], watermark_pos[1] + 1), (text + ' ') * size_option * 2, font=font,
        #                   fill=SHADOW_COLOR)

        # thick border
        drawable_img.text((watermark_pos[0] - 1, watermark_pos[1]-1), (text + ' ') * size_option * 2, font=font,
                          fill=SHADOW_COLOR)
        drawable_img.text((watermark_pos[0] + 1, watermark_pos[1]-1), (text + ' ') * size_option * 2, font=font,
                          fill=SHADOW_COLOR)
        drawable_img.text((watermark_pos[0]-1, watermark_pos[1]+1), (text + ' ') * size_option * 2, font=font,
                          fill=SHADOW_COLOR)
        drawable_img.text((watermark_pos[0]+1, watermark_pos[1]+1), (text + ' ') * size_option * 2, font=font,
                          fill=SHADOW_COLOR)

        # text
        drawable_img.text(watermark_pos, (text + ' ') * size_option * 2, font=font, fill=TEXT_COLOR)


        return img
