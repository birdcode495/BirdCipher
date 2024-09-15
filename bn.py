import tkinter as tk
from tkinter import ttk
from playsound import playsound


root = tk.Tk()
root.geometry('1100x700')

def play():

	playsound('ttsmaker-file-2024-9-14-19-11-37.mp3')


gf = tk.PhotoImage(file = 'Computer virus.png')

hn = tk.Button(root, image = gf, command = lambda:play())
hn.place(x = 30, y = 30)



root.mainloop()