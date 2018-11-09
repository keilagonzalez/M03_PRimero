# Entrada | Sortida #
#   1,2,3 | 1,2,3   #
#   1,3,2 | 1,2,3   #
#   2,1,3 | 1,2,3   # 
#   2,3,1 | 1,2,3   #
#   3,2,1 | 1,2,3   #
#   3,1,2 | 1,2,3   #
#   1,1,1 | 1,1,1   #
#   1,1,2 | 1,1,2   #
#   2,2,1 | 1,2,2   #
#   1,2,2 | 1,2,2   #
#   2,1,1 | 1,1,2   #
#   2,1,2 | 1,2,2   #
#   2,3,2 | 2,2,3   #
primer=int(input("Introdueix el primer numero: "))
segon=int(input("Introdueix el segon numero: "))
tercer=int(input("Introdueix el tercer numero: "))
if(primer<segon<tercer>primer):
    print(primer,",",segon,",",tercer) 
else:
    if(primer<segon>tercer>primer):
        print(primer,",",tercer,",", segon)
    else:
        if(primer>segon<tercer>primer):
            print(segon,",",primer,",",tercer)
        else:
            if(primer<segon>tercer<primer):
                print(tercer,",",primer,",",segon)
            else:
                if(primer>segon>tercer<primer):
                    print(tercer,",",segon,",",primer)
                else:
                    if(primer>segon<tercer<primer):
                        print(segon,",",tercer,",",primer)
                    else:
                         if(primer==segon==tercer==primer):
                            print(primer,",",segon,",",tercer)
                         else:
                             if(primer==segon<tercer>primer):
                                print(primer,",",segon,",",tercer)
                             else:
                                if(primer==segon>tercer<primer):
                                    print(tercer,",",primer,",",segon)
                                else: 
                                    if(primer<segon==tercer>primer):
                                        print(primer,",",segon,",",tercer)
                                    else:
                                        if(primer==segon>tercer):
                                            print(tercer,",",segon,",",primer)
                                        else: 
                                            if(primer>segon==tercer<primer):
                                                print(segon,",",tercer,",",primer)
                                            else:
                                                if(primer==tercer>segon<primer):
                                                    print(segon,",",primer,",",tercer)
                                                else:
                                                    if(primer==tercer<segon>primer):
                                                        print(primer,",",tercer,",",segon)
                                                    
                                            
