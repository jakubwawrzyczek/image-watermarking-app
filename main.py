import tkinter
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os
import photo_watermark
import text_watermark
import tui

tui = tui.Tui()
photo_watermark = photo_watermark.PhotoWatermark()
text_watermark = text_watermark.TextWatermark()

image_path = ''
watermark_path = ''


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


def open_image_file():
    global image_path
    file = filedialog.askopenfile(mode='r', filetypes=[('Png Files', '*.png'),
                                                       ('Jpg Files', '*.jpg')])
    if file:
        image_path = os.path.abspath(file.name)


def open_watermark_file():
    global watermark_path
    file = filedialog.askopenfile(mode='r', filetypes=[('Png Files', '*.png'),
                                                       ('Jpg Files', '*.jpg')])
    if file:
        watermark_path = os.path.abspath(file.name)


def toggle(value):
    if value == 'Image':
        input_text.grid_forget()
        btn_browse_watermark_path.grid(row=3, column=1)
        lbl_content.config(text='Watermark path')
        lbl_content.grid(row=3, column=0)
    elif value == 'Text':
        btn_browse_watermark_path.grid_forget()
        input_text.grid(row=3, column=1)
        lbl_content.config(text='Watermark text')
        lbl_content.grid(row=3, column=0)


def watermark():
    if type_value.get() == 'Text':
        text_watermark.add_text_watermark(image_path,
                                          input_text.get(),
                                          convert_watermark_size()).show()
    elif type_value.get() == 'Image':
        photo_watermark.add_photo_watermark(image_path,
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
lbl_type.grid(row=2, column=0)

lbl_content = Label(text='', width=20)

# buttons
btn_add_watermark = Button(text='Add Watermark', command=watermark, width=40, borderwidth=0, pady=0, padx=0)
btn_add_watermark.grid(row=4, column=0, columnspan=4)

btn_browse_image_path = Button(text='Browse', command=open_image_file)
btn_browse_image_path.grid(row=0, column=1)

btn_browse_watermark_path = Button(text='Browse', command=open_image_file)

# menus
size_options = ['S', 'M', 'L', 'XL']
size_value = tkinter.StringVar(window)
menu_size = OptionMenu(window, size_value, *size_options)
menu_size.grid(row=1, column=1, sticky="ew")

type_options = ['Text', 'Image']
type_value = tkinter.StringVar(window)
menu_type = OptionMenu(window, type_value, *type_options, command=toggle)
menu_type.grid(row=2, column=1, sticky="ew")

# inputs
input_text = Entry(width=10)

window.mainloop()
