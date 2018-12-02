Dividendo=float(input("¿Cual es el dividendo?"))
Divisor=float(input("¿Cual es el divisor? "))
Residuo=Dividendo%Divisor
if (Residuo==0):
    print("El", Dividendo, "es par.")
else: 
    print("El", Dividendo, "es impar.")
