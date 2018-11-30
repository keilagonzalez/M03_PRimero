print("Menu de gasolina:")
print("Super:")
print("  1.Normal: 1.5€")
print("  2.Turbo: 1.55€")
print("Sin Plomo")
print("  3.Normal: 1.6€")
print("  4.Con Aditivos(Sabor Naranja): 1.65€")
print("Diesel:")
print("  5.Normal: 1.7€")
print("  6.Fast&Furious: 1.75€")
super_normal=1
super_turbo=2
sin_normal=3
sin_aditivos=4
diesel_normal=5
diesel_fastfurious=6
precio_1=1.5
precio_2=1.55
precio_3=1.6
precio_4=1.65
precio_5=1.7
precio_6=1.75
seleccion=int(input("Introduzca el numero de la gasolina deseada: "))
litros=int(input("¿Cuantos litros desea? "))
if(seleccion==1):
    resultado=(litros*precio_1)
    print("Importe:", resultado,"€")
else:
    if(seleccion==2):
        resultado=(litros*precio_2)
        print("Importe:", resultado,"€")
    else:
        if(seleccion==3):
            resultado=(litros*precio_3)
            print("Importe:", resultado,"€")
        else:
            if(seleccion==4):
                resultado=(litros*precio_4)
                print("Importe:", resultado,"€")
            else:
                if(seleccion==5):
                    resultado=(litros*precio_5)
                    print("Importe:", resultado,"€")
                else:
                    if(seleccion==6):
                        resultado=(litros*precio_6)
                        print("Importe:", resultado,"€")
