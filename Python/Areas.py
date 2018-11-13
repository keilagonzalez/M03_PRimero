figura=input("¿Quieres calcular el area de un triangulo, o un circulo? ")
if(figura=="triangulo"):
    base=int(input("¿Que base tiene el triangulo? "))
    altura=int(input("¿Que altura tiene el triangulo? "))
    area_triangulo=(base*altura)/2
    print("El area del triangulo es", area_triangulo,)
else:
    if(figura=="circulo"):
        radio=int(input("¿Cual es el radio del circulo? "))
        area_circulo=(radio**2)*3.14
        print("El area del circulo es", area_circulo)
    else:
        print("Solo triangulo o circulo")
