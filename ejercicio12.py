entrada = input("Indroduce una secuencia de numeros separados por espacios")
numeros =[int(n) for n in entrada.split()]
suma_total = sum(numeros)
print("La suma total de los numeros es :", suma_total)