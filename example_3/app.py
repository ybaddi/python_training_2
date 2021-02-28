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
# from easygui import integerbox, msgbox
# liste = [2,4,5,6,7,11]
# cible = integerbox("Veuillez entrer un entier:","")
# print(cible)

#  exercice 4
"""
1- Écrire une fonction cube qui retourne le cube de son argument.
2- Écrire une fonction volumeSphere qui calcule le volume d’une sphère 
de rayon r fourni
en argument et qui utilise la fonction cube.
Tester la fonction volumeSphere par un appel dans le programme principal.
"""
from math import pi
def cube(x): return x**3
    #  4 * pi * r**3/3

def volumeSphere(r): return 4 * pi * cube(r) / 3

rayon = float(input("Rayon :"))
print("Volume de la sphere de rayon {:.1f} est : {:.3f}"
.format(rayon,volumeSphere(rayon)))

#  exercice 5
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
def maFonction(x): return 2 * x**3 + x - 5

def tabular(fonction, bornInf, bornSup, nbPas): 
    # h = (bornSup - bornInf) / float(nbPas)
    x = bornInf
    while x <= bornSup:
        y = fonction(x)
        print("f({:.2f}) = {:.3f}".format(x,y))
        x += nbPas

tabular(maFonction, 0, 100, 10)
tabular(maFonction, 0, 10, 2)

#  exercice 6
"""
définir la liste : liste =[17, 38, 10, 25, 72], 
puis effectuez les actions suivantes :
– triez et affichez la liste ;
– ajoutez l’élément 12 à la liste et affichez la liste ;
– renversez et affichez la liste ;
– affichez l’indice de l’élément 17 ;
– enlevez l’élément 38 et affichez la liste ;
– affichez la sous-liste du 2eau 3eélément ;
– affichez la sous-liste du début au 2eélément ;
– affichez la sous-liste du 3eélément à la fin de la liste ;
– affichez la sous-liste complète de la liste ;
– affichez le dernier élément en utilisant un indiçage négatif.
Bien remarquer que certaines méthodes de liste ne retournent rien.
"""

nombres = [17, 38, 10, 25, 72]
print(" Liste initiale ".center(50, '+'))
print(nombres, '\n')

rien = input('"Entree"')
print(" Tri ".center(50, '-'))
nombres.sort()
print(nombres, '\n')
rien = input('"Entree"')
print(" Ajout d'un element ".center(50, '-'))
nombres.append(12)
print(nombres, '\n')
rien = input('"Entree"')
print(" Retournement ".center(50, '-'))
nombres.reverse()
print(nombres, '\n')
rien = input('"Entree"')
print(" Indice d'un element ".center(50, '-'))
print(nombres.index(17), '\n')
rien = input('"Entree"')
print(" Retrait d'un element ".center(50, '-'))
nombres.remove(38)
print(nombres, '\n')
rien = input('"Entree"')
print(" Indicage ".center(50, '-'))
print("nombres[1:3] =", nombres[1:3])
print("nombres[:2] =", nombres[:2])
print("nombres[2:] =", nombres[2:])
print("nombres[:] =", nombres[:])
print("nombres[-1] =", nombres[-1])


#  exercice 7 
"""
1- Écrire une fonction compterMots ayant un argument 
(une chaîne de caractères) er qui
renvoie un dictionnaire qui contient la fréquence 
de tous les mots de la chaîne entrée.
"hello world, hello karim, hello alvin" => 
hello=3, world=1, karim=1, alvin=1 
2- meme exercice pour les caractere compterCaracter
liste= " ".split(' ')
"""
def compterMots(texte):
    dict = {}
    listeMots = texte.split()
    for item in listeMots:
        if item in dict:
            dict[item] = dict[item] + 1
        else:
            dict[item] = 1
    return dict
# programme principal -----------------------------------------------
res = compterMots("Ala Met Asn Glu Met Cys Asn Glu Hou Ala Met Gli Asn Asn")
for c in res.keys():
    print(c, "-->", res[c])

#  exercice 8
"""
Implémentez une pile LIFO avec une liste.
Pour cela, définir trois fonctions :

- pile : qui retourne une pile à partir d’une liste 
variable d’éléments passés en paramètre ;

- empile : empile un élément en « haut » de la pile ;
- depile : dépile un élément du « haut » de la pile.

      ___________________________
=>    12 11
      __________________________
2- meme exercice avec FIFO
"""

