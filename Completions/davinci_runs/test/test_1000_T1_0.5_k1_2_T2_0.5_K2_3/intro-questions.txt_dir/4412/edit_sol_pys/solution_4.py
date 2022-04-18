# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:44:08 2020

@author: ritik
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 250, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg = 'lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def getPNG ():
    global im1
    
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)
    
browseButton_PNG = tk.Button(text="      Import PNG File     ", command=getPNG, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_PNG)

def convertToJPG ():
    global im1
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    im1.save(export_file_path)

saveAsButton_JPG = tk.Button(text='Convert PNG to JPG', command=convertToJPG, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_JPG)

root.mainloop()
