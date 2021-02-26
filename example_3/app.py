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
