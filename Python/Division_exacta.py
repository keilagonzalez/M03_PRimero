dividendo=int(input("Inroduzca aqui el dividendo: "))
divisor=int(input("Introduxca aqui el divisor: "))
if (divisor==0):
    print("No se puede dividir entre 0.")
cociente=dividendo//divisor
residuo=dividendo%divisor
if(residuo==0):
    print("La division es exacta, el cociente es ",cociente,".")
else:
    print("La division no es exacta, el cociente es ",cociente,", y el residuo es ",residuo,".")
