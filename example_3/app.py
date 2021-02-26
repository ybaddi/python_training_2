# exercice 1
""" 
Utilisez une exception pour calculer, 
dans une boucle évoluant de -3 à 3 compris, 
la valeur de sin(x)/x.
"""
from math import sin
for x in range(-3,4):
    try:
        print("{:.3f}".format(sin(x)/x))
    except:
        print("{:.3f}".format(float(1)))

#  exercice 2
"""
Écrire une procédure table avec quatre paramètres : base, debut, 
fin et inc.
Cette procédure doit afficher la table des base, de debut à fin, 
de inc en inc.
Tester la procédure par un appel dans le programme principal.
"""

def table(base, debut, fin, inc):
    n = debut
    while n <=fin:
        print(n, 'x', base, '=', n*base)
        n += inc # n = n + inc  *= -= 

table(7,2,14,2)


#  exercice 3
"""
La clause else des boucles. Dans cet exercice, effectuez 
les saisies avec des integerbox et les affichages avec des msgbox, 
tous deux appartenant au module easygui.
Initialisez une liste avec 5 entiers de votre choix puis saisissez 
un entier. Dans une boucle for, parcourez la liste. Si l’entier 
saisie appartient à la liste, sauvez-le et interrompez la boucle 
(puisque vous l’avez trouvé). Si la boucle s’est bien terminée,
utilisez une clause else pour afficher un message l’annonçant.
Entrez maintenant un autre entier, cette fois-ci positif.
Écrivez une boucle while pour déterminer si cet entier est premier. 
S’il ne l’est pas, la boucle devra afficher le premier diviseur 
trouvé et s’interrompre. S’il est premier,
l’afficher dans une clause else.
"""

#  exercice 4
"""
1- Écrire une fonction cube qui retourne le cube de son argument.
2-Écrire une fonction volumeSphere qui calcule le volume d’une sphère 
de rayon r fourni
en argument et qui utilise la fonction cube.
Tester la fonction volumeSphere par un appel dans le programme principal.
"""

#  exercice 4
"""
Écrire une fonction maFonction qui retourne f (x) = 2x^3 + x −5.
Écrire une procédure tabuler avec quatre paramètres : fonction, borneInf,
 borneSup et nbPas. Cette procédure affiche les valeurs de fonction, 
 de borneInf à borneSup, tous les nbPas. Elle doit respecter 
 borneInf < borneSup.
Tester cette procédure par un appel dans le programme principal après 
avoir saisi les deux bornes dans une floatbox et le nombre de pas 
dans une integerbox (utilisez le module easyguiB).
"""