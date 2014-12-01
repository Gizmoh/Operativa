# -*- coding: utf-8 -*-
import random
import math

#Operaremos bajo el supuesto de que el tiempo se medira por turno, y de que una vez comenzado un turno, el proceso
#1° supuesto, la distribucion de los camiones se determina una vez y se usa para el turno entero, una por turno
#2° supuesto, el tiempo de compactacion de las maquina se calcula una vez por ciclo, y se cicla hasta que se acaba el turno / se acaban las cargas
#3° supuesto, al tercer turno no llegan camiones con carga.
#4° supuesto, un dia esta compuesto de tres turnos, los dias se trabajan en su totalidad.
# solo se acaba al final del turno.
shift_count = 500 #En esta variable se guarda la cantidad de turnos a contar (" aca va el input de los turnos")
shift_selector = 0 #determina que turno se ejecutara a continuacion.
shift_worked01 = 0 #Cantidad de turnos trabajados por maquina 1
shift_worked02 = 0 #Cantidad de turnos trabajados por maquina 2

TruckLoad = 0 #Carga sobrante entre turnos.
proLoad = 0 #Carga al principio del turno
Package01 = 0 #Cantidad de paquetes hechos por la primera maquina
Package02 = 0 #Cantidad de paquetes hechos por la segunda maquina
Packages = 0 #Cantidad de paquetes por turno.

Time_Off01 = 0 #Cantidad de tiempo que la maquina permanece sin uso
Time_Off02 = 0 #Cantidad de tiempo que la maquina permanece sin uso
Time_On01 = 0 #Cantidad de tiempo que la maquina se encuentra ocupada
Time_On02 = 0 #Cantidad de tiempo que la maquina se encuentra ocupada
		
def CreaCarga(TruckLoad):#Creamos los camiones que llegan ese turno
	Time = 0 #Inicializamos la variable en 0
	Trucks_shift = 0
	while Time < 480: #agregamos mas camiones al turno hasta que se completen los 480 minutos
		Time = Time + random.expovariate(2) #agregamos una cantidad de tiempo al azar a los minutos para simular la llegada de un camion
		Trucks_shift = Trucks_shift + 1 #agregamos un contador al contador de camiones
	Trucks_shift = math.ceil(Trucks_shift)
	Trucks_shift = Trucks_shift + TruckLoad #agregamos los camiones sobrantes del turno anterior a los camiones para este turno
	return Trucks_shift


def Machine01(carga):#Turno de la maquina 1
	global Package01
	global shift_worked01
	global Time_Off01
	time = 480
	while time > 0 and carga > 0:#Maquina opera mientras dure el turno o duren las cargas de los camiones, lo que se acabe primero
		time = time - random.normalvariate(12,5)
		carga = carga-1
		Package01 = Package01 + 1
	if time > 0: #Si el turno se termina por falta de cargas se suma el tiempo sobrante al tiempo desocupado
		Time_Off01 = Time_Off01 + time
		Time_On01 = 480 - time
	shift_worked01 = shift_worked01 + 1
	return carga

def Machine02(carga):#Turno de la maquina 2
	global Package02
	global shift_worked02
	global Time_Off02
	time = 480
	while time > 0 and carga > 0:#Maquina opera mientras dure el turno o duren las cargas de los camiones, lo que se acabe primero
		time = time - random.uniform(12,15)
		carga = carga - 2
		Package02 = Package02 + 1
	if time > 0: #Si el turno se termina por falta de cargas se suma el tiempo sobrante al tiempo desocupado
		Time_Off01 = time
		Time_On01 = 480 - time
	shift_worked02 = shift_worked02 + 1
	return carga


Package01 = 0
for i in range(0,shift_count): # el proceso funciona hasta pasar por todos los turnos introducidos
	if shift_selector == 0: #Turno de la primera maquina
		shift_selector = 1
		proLoad = CreaCarga(TruckLoad)
		TruckLoad = Machine01(proLoad)
	if shift_selector == 1: #Turno de la segunda maquina
		shift_selector = 2
		proLoad = CreaCarga(TruckLoad)
		TruckLoad = Machine02(proLoad)
	if shift_selector == 2: #Turno de descanso, no se hace nada, no llegan camiones.
		shift_selector = 0
Packages = Package01 + Package02
print ("Carga sobrante final = "+str(TruckLoad)+" cargas ; paquetes totales creados = "+str(Packages)+".")
print ("Tiempo desocupado promedio maquina 1 = "+str(Time_Off01/shift_worked01)+" minutos.")
print ("Tiempo desocupado promedio maquina 2 = "+str(Time_Off02/shift_worked02)+" minutos.")
print ("Paquetes creados maquina 2 = "+str(Package02)+".")