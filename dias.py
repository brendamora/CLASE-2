dia = int(raw_input("ingrese el numero a validar"))

dias = ("domingo" , "lunes" , "martes" , "miercoles" , "jueves" , "viernes" , "de farra")

if numero < 1 or numero > 7:
    print ("el numero no es un dia valido")
else:
    print ("el numero corresponde a 2" + dias [numero - 1])
    
           
