print("Introduce una nota (0 a 10)")
nota = float(input())

if nota < 0 or nota > 10:
    print("Nota no válida")
else:
    if nota < 5:
        print("Insuficiente")
    elif nota < 6:
        print("Suficiente")
    elif nota < 7:
        print("Bien")
    elif nota < 8:
        print("Notable")
    elif nota < 9:
        print("Notable")
    else:
        print("Sobresaliente")
