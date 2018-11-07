any_actual=int(input("¿En que anyo estamos? "))
any_qualsevol=int(input("¿Con que anyo quieres calcular? "))
if (any_actual==0)or(any_qualsevol==0):
    print("0 no es un anyo valido!")
else:
    if (any_actual==any_qualsevol):
	      print("Es el mismo anyo!")
    else:
        resultat=(any_qualsevol)-(any_actual)
        if(any_qualsevol>any_actual):
            print("Faltan", resultat, "anyos para llegar al", any_qualsevol)
        else:
            resultat=(any_actual)-(any_qualsevol)
            if(any_actual > any_qualsevol):
                print("Han pasado", resultat, "anyos desde", any_qualsevol)
