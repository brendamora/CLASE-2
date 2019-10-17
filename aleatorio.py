import random
lista = []

while len(lista) < 3:
    digito = random.randint(0, 9)
    if digito not in lista:
        lista.append(digito)

print (lista)

while True:
    intento = raw_input ("Ingrese una lista")
    pica = 0
    fija = 0
    usuario = []
    for i in intento:
        if i not in usuario:
            usuario.append(int(i))

    if len(usuario) != len(lista):
        print("intento no valido")
    else:
        for j in lista:
            if j in usuario:
                if lista.index (j) == usuario.index (j):
                    fija +=1
                else:
                    pica +=1
        print ("pica: " + str(pica) + " y fija" + str(fija))
        if fija == 3:
            break
    

"""comparacion entre lista por posicion. ciclo que recorra los
elementos (pica y fija)"""



