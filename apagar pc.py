import os
from tkinter import *
import tkinter 
import threading
from tkinter import messagebox, filedialog

def apagar():
    global executing
    shutdown = input("Quieres apagar el equipo ? (Si/No):")

    if (shutdown == 'no'):
        exit()
    else:
        messagebox.showwarning("Apagao","Apagando Equipo en 10 segundos")
        os.system("shutdown /s /t 10") 

def salir():
    exit(0)

root = tkinter.Tk() #ventana tk
root.title("Apagar equipo")
root.configure(background="white")
root.geometry("250x100")
executing = False

etiqueta = Label(root,text='Quieres apagar el equipo?',bg="black",fg="red",width=25,height=2)
etiqueta.place(x=26,y=10)
Button(root,text="NO",activebackground='red',activeforeground='green',fg='white',bg ='green',command=salir).place(x=130,y=50) 
Button(root,text="SI",activebackground='white',activeforeground='green',fg='white',bg ='green',command=apagar).place(x=70,y=50)

apagar()
root.mainloop()