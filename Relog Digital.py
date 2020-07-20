# ©Sn.Lionel90, do not share without credit me, thanks!!

from tkinter import *
from tkinter.ttk import *
from time import strftime

ventana_reloj = Tk()
ventana_reloj.geometry('200x60')
ventana_reloj.title ('reloj digital snLionel90')

def reloj ():
    string = strftime('%H:%M:%S')
    etiqueta.config (text = string)
    etiqueta.after(1000, reloj)

#etiqueta_titulo = Label(ventana_reloj,Text="Reloj digital snLionel90" ,font = ('calibri',15 , 'italic'),foreground = 'black' ).place(x=60, y= 20)
etiqueta = Label(ventana_reloj, font = ('calibri', 30 , 'italic'), background = 'black', foreground = 'navajo white')
etiqueta.pack(anchor = 'center')

reloj()
ventana_reloj.mainloop()



