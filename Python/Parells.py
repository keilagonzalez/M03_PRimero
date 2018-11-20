"""
dividendo|resultat
        2|parell
        3|imparell
        0|parell
       -8|parell
       -7|imparell
"""
Dividendo=float(input("¿Cual es el dividendo?"))
Divisor=float(input("¿Cual es el divisor? "))
Residuo=Dividendo%Divisor
if (Residuo==0):
    print("El", Dividendo, "es par.")
else: 
    print("El", Dividendo, "es impar.")
