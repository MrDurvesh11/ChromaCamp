from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageEnhance, ImageFilter,Image
from tkinter import filedialog
import os
from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)


# Displaying Image
def displayimage(img):
    dispimage = ImageTk.PhotoImage(img)
    panel.configure(image=dispimage)
    panel.image = dispimage


# Brightness Slider
def brightness_callback(brightness_pos):
    brightness_pos = float(brightness_pos)
    # print(brightness_pos)
    global outputImage
    enhancer = ImageEnhance.Brightness(img)
    outputImage = enhancer.enhance(brightness_pos)
    displayimage(outputImage)


# Contrast Slider
def contrast_callback(contrast_pos):
    contrast_pos = float(contrast_pos)
    # print(contrast_pos)
    global outputImage
    enhancer = ImageEnhance.Contrast(img)
    outputImage = enhancer.enhance(contrast_pos)
    displayimage(outputImage)


# Sharpness Slider
def sharpen_callback(sharpness_pos):
    sharpness_pos = float(sharpness_pos)
    # print(sharpness_pos)
    global outputImage
    enhancer = ImageEnhance.Sharpness(img)
    outputImage = enhancer.enhance(sharpness_pos)
    displayimage(outputImage)

# Color slider


def color_callback(Color_pos):
    Color_pos = float(Color_pos)
    # print(Color_pos)
    global outputImage
    enhancer = ImageEnhance.Color(img)
    outputImage = enhancer.enhance(Color_pos)
    displayimage(outputImage)


# Rotate
def rotate():
    global img
    img = img.rotate(90)
    displayimage(img)


# Flip image
def flip():
    global img
    img = img.transpose((Image.FLIP_LEFT_RIGHT))
    displayimage(img)


# Blur effect on images
def blurr():
    global img
    img = img.filter(ImageFilter.BLUR)
    displayimage(img)


# Emboss effect on images
def emboss():
    global img
    img = img.filter(ImageFilter.EMBOSS)
    displayimage(img)

# Edge enhance effect on images


def edgeEnhance():
    global img
    img = img.filter(ImageFilter.FIND_EDGES)
    displayimage(img)

# Resize image


def resize():
    global img
    img = img.resize((200, 300))
    displayimage(img)


# Crop images within specific window
def crop():
    global img
    img = img.crop((100, 100, 400, 400))
    displayimage(img)

# Reset Function


def reset():
    img = Image.open(imgname)
    width,height=img.size
    if(width>1200 or height>600):
        img = img.resize((1200, 600))
    else:
        img = img.resize((width, height))
    displayimage(img)


def smooth1():
    global img
    img = img.filter(SMOOTH)
    displayimage(img)

# Open images from file explorer


def ChangeImg():
    global img
    global imgname
    imgname = filedialog.askopenfilename(title="Upload Image")
    if imgname:
        img = Image.open(imgname)
        width,height=img.size
        if(width>1200 or height>600):
            img = img.resize((1200, 600))
        else:
            img = img.resize((width, height))
        displayimage(img)


# Save edited images
def save():
    global img
    savefile = filedialog.asksaveasfile(defaultextension=".jpg")
    outputImage.save(savefile)


def close():
    mains.destroy()


# Creating Window
mains = Tk()
space = (" ")*215
screen_width = mains.winfo_screenwidth()
screen_height = mains.winfo_screenheight()

# mains.geometry("1000x700")
mains.geometry(f"{screen_width}x{screen_height}")
mains.title(f"{space}ChromaCamp")
mains.wm_iconbitmap("icon.ico")
mains.configure(bg='GREY')

# Default image in editor
img = Image.open("GreenHills.jpg")
img = img.resize((1200, 600))

# Creating panel to display image
panel = Label(mains)
panel.grid(row=0, column=0, rowspan=12, padx=50, pady=50)
displayimage(img)


# Necessary editing buttons and sliders

# Brightness Slider button
brightnessSlider = Scale(mains, label="Brightness", from_=0, to=2, orient=HORIZONTAL, length=200,
                         resolution=0.1, command=brightness_callback, bg="PINK")
brightnessSlider.set(1)
brightnessSlider.configure(font=('consolas', 10, 'bold'), foreground='black')
brightnessSlider.place(x=1300, y=125)
# brightnessSlider.grid(row=0, column=3)
# brightnessSlider.pack()

