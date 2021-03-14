from tkinter import Tk, Label, StringVar

w = Tk()
w.title('Python GUI Interface')
w.geometry('1200x600')

text = StringVar()
l = Label(w, textvariable=text, font=("Arial Bold", 70))
text.set('hello world')
l.pack()


w.mainloop()