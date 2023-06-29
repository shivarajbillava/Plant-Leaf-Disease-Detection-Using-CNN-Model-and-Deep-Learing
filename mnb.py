import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from easygui import *
import numpy
# load the trained model to classify sign
from tensorflow.keras.models import load_model

model = load_model('my_model.h5')

# dictionary to label all traffic signs class.
classes = {0: 'Apple___Cedar_apple_rust',
           1: 'Apple___healthy',
           2: 'Cherry___healthy',
           3: 'Cherry___Powdery_mildew',
           4: 'Grape___Esca_(Black_Measles)',
           5: 'Grape___healthy'
           }

# initialise GUI
top = tk.Tk()
top.geometry('800x600')
top.title('Leaf Disease Classification')
top.configure(background='#CDCDCD')

label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)


def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30, 30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    print(image.shape)
    pred = model.predict_classes([image])[0]
    sign = classes[pred + 1]
    print(sign)
    if sign == 'Cherry___healthy':
        title = "Arive-Dantu Properties"
        with open('Arive-Dantu.txt') as f:
            lines = f.read()

        # message for our window


        # button message by default it is "OK"
        button = "Close"

        # creating a message box
        msgbox(lines, title, button)
    else:
        title = "Arive-Dantu Properties"
        with open('Arive-Dantu.txt') as f:
            lines = f.read()

        # message for our window


        # button message by default it is "OK"
        button = "Close"

        # creating a message box
        msgbox(lines, title, button)
    label.configure(foreground='#011638', text=sign)


def show_classify_button(file_path):
    classify_b = Button(top, text="Classify Image", command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass


upload = Button(top, text="Upload an image", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))

upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Leaf Disease Classification", pady=20, font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()
top.mainloop()
