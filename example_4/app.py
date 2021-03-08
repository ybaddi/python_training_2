
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

# exercice 4: Ecrire un programme Python pour lire les n dernières lignes d'un fichier

# exercice 5: Ecrire un programme Python pour lire un fichier ligne par ligne et le stocker 
# dans une liste.

# exercice 6: 