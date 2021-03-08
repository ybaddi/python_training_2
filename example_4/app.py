
# exercice 1 : ecrir un programme qui lis la totalite d'un fichier text

txt = open("file.txt")
print(txt.read())

print("=============")

def read_file(filename):
    txt = open(filename)
    print(txt.read())

read_file("file.txt")
print("=============")
# exercice 2 : ecrir un programme qui lis les n premiers ligne d'un fichier text

from itertools import islice
def read_n_line_file(filename, n):
    str=''
    with open(filename) as f:
        for line in islice(f, n):
            str += line
        print(str)

read_n_line_file("file.txt",2)
print("=============")
# exercice 3: Écrivez un programme Python pour ajouter du texte à un fichier et afficher le texte.
def write_file(filename):
    str=''
    with open(filename,"w") as f:
        f.write("hello from Python\n")
        f.write("hello from Python")

write_file("file_1.txt")
read_file("file_1.txt")
print("=============")
# exercice 4: Ecrire un programme Python pour lire les n dernières lignes d'un fichier
# a faire chez vous
import sys
import os
# exercice 5: Ecrire un programme Python pour lire un fichier ligne par ligne et le stocker 
# dans une liste.

def read_lines_file(filename):
    with open(filename, "r") as f:
        data =f.readlines()
        return data

print(read_lines_file("file.txt")[0:2])
print("=============")
# exercice 6:  Écrire un programme Python pour compter la fréquence des mots dans un fichier

from collections import Counter
def count_words_file(filename):
    with open(filename, "r") as f:
        return Counter(f.read().split())

print(count_words_file("file.txt"))
print("=============")
# exercice 7: Écrire un programme Python pour convertir un entier en chaîne de caractères 
# dans n'importe quelle base
# // 

def base_to_string(n,base): 
    symbole= "0123456789ABCDEF"
    if n < base:
        return symbole[n]
    else:
        return base_to_string(n//base,base) +  symbole[n%base]


print(base_to_string(2835,2))   # B13  D
print("=============")

# exercice 8: un programme qui calcule le factoriel de x    x!= 1*2*3*4.....x  5!=1*2*3*4*5

def factoriel(x): 
    res=1
    for i in range(1,x+1): 
        res = res*i
    return res

def factoriel_rec(x): 
    if x == 0: 
        return 1
    else: return factoriel_rec(x-1)*x

print(factoriel(5))
print(factoriel_rec(5))
print("=============")
#  exercice 9
x=15
y=4

print(x/y)
print((x//y) + 1)
print("=============")



# exercice 10:  ecrir un programme python qui se connect a une base de donnee SQLite
#  et qui affiche sa version

import sqlite3

try:
    sqlite_Connection = sqlite3.connect('database.db')
    conn = sqlite_Connection.cursor()
    req="select sqlite_version();"
    conn.execute(req)
    record = conn.fetchall()
    print(record)
    conn.close()
except sqlite3.OperationalError as error:
    print(error)
# finally:
#     print("la version du sqlite")

print("hello")


# exercice 11 : 
# 1-Écrire un programme Python pour connecter une base de données et créer 
# une table SQLite dans la base de données.
# 2- Ecrire un programme Python pour lister les tables d'un fichier de base 
# de données SQLite donné. 
# 3-Écrivez un programme Python pour créer une table et insérez des enregistrements 
# dans cette table. 
# 4-Enfin, sélectionnez toutes les lignes de la table et affichez 
# les enregistrements.
from sqlite3 import Error
def sql_connect():
    try:
        sqlite_Connection = sqlite3.connect('database.db')
        return sqlite_Connection
    except Error:
        print(Error)

def sql_creat_table(sqlite_Connection):
    try:
        conn = sqlite_Connection.cursor()
        req="Create table etudiant(id int, name varchar(255), email varchar(255), telephone varchar(255))"
        conn.execute(req)
        sqlite_Connection.commit()
    except Error:
        print(Error)
    
def sql_table(sqlite_Connection):
    conn = sqlite_Connection.cursor()
    req="select id, name, email, telephone from etudiant"
    conn.execute(req)
    record = conn.fetchall()
    print(record)

class Etudiant:    
    def __init__(self,id,nom,email,telephone):
        self.id=id
        self.nom=nom
        self.email=email
        self.telephone=telephone

def add_etudiant(etudiant):
    conn = sqlite_Connection.cursor()
    req=f"insert into etudiant values('{etudiant.id}','{etudiant.nom}','{etudiant.email}','{etudiant.telephone}');"
    conn.execute(req)
    sqlite_Connection.commit()

connection = sql_connect()
sql_creat_table(connection)
sql_table(connection)
e1=Etudiant(1,'baddi','b@b.com','06587678')
e2=Etudiant(2,'alvin','b@b.com','06587678')
e3=Etudiant(3,'karim','b@b.com','06587678')
add_etudiant(e1)
add_etudiant(e2)
add_etudiant(e3)
sql_table(connection)
connection.close()


# 
# Python GUI tkinter