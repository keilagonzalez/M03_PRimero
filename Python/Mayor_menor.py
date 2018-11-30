primero=float(input("Seleccione el primer numero: "))
segundo=float(input("Seleccione el segundo numero: "))
tercero=float(input("Seleccione el tercer numero: "))
if(primero==segundo==tercero==primero):
    print("Los tres numeros son iguales.")
else:
    if(primero==segundo>tercero<primero)or(primero==segundo<tercero>primero)or(primero<segundo>tercero==primero)or(primero>segundo<tercero==primero)or(primero<segundo==tercero>primero)or(primero>segundo==tercero<primero):
        print("Has escrito uno de los numeros dos veces.")
    else:
        print("Los tres numeros que hays escrito son distintos.")
    
