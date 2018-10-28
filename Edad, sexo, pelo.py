#Determinando el precio por edad, sexo y color de pelo.

edad = int(input("Cuantos años tienes? "))
sexo = input("Eres hombre (H), o mujer (D)? ")
pelo = input ("De que color tienes el pelo? ")
if (edad >65) : 
    print (" Te sale gratis")
if (edad <= 65) and (sexo== "H") :
    print ( "Tienes que pagar 1€")
if (sexo == "D") and (edad <= 65) and (pelo=="rubio") :
    print ("Te sale gratis")
if (edad <= 65) and (sexo == "D") and (pelo != "rubio") :
    print ( "Pagas 0.5€")