# Contrast Slider button
contrastSlider = Scale(mains, label="Contrast", from_=0, to=2, orient=HORIZONTAL, length=200,
                       command=contrast_callback, resolution=0.1, bg="light green")
contrastSlider.set(1)
contrastSlider.configure(font=('consolas', 10, 'bold'), foreground='black')
contrastSlider.place(x=1300, y=210)
# contrastSlider.grid(row=1, column=3)

# <------Sharpness Slider button------>
sharpnessSlider = Scale(mains, label="Sharpness", from_=0, to=2, orient=HORIZONTAL, length=200,
                        command=sharpen_callback, resolution=0.1, bg="light blue")
sharpnessSlider.set(1)
sharpnessSlider.configure(font=('consolas', 10, 'bold'), foreground='black')
sharpnessSlider.place(x=1300, y=295)
# sharpnessSlider.grid(row=2, column=3)

# <------Color Slider button------>
colorSlider = Scale(mains, label="Colors", from_=0, to=2, orient=HORIZONTAL, length=200,
                    command=color_callback, resolution=0.1, bg="YELLOW", font=('consolas', 10, 'bold'), foreground='black')
colorSlider.set(1)

colorSlider.place(x=1300, y=380)
# colorSlider.grid(row=3, column=3)


# <------Rotate button------>
btnRotate = Button(mains, text='Rotate', width=20,height=2 ,command=rotate,
                   bg="GREEN", font=('consolas', 10, 'bold'), foreground='white')

btnRotate.place(x=1035, y=700)
# btnRotate.grid(row=1, column=1)

# <------Reset all button------

reset_button = Button(mains, text="Reset", command=reset,
                      bg="BLACK", activebackground="ORANGE")
reset_button.configure(font=('consolas', 15, 'bold'), foreground='white')
reset_button.place(x=1320, y=50)

# <------Change image button------>
btnChaImg = Button(mains, text='Upload Image', width=20,height=2,
                   command=ChangeImg, bg="RED", activebackground="ORANGE")
btnChaImg.configure(font=("consolas", 10, 'bold'), foreground='white')
btnChaImg.place(x=45, y=700)
# btnChaImg.grid(row=0, column=1)

# <------Flip button------>
btnFlip = Button(mains, text='Flip', width=20,height=2, command=flip, bg="BLUE")
btnFlip.configure(font=('consolas', 10, 'bold'), foreground='white')
btnFlip.place(x=210, y=700)
# btnFlip.grid(row=2, column=1)

# <------Resize button------>
btnResize = Button(mains, text='Resize', width=20,height=2, command=resize, bg="YELLOW")
btnResize.configure(font=('consolas', 10, 'bold'), foreground='black')
btnResize.place(x=375, y=700)
# btnResize.grid(row=3, column=1)

# <------Crop button------>
btnCrop = Button(mains, text='Crop', width=20,height=2, command=crop, bg="VIOLET")
btnCrop.configure(font=('consolas', 10, 'bold'), foreground='black')
btnCrop.place(x=540, y=700)
# btnCrop.grid(row=4, column=1)

# <------Blur effect button------>
btnBlur = Button(mains, text='Blur', width=20,height=2, command=blurr, bg="ORANGE")
btnBlur.configure(font=('consolas', 10, 'bold'), foreground='black')
btnBlur.place(x=705, y=700)
# btnBlur.grid(row=5, column=1)

# <------Edge enhance effect button------>
btnEdgeEnhance = Button(mains, text='EdgeEnhance',
                        width=20,height=2, command=edgeEnhance, bg="light blue")
btnEdgeEnhance.configure(font=('consolas', 10, 'bold'), foreground='black')
btnEdgeEnhance.place(x=870, y=700)
# btnEdgeEnhance.grid(row=7, column=1)

# <------Save button------>
btnSave = Button(mains, text='Save', width=20,height=2, command=save, bg="BROWN",borderwidth=1)
btnSave.configure(font=('consolas', 10, 'bold'), foreground='white')
btnSave.place(x=1200, y=700)
# btnSave.grid(row=8, column=1)

btnClose = Button(mains, text='Close', command=close,
                  bg="BLACK", activebackground="ORANGE")
btnClose.configure(font=('consolas', 15, 'bold'), foreground='white')
btnClose.place(x=1420, y=50)

lbl=Label(mains,text="ChromaCamp - The Photo Editing Software",width="50")
lbl.configure(font=('consolas', 15, 'bold'), foreground='black')
lbl.place(x=450,y=10)
mains.mainloop()
