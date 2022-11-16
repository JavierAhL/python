#Diseña un algoritmo y un diagrama de flujo para:
#Con la base y la altura de un rectángulo, se nos pide calcular su perímetro y
#su área

def rectangulo():
    base=float(input("Tamaño de la base:"))
    altura=float(input("Tamaño de la altura:"))

    perimetro=(base*2+altura*2)
    area=(base*altura)

    print(f"El perímetro es {perimetro}m y el area es {area}m2.")
rectangulo()