def pile(*args):
    p=[]
    if not args:
        return p
    for item in args:
        p.append(item)
    return list(p)

def empiler(p,a): p.append(a)

def depiler(p): 
    try:
        p.pop()
    except:
        print("la pile est vide")

print(" Pile ".center(50, '-'))
numbersList=pile(5,6,7,8,9)
print(numbersList)
rien = input('"Entree"')
print(" empiler ".center(50, '-'))
empiler(numbersList, 13)
print(numbersList)
rien = input('"Entree"')
print(" depiler ".center(50, '-'))
for i in range(7):
    depiler(numbersList)
    print(numbersList)


#  exercice 9
"""
1-Écrire un module de calcul des racines du 
trinôme réel : ax2 +bx +c.
Le module définit une fonction trinome avec 
les trois paramètres du trinôme, a, b et
c. La fonction doit retourner un tuple dont 
le premier élément est les racines
du trinôme (0, 1 ou 2), et les autres éléments sont les racines éventuelles.
Testez votre fonction avec les trois jeux de valeurs suivantes : 1,−3, 2, 1,−2, 1 et 1, 1, 1.

2-Écrire un programme principal utilisant le module précédent.
Les trois paramètres seront saisis dans une flotbox du module easyguiB et les résultats seront affichés dans une msgbox.
"""
from math import sqrt
def trinome(a,b,c):
    delta = b**2 - 4*a*c

    if delta > 0.0:
        racine_delta = sqrt(delta)
        return (2, (-b-racine_delta)/(2*a), (-b+racine_delta)/(2*a))
    if delta < 0.0:
        return (0,)
    else:
        return (1, (-b)/(2*a))

print(trinome(1.0,-3.0,2.0)) # x^2 -3x+2=0
print(trinome(1.0,-2.0,1.0)) # x^2 -2x+1=0
print(trinome(1.0,1.0,1.0)) # x^2 -x+1=0
#  exercice 10
"""
Définir une classe MaClasse possédant 
les attributs suivants :
données : deux attributs de classes : x = 23 et y = x + 5.
méthode : une méthode affiche contenant un attribut d’instance z = 42 et les affichages de y et de z.
Dans le programme principal, instanciez un objet de la classe MaClasse et invoquez la
méthode affiche.
"""
class MaClass:
    x=23
    y=x+5

    def affiche(self):
        self.z=42
        print(MaClass.y)
        print(self.z)

obj = MaClass()
obj.affiche()

#  exercice 11
"""
Définir une classe Rectangle avec un constructeur 
donnant des valeurs (longueur et
largeur) par défaut et un attribut 
nom = "rectangle", une méthode d’affichage et
une méthode surface renvoyant la surface d’une instance.
Définir une classe Carre héritant de Rectangle et 
qui surcharge l’attribut d’instance :
nom = "carré".
Dans le programme principal, instanciez un Rectangle et un Carre et affichez-les
"""
class Rectangle:
    # nom = "rectangle"
    def __init__(self, longueur, largeur ):
        print("test")
        self.longueur = longueur
        self.largeur= largeur
        self.nom = "rectangle"

    def affichage(self):
        print("le nom est {0} avec longueur {1} et largeur {2}"
        .format(self.nom, self.longueur, self.largeur))

    def surface(self):
        print("la surface est {0}".format(self.longueur * self.largeur))


rec = Rectangle(12,24)
rec.affichage()
rec.surface()


#  exercice 12
"""
Définir une classe Vecteur2D avec un constructeur fournissant les coordonnées par
défaut d’un vecteur du plan (par exemple : x = 0 et y = 0).
Dans le programme principal, instanciez un Vecteur2D sans paramètre, un Vecteur2D
avec ses deux paramètres, et affichez-les.
"""

#  exercice 13
"""
Enrichissez la classe Vecteur2D précédente en lui ajoutant une méthode d’affichage
et une méthode de surcharge d’addition de deux vecteurs du plan.
Dans le programme principal, instanciez deux Vecteur2D, affichez-les et affichez leur
somme.
"""