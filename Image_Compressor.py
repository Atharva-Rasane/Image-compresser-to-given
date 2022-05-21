from tkinter import *
import tkinter.filedialog
import os
import tkinter as tk
from PIL import Image

#Global Variables
f_location = ""
width = 0
height = 0
ratio = 1
options = [
    "kb",
    "mb",
    "gb"
]
val = {
    "kb" : 1000,
    "mb" : 1000000,
    "gb" : 1000000000
}

#Open Button Function
def openfile():
    global width
    global height
    global f_location
    global ratio
    f_location = tkinter.filedialog.askopenfilename()
    width, height = Image.open(f_location).size
    ratio = width/height
    l0.config(text=f_location)
    save_B.config(state=NORMAL)

#Save file Function
def savefile():
    global width
    global height
    global f_location
    file_size = 9999999999
    quality = 100
    i = 1
    print("|Sn no|" + " " + "|Quality|" + " " + "|Compressed Size|" + " " + "|Compressed Width|" + " " + "|Compressed Height|\n")
    while file_size > int(e.get())*val[clicked.get()]:
        quality -= 1
        picture = Image.open(f_location)
        picture = picture.convert('RGB')
        picture = picture.resize((int(quality / 100 * width), int(quality / 100 * height)), Image.Resampling.LANCZOS)
        width1, height1 = picture.size
        picture.save("Compressed_.jpeg",
                     "JPEG",
                     #optimize=True,
                     #quality=quality
                     )
        file_size = os.path.getsize("Compressed_.jpeg")
        print(str(i)+"\t\t    "+str(quality)+"\t\t   "+str(file_size)+"\t\t     "+str(width1)+"\t\t          "+str(height1)+"\n")
        if quality == 1:
            break
        i+=1
    print(tk.END, "Done")
    s_location = tkinter.filedialog.asksaveasfilename(initialfile='Untitled.jpeg',defaultextension=".jpeg", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    picture = Image.open(f_location)
    picture = picture.convert('RGB')
    picture = picture.resize((int(quality / 100 * width), int(quality / 100  * height)), Image.Resampling.LANCZOS)
    #picture = picture.resize((int(quality / 100 * height), int(quality / 100 * width)), Image.Resampling.LANCZOS)
    print(int(quality / 100 * height), int(quality / 100 * width),height,width)
    picture.save(s_location,
                 "JPEG",
                 #optimize=True,
                 #quality=quality
                 )



#Tkinter Root Loop
root = Tk()
#Root Geometry
root.geometry("400x110")
root.resizable(width=False, height=False)
#Open Button
open_B = Button(root, text="Open", command=openfile).grid(row=0, column=0, sticky='w')
#File Labels
ln1 = Label(root, text="File: ").grid(row=1,column=0, sticky='w')
l0 = Label(root, text="No file selected")
l0.grid(row=1,column=1,columnspan=5, sticky='w')
#Size Entry
e = Entry(root)
e.insert(0, "1")
#Size Entry Label
l1 = Label(root, text="Maximum Required Size: ").grid(row=2,column=0,columnspan=2, sticky='w')
e.grid(row=2, column=2, sticky='w')
#Size format options menu
clicked = StringVar()
clicked.set("mb")
drop = OptionMenu(root, clicked, *options)
drop.grid(row=2,column=3, sticky='w')
#Save Button
save_B = Button(root, text="Compress and Save", command=savefile, state=DISABLED)
save_B.grid(row=3, column=0,columnspan=2, sticky='w')
root.mainloop()
