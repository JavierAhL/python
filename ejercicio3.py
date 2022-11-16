#Se pide calcular la nota de tu examen tipo test.
    #Serán 20 preguntas
    #Las preguntas correctas sumarán 0,5
    #Las preguntas incorrectas restarán 0,25
    #Las preguntas sin contestar tendrán 0
#Datos de entrada
    #Respuesta de la pregunta
#Datos de salida
    #La nota total

def nota():
    acierto=int(input('Cuantas aciertas'))
    fallo=int(input('Cuantas fallas'))
    nada=int(input('Cuantas sin nada'))
    nota=(acierto*0.5)-(fallo*0.25)+(nada*0)
    print(nota)
nota()