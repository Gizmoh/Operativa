import random

#Defino Variables:
Trucks = random.expovariate(20)
Trucks_shift = Trucks*480 #Dado que son turnos de 8 horas, se multiplica la distribucion por la cantidad de minutos en
#8 horas para obtener camiones por turno.
#Operaremos bajo el supuesto de que el tiempo se medira por turno, y de que una vez comenzado un turno, el proceso solo se acaba al final del turno.
shift_count = 6 #En esta variable se guarda la cantidad de turnos a contar (" aca va el input de los turnos")
while shift_count > 0:
	if shift_count > 0: #Primer turno
		print ("megadurr")
		shift_count = 0

