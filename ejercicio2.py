#La nota del trimestre está basada en
#• Nota hito individual = 30 %
#• Nota hito grupal = 20 %
#• Nota examen = 50 %

#Datos de entrada
    #Nota en el hito individual
    #Nota en el hito grupal
    #Nota en el examen

#Datos de salida
    #Nota total
E=int(input("Dime la nota del examen"))
I=int(input("Dime la nota del hito individual"))
G=int(input("Dime la nota del hito grupal"))
notas=((E*0.50) + (I*0.30) + (G*0.20))
print(f'la nota media es {notas}')