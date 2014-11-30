import random

#Defino Variables:
Camiones = random.expovariate(20)
Camiones_turno = Camiones*480 #Dado que son turno de 8 horas, se multiplica la distribucion por la cantidad de minutos en
#8 horas para obtener camiones por turno.
print(Camiones_turno)