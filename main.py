import photo_watermark
import text_watermark
import tui

tui = tui.Tui()
photo_watermark = photo_watermark.PhotoWatermark()
text_watermark = text_watermark.TextWatermark()


def watermark():
    watermark_type = tui.get_watermark_type()

    if watermark_type == 'TEXT':
        return text_watermark.add_text_watermark(tui.get_image_path(),
                                                 tui.get_watermark_text(),
                                                 tui.get_watermark_size())
    elif watermark_type == 'IMAGE':
        return photo_watermark.add_photo_watermark(tui.get_image_path(),
                                                   tui.get_watermark_image(),
                                                   tui.get_watermark_size())
    else:
        print('Incorrect type')


img = watermark()
img.show()
