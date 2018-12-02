print("MENU:")
print("  PIEDRA")
print("  PAPEL")  
print("  TIJERAS")
usuario=input("Introduzca su seleccion: ")
usuario.lower()
from random import choice
posibilidades=["piedra","papel","tijeras"]
maquina=(choice(posibilidades))
print("Tu has sacado: ",usuario,)
print("La maquina ha sacado: ",maquina,)
if(usuario==maquina):
    print("Empate")
else:
    if((usuario=="piedra")and(maquina=="tijeras"))or((usuario=="papel")and(maquina=="piedra"))or((usuario=="tijeras")and(maquina=="papel")):
        print("Has ganado!!")
    else:
        if((maquina=="piedra")and(usuario=="tijeras"))or((maquina=="papel")and(usuario=="piedra"))or((maquina=="tijeras")and(usuario=="papel")):
            print("Ha ganado la maquina...")
