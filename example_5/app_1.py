import tkinter as tk
from tkinter import  ttk

w = tk.Tk()
w.title('Python GUI Interface')
w.geometry('1200x600')

text = tk.StringVar()
l = tk.Label(w, textvariable=text, font=("Arial Bold", 70))
text.set('hello world')
l.pack()

my_combobox = ttk.Combobox(w,textvariable=text, values=['baddi', 'karim', 'alvin'])
my_combobox.pack()

button_1 = tk.Button(w, text='Quit', height=2, width=40, command=w.destroy)
button_1.pack()

w.mainloop()