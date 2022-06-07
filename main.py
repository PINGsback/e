#!/usr/bin/python3.9

import tkinter as tk
from PIL import Image
from os import listdir
from random import choice

root = tk.Tk()
root.configure(bg='#55ffaa')

img = tk.PhotoImage(file='pictures/'+choice(listdir('pictures')))

print(img.width(), img.height())

cvs_main = tk.Label(root, image=img)
cvs_main.pack()

root.after(850, lambda: root.destroy())

root.focus()

root.mainloop()

exit(0)
