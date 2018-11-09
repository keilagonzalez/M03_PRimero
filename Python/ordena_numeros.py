# Entrada | Sortida #
#   1,2,3 '| 1,2,3   #
#   1,3,2 '| 1,2,3   #
#   2,1,3 '| 1,2,3   # 
#   2,3,1 '| 1,2,3   #
#   3,2,1 '| 1,2,3   #
#   3,1,2 '| 1,2,3   #
#   1,1,1 '| 1,1,1   #
#   1,1,2 '| 1,1,2   #
#   2,1,1 | 1,1,3   #
#   2,1,2 | 1,2,2   #
primer=int(input("Introdueix el primer numero: "))
segon=int(input("Introdueix el segon numero: "))
tercer=int(input("Introdueix el tercer numero: "))
if(primer<segon<tercer):
    print(primer,",",segon,",",tercer) 
else:
    if(primer<segon>tercer):
        print(primer,",",tercer,",", segon)
    else:
        if(primer>segon<tercer):
            print(segon,",",primer,",",tercer)
        else:
            if (primer<segon)and(primer>tercer)and(segon>primer):
                print(tercer,",",segon,",",primer)
            else:
                if (primer>segon>tercer):
                    print (tercer,",",segon,",",primer)
                else: 
                    if(primer==segon==tercer):
                        print(primer,",",segon,",",tercer)
                    else:
                        if (primer==segon<tercer):
                            print(primer,",",segon,",",tercer)
                        else:
                            if (primer==segon>tercer):
                                print(tercer,",",primer,",",segon)
                        
