from tkinter import *
import tkinter as tk
from tkinter import messagebox,Tk, ttk
from microfono import micro, welcome  

class MyWindow(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        root.geometry("250x120")
        root.resizable(0,0)
        root.title("Asistente")
        root.wm_attributes("-topmost", True)

        labelWelcome = tk.Label(self, height= 2, text="Bienvenido, soy tu asistente virtual!")
        labelWelcome.pack()

        btnSpeak = tk.Button(self, text="DIME",height= 5, width= 25, command=micro)

        btnSpeak.pack()
        

if __name__ == "__main__":
    
    root = tk.Tk()
    
    MyWindow(root).pack()
    welcome()

    root.mainloop()
