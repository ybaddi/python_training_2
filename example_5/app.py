# atlas toolkit for python, pyGUI cocoa
# chaquopy
#komodo
# from tkinter import Tk, Label, StringVar

# w = Tk('GUI Interface')

# text = StringVar()
# l = Label(w, textvariable=text)
# text.set('hello world')
# l.pack()


# w.mainloop()



# exercice 1: Write a Python program to read each row from a given csv file 
# and print a list of strings. 

import csv
with open('file.csv') as file:
    data = csv.reader(file, delimiter=',')
    for row in data : 
        print('|'.join(row))

# exercice 2: Write a Python program to read a given CSV file having tab delimiter. 
 

# exercice 3: Write a Python program to read a given CSV file as a list.
 

# exercice 4: Write a Python program to read a given CSV file as a dictionary
 


# exercice 5: Write a Python program to read each row from a given csv file and print a list of strings. 
 

# exercice 6: Write a Python program to read a given CSV file having tab delimiter. 
 

# exercice 7: Write a Python program to read a given CSV file as a list.
 

# exercice 8: Write a Python program to read a given CSV file as a dictionary