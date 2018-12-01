primero=int(input("Introduzca el primer numero:"))
segundo=int(input("Introduzca el segundo numero:"))
if(primero%segundo==0):
    print(primero ,"es multiplo de ",segundo,".")
if(segundo%primero==0):
    print(segundo ,"es multiplo de ",primero,".")
if(primero%segundo!=0)or(segundo%primero!=0):
    print("No son multiplos.")
if(primero==segundo):
    print("Son iguales.")
