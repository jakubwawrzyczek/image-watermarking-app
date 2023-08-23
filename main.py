from tkinter import *
import photo_watermark
import text_watermark
import tui

tui = tui.Tui()
photo_watermark = photo_watermark.PhotoWatermark()
text_watermark = text_watermark.TextWatermark()

def watermark():
    watermark_type = tui.get_watermark_type()

    if watermark_type == 'TEXT':
        text_watermark.add_text_watermark(tui.get_image_path(),
                                                 tui.get_watermark_text(),
                                                 tui.get_watermark_size()).show()
    elif watermark_type == 'IMAGE':
        photo_watermark.add_photo_watermark(tui.get_image_path(),
                                                   tui.get_watermark_image(),
                                                   tui.get_watermark_size()).show()
    else:
        print('Incorrect type')


# window config
window = Tk()
window.title('Watermark App')

# buttons
btn_add_watermark = Button(text='Add Watermark', command=watermark)
btn_add_watermark.grid(row=0, column=0)

window.mainloop()

