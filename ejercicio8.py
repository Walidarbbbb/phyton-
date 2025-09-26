print("Introduce la primera nota")
nota1 = float(input())

print("Introduce la segunda nota")
nota2 = float(input())

print("Introduce la tercera nota")
nota3 = float(input())

if nota1 <= 4 and nota2 <= 4 and nota3 <= 4:
    print("La nota final es 0")
elif nota1 > 4 and nota2 > 4 and nota3 > 4:
    nota_final = (nota1 * 0.3) + (nota2 * 0.2) + (nota3 * 0.5)
    print("La nota final es", nota_final)
else:
    print("La nota final es 2")
