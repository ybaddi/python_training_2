
#  exercice 12
"""
Définir une classe Vecteur2D avec un constructeur 
fournissant les coordonnées par
défaut d’un vecteur du plan (par exemple : x = 0 et y = 0).
Dans le programme principal, instanciez un Vecteur2D 
sans paramètre, un Vecteur2D
avec ses deux paramètres, et affichez-les.
"""

class Vector2D:

    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
    


v1=Vector2D(1,2)
print("instance avec x={0} et y={1}".format(v1.x,v1.y))

v2=Vector2D()
print("instance avec x={0} et y={1}".format(v2.x,v2.y))

#  exercice 13
"""
Enrichissez la classe Vecteur2D précédente 
en lui ajoutant une méthode d’affichage
et une méthode de surcharge d’addition 
de deux vecteurs du plan.
Dans le programme principal, instanciez 
deux Vecteur2D, affichez-les et affichez leur
somme.
surchage c'est la redifinition d'une function 
qui existe deja par default dans toutes les class
"""

class vecteur2D:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def affichage(self):
        print("Instance avec x={0} et y={1}".format(self.x,self.y))

    def __add__(self,v): return vecteur2D(self.x + v.x,self.y+ v.y)

    def __mul__(self,v): return vecteur2D(self.x * v.x,self.y * v.y)
    def __str__(self): return "Instance avec x={0} et y={1}".format(self.x,self.y)
    

v1 = vecteur2D(1,2)
v2 = vecteur2D(2,2)

v3 = v1+v2
v3.affichage()

v4 = v1*v2
v4.affichage()
print(v3)
print(v4)

# exercice 14
"""
Un permis de chasse à points remplace désormais 
le permis de chasse traditionnel.
Chaque chasseur possède au départ un capital de 100 points. 
S’il tue une poule il perd
1 point, 3 points pour 1 chien, 5 points pour une vache et 
10 points pour un ami. Le permis coûte 200 euros.
Écrire une fonction amende qui reçoit le nombre de victimes du chasseur et qui renvoie
la somme due.
Utilisez cette fonction dans un programme principal qui saisit le nombre de victimes
et qui affiche la somme que le chasseur doit débourser.
"""

def amende(p,c,v,a):
    points_perdus = p + 3 * c + 5 * v+ 10 * a
    nbr_perdu = points_perdus /100.0
    return nbr_perdu * 200

poule = int(input("Combien de poules? "))
chien = int(input("Combien de chiens? "))
vaches = int(input("Combien de vaches? "))
amis = int(input("Combien de amis? "))

payer = amende(poule, chien, vaches, amis)

print("payer : ")
if payer == 0:
    print("rien")
else: 
    print("payer {0}".format(payer))

# exercice 15
"""
Écrire une fonction indiceDuMax() qui retourne 
l’indice du plus grand flottant parmi
ces n, et une autre indiceDuMin() qui retourne 
l’indice du plus petit.

Écrire ensuite un programme principal effectuant les actions suivantes :
– saisie filtrée de n (vous devez faire en sorte que n ne puisse pas être saisi hors de ses
limites) ;
– remplissage aléatoire des n premières valeurs de tab (on utilisera le module random(),
sans argument, qui retourne un flottant au hasard entre 0.0 et +1.0) ;
– affichage de l’amplitude du tableau (écart entre sa plus grande et sa plus petite valeur) ;
– affichage de la moyenne des n premières valeurs de tab.
"""

from random import random
def listRandom(n): 
    return [random() for item in range(n)]

t = listRandom(5)

def indiceDuMax(t): return t.index(max(t))
def indiceDuMin(t): return t.index(min(t))
print(t)
print(max(t))
print(min(t))
print(indiceDuMax(t))
print(indiceDuMin(t))