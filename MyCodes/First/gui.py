# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\Documents\Tkinter-Designer\MyCodes\First\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def mainButtonClicked():
    print("Hello, World! Clicked!")


rootWindow = Tk()

rootWindow.geometry("478x341")
rootWindow.configure(bg="#FFFFFF")

canvas = Canvas(
    rootWindow,
    bg="#FFFFFF",
    height=341,
    width=478,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=mainButtonClicked,
    relief="flat"
)

button_1.place(
    x=124.0,
    y=104.0,
    width=231.0,
    height=25.0
)
rootWindow.resizable(False, False)
rootWindow.mainloop()
