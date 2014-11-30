import random
import math

#Operaremos bajo el supuesto de que el tiempo se medira por turno, y de que una vez comenzado un turno, el proceso
# solo se acaba al final del turno.
shift_count = 6 #En esta variable se guarda la cantidad de turnos a contar (" aca va el input de los turnos")
TruckLoad = 0 #Carga sobrante entre turnos.
Packages = 0 #Cantidad de paquetes por turno.
Time_Off01 = 0 #Cantidad de tiempo que la maquina permanece sin uso
Time_Off02 = 0 #Cantidad de tiempo que la maquina permanece sin uso
Time_On01 = 0 #Cantidad de tiempo que la maquina se encuentra ocupada
Time_On02 = 0 #Cantidad de tiempo que la maquina se encuentra ocupada
while shift_count > 0:
	if shift_count > 0: #Primer turno
		Trucks = random.expovariate(20) #Obtengo cantidad de camniones por minuto usando distribucion exponencial.
		Trucks_shift = Trucks*480 #Dado que son turnos de 8 horas, se multiplica la distribucion por la cantidad de minutos en 8 horas
		Trucks_shift = math.ceil(Trucks_shift)
		Work_01 = 0 #cantidad de paquetes hechos por la primera maquina
		print(Trucks_shift)
		shift_count = 0