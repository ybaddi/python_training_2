
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
"""

# exercice 14
"""
Un permis de chasse à points remplace désormais le permis de chasse traditionnel.
Chaque chasseur possède au départ un capital de 100 points. S’il tue une poule il perd
1 point, 3 points pour 1 chien, 5 points pour une vache et 10 points pour un ami. Le
permis coûte 200 euros.
Écrire une fonction amende qui reçoit le nombre de victimes du chasseur et qui renvoie
la somme due.
Utilisez cette fonction dans un programme principal qui saisit le nombre de victimes
et qui affiche la somme que le chasseur doit débourser.
"""