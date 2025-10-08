print("=== FACTURA SIMPLE (sin listas) ===")

# 1) Pide N en 1..50 (usa while para validar)
while True:
    N = int(input("Número de líneas de la factura (1-50): "))
    if 1 <= N <= 50:
        break
    print("Error: debe estar entre 1 y 50.")

total_bruto = 0.0
baratas = medias = caras = 0
precio_min = None
precio_max = None

# 2) Recorre 1..N con for
for i in range(1, N + 1):
    # 2.a) Precio >= 0 (validar con while)
    while True:
        precio = float(input(f"Línea {i} - Precio unitario (€): "))
        if precio >= 0:
            break
        print("Error: el precio debe ser >= 0.")
    
    # 2.b) Cantidad >= 1 (validar con while)
    while True:
        cantidad = int(input(f"Línea {i} - Cantidad: "))
        if cantidad >= 1:
            break
        print("Error: la cantidad debe ser >= 1.")
    
    # 2.c) Clasifica el precio con if/elif/else y lleva contadores
    if precio < 5:
        baratas += 1
    elif precio <= 20:
        medias += 1
    else:
        caras += 1
    
    # 2.d) Actualiza min/max
    if precio_min is None or precio < precio_min:
        precio_min = precio
    if precio_max is None or precio > precio_max:
        precio_max = precio
    
    # 2.e) Acumula subtotal en total_bruto
    total_bruto += precio * cantidad

# 3) Tramos de descuento con if/elif/else
if total_bruto >= 100:
    porc_desc = 0.15
elif total_bruto >= 50:
    porc_desc = 0.10
elif total_bruto >= 20:
    porc_desc = 0.05
else:
    porc_desc = 0.0

# 4) Calcula descuento, base, iva y total
descuento = total_bruto * porc_desc
base_imponible = total_bruto - descuento
iva = base_imponible * 0.10
total = base_imponible + iva

# 5) Muestra resumen con 2 decimales
print("\n=== RESUMEN FACTURA ===")
print(f"Total bruto: {total_bruto:.2f} €")
print(f"Descuento: {descuento:.2f} €")
print(f"Base imponible: {base_imponible:.2f} €")
print(f"IVA (10%): {iva:.2f} €")
print(f"TOTAL: {total:.2f} €\n")

print("=== RESUMEN LÍNEAS ===")
print(f"Líneas baratas (<5€): {baratas}")
print(f"Líneas medias (5-20€): {medias}")
print(f"Líneas caras (>20€): {caras}")
print(f"Precio mínimo introducido: {precio_min:.2f} €")
print(f"Precio máximo introducido: {precio_max:.2f} €")
