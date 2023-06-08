from tkinter import *
from tkinter import ttk

root = Tk()

hosgeldiniz=Label(text="Welcome\n",font="Verdana 25").grid(column=1, row=0)

değer = Entry(font="Verdana 14",fg="White").grid(column=1, row=1)
label = Label(text="Name").grid(column=0, row=1)

soyad= Entry(font=" Verdana 14", fg="White").grid(column=1, row=2)
soyadı= Label(text="Surname ").grid(column=0, row=2)

Yas= Entry(font=" Verdana 14", fg="White").grid(column=1, row=3)
Yası= Label(text="Age ").grid(column=0, row=3)

cinsiyet= Entry(font=" Verdana 14", fg="White").grid(column=1, row=4)
cinsiyeti= Label(text="Cinsiyet ").grid(column=0, row=4)

cıkıs=ttk.Button(text="Cıkıs",command=root.quit).grid(column=1, row=5)
root.mainloop()