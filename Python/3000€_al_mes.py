loteria = input("¿Le ha tocado la loteria? ")
edad = int(input("¿Cuantos anyos tiene?"))
malaltia = input ("¿Tiene problemas cardiacos? ")
solteria = input ("¿Esta soltero? ")
nota_m01 = int(input("¿Que nota has sacado de m01?"))
nota_m02 = int(input("¿Que nota has sacado de m02?"))
nota_m03 = int(input("¿Que nota has sacado de m03?"))
nota_m05 = int(input("¿Que nota has sacado de m05?"))
ponderada = (nota_m01*0.30)+(nota_m02*0.40)+(nota_m03*0.25)+(nota_m05*0.05)
if (loteria=="si") or (edad>=80 and malaltia=="si" and solteria=="si") or (nota_m01>=9 and nota_m02>=10 and nota_m03>=8 and (nota_m05>=6 and nota_m05<=8)) or (ponderada>=8):
    print ("Tienes los 3000€ mensuales")
else:
    print("Sigue provando, no hay 3000€")
