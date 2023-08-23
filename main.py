import tkinter
from tkinter import *
import photo_watermark
import text_watermark
import tui

tui = tui.Tui()
photo_watermark = photo_watermark.PhotoWatermark()
text_watermark = text_watermark.TextWatermark()


def convert_watermark_size():
    size = size_value.get().upper()

    match size:
        case 'S':
            return 24
        case 'M':
            return 20
        case 'L':
            return 14
        case 'XL':
            return 10

def watermark():
    if type_value.get().upper() == 'TEXT':
        text_watermark.add_text_watermark(input_image_path.get(),
                                                 input_content.get(),
                                                 convert_watermark_size()).show()
    elif type_value.get().upper() == 'IMAGE':
        photo_watermark.add_photo_watermark(tui.get_image_path(),
                                                   tui.get_watermark_image(),
                                                   convert_watermark_size()).show()
    else:
        print('Incorrect type')


# window config
window = Tk()
window.title('Watermark App')
window.columnconfigure(1, minsize=60)
window.columnconfigure(3, minsize=90)

# labels
lbl_image_path = Label(text='Path', width=20)
lbl_image_path.grid(row=0, column=0)

lbl_size = Label(text='Watermark size: ', width=20)
lbl_size.grid(row=1, column=0)

lbl_type = Label(text='Watermark type: ', width=20)
lbl_type.grid(row=1, column=2)

lbl_content = Label(text='Watermark path/text', width=20)
lbl_content.grid(row=3, column=0)

# buttons
btn_add_watermark = Button(text='Add Watermark', command=watermark, width=40, borderwidth=0, pady=0, padx=0)
btn_add_watermark.grid(row=4, column=0, columnspan=4)

# menus
size_options = ['S', 'M', 'L', 'XL']
size_value = tkinter.StringVar(window)
menu_size = OptionMenu(window, size_value, *size_options)
menu_size.grid(row=1, column=1, sticky="ew")

type_options = ['Text', 'Image']
type_value = tkinter.StringVar(window)
menu_type = OptionMenu(window, type_value, *type_options)
menu_type.grid(row=1, column=3, sticky="ew")

# inputs
input_image_path = Entry(width=40)
input_image_path.grid(columnspan=3, row=0, column=1)

input_content = Entry(width=40)
input_content.grid(columnspan=3, row=2, column=1)

window.mainloop()

