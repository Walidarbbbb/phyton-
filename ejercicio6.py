print("Introduce tu edad")
edad = int(input())

if edad < 0 or edad > 120:
    print("Edad no válida")
elif edad < 18:
    print("Menor de edad")
else:
    print("Mayor de edad")
