numero1 = int(raw_input("ingrese el primer numero"))
numero2 = int(raw_input("ingrese el segundo numero"))
numero3 = int(raw_input("ingrese el tercer numero"))


if numero1 > numero2:
    if numero2 > numero3:
        print ("Estan en desendente")
elif numero1 < numero2:
    if numero2 < numero3:
        print ("Estan en ascendente")
