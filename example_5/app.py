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

with open('file_tab.csv') as file_tab:
    data_tab = csv.reader(file_tab, delimiter=';')
    for row_tab in data_tab : 
        print(row_tab)

# exercice 3: Write a Python program to read a given CSV file as a list.

with open('file.csv') as file:
    data = csv.reader(file, delimiter=';')
    data_list = list(data)

print(data_list)

# exercice 4: Write a Python program to read a given CSV file as a dictionary
 
with open('file.csv') as file:
    data = csv.DictReader(file, delimiter=';')
    for row in data : 
        print(row)



# exercice 5: ecrir un programme python qui permet d'afficher les folder, files d'un path

import os
print(os.name)
print(os.uname())
print(os.getcwd())
print(os.listdir('.'))
print(os.listdir(os.getcwd()))
print(os.listdir(os.getcwd())[1])

f = open(os.listdir(os.getcwd())[1], 'r')
text = f.read()
f.close()
print(text)

if os.name == "nt":
    command = "dir"
else:
    command = "ls -l"
os.system(command)


import time
def time_struct(s):
    print('year : ', s.tm_year)
    print('tm_mon : ', s.tm_mon)
    print('tm_mday : ', s.tm_mday)
    print('tm_hour : ', s.tm_hour)
    print('tm_min : ', s.tm_min)
    print('tm_sec : ', s.tm_year)
    print('tm_wday : ', s.tm_wday)
    
print(time.localtime())
time_struct(time.localtime())
print(time.gmtime())


fd = os.open('file.csv', os.O_RDONLY)
os.fchown(fd,0,-1)
os.fchown(fd, -1,0)
os.close(fd)

# for x in range(10):
#     time.sleep(3)
#     print('sleep for 3 sec')

print(time.ctime())
print(time.ctime(10))
