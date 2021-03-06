#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
from main_ui import Ui_MainWindow
from PySide import QtCore, QtGui
import random
import math

class MainWindow(QtGui.QMainWindow):

	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.set_listeners()
	
		self.shift_selector = 0 #determina que turno se ejecutara a continuacion.
		self.shift_worked01 = 0 #Cantidad de turnos trabajados por maquina 1
		self.shift_worked02 = 0 #Cantidad de turnos trabajados por maquina 2

		self.TruckLoad = 0 #Carga sobrante entre turnos.
		self.proLoad = 0 #Carga al principio del turno
		self.Package01 = 0 #Cantidad de paquetes hechos por la primera maquina
		self.Package02 = 0 #Cantidad de paquetes hechos por la segunda maquina
		self.Packages = 0 #Cantidad de paquetes por turno.

		self.Time_Off01 = 0 #Cantidad de tiempo que la maquina permanece sin uso
		self.Time_Off02 = 0 #Cantidad de tiempo que la maquina permanece sin uso
		self.Time_On01 = 0 #Cantidad de tiempo que la maquina se encuentra ocupada
		self.Time_On02 = 0 #Cantidad de tiempo que la maquina se encuentra ocupada

		self.totalTime01 = 0
		self.totalTime02 = 0

	def about(self):
		"""
		Ventana con los integrantes del grupo
		"""
		message = u'Simulador realizado para el ramo de Investigación Operativa II \n\
		\nIntegrantes: \n- Nicolas Aravena\n- Hernan Casanova\n- Arturo Reyes\n\
		\nProfesor responsable: \n - Miguelina Vega Rosales\n'
		self.ui.about = QtGui.QMessageBox.information(self, 'Acerca de Simulador', message)


	def set_listeners(self):
		"""
		Se inicializan los listeners
		"""
		self.ui.aboutUs.triggered.connect(self.about)
		self.ui.simulate.clicked.connect(self.simulate)


	def CreaCarga(self, TruckLoad):
		"""
		Creamos los camiones que llegan ese turno
		"""
		Time = 0 #Inicializamos la variable en 0
		Trucks_shift = 0
		while Time < 480: #agregamos mas camiones al turno hasta que se completen los 480 minutos
			rand = random.expovariate(0.05)
			Time += rand #agregamos una cantidad de tiempo al azar a los minutos para simular la llegada de un camion
			Trucks_shift += 1 #agregamos un contador al contador de camiones
			#print "rand carga", rand
		Trucks_shift = math.ceil(Trucks_shift)
		Trucks_shift += self.TruckLoad #agregamos los camiones sobrantes del turno anterior a los camiones para este turno
		return Trucks_shift


	def Machine01(self, carga):
		"""
		Proceso de la maquina 1 equivalente a 1 turno
		"""
		time = 480
		self.totalTime01 += time
		while time > 0 and carga > 0:#Maquina opera mientras dure el turno o duren las cargas de los camiones, lo que se acabe primero
			rand = random.normalvariate(12,5)
			if rand < 0:
				rand *= (-1)
			time -= rand
			#print "rand mq1", rand
			carga -= 1
			self.Package01 += 1
		if time > 0: #Si el turno se termina por falta de cargas se suma el tiempo sobrante al tiempo desocupado
			self.Time_Off01 += time
			self.Time_On01 += (480 - time)
		else:
			self.Time_On01 += 480
		self.shift_worked01 += 1
		return carga


	def Machine02(self, carga):
		"""
		Proceso de la maquina 2 equivalente a 1 turno
		"""
		time = 480
		self.totalTime02 += time
		while time > 0 and carga > 0:#Maquina opera mientras dure el turno o duren las cargas de los camiones, lo que se acabe primero
			rand = random.uniform(12,15)
			if rand < 0:
				rand *= (-1)
			time -= rand
			carga -= 2
			self.Package02 += 1
			#print "rand MQ2", rand
		if time > 0: #Si el turno se termina por falta de cargas se suma el tiempo sobrante al tiempo desocupado
			self.Time_Off02 += time
			self.Time_On02 += (480 - time)
		else:
			self.Time_On02 += 480
		self.shift_worked02 += 1
		return carga

	def simulate(self):
		"""
		Simulacion realizada por el usuario
		"""
		self.resetValues()
		shift_count = self.ui.shifts.value() #En esta variable se guarda la cantidad de turnos a contar
		for i in range(0,shift_count): # el proceso funciona hasta pasar por todos los turnos introducidos
			if self.shift_selector == 0: #Turno de la primera maquina
				self.shift_selector = 1
				self.proLoad = self.CreaCarga(self.TruckLoad)
				self.TruckLoad = self.Machine01(self.proLoad)
			elif self.shift_selector == 1: #Turno de la segunda maquina
				self.shift_selector = 2
				self.proLoad = self.CreaCarga(self.TruckLoad)
				self.TruckLoad = self.Machine02(self.proLoad)
			elif self.shift_selector == 2: #Turno de descanso, no se hace nada, no llegan camiones.
				self.shift_selector = 0
		self.Packages = self.Package01 + self.Package02
		if shift_count > 1:
			message = u'Paquetes totales creados: {0}\
					\nPaquetes creados máquina 1: {1}\
					\nPaquetes creados máquina 2: {2}\
					\n----------------------\
					\nTiempo promedio trabajado máquina 1: {3} minutos\
					\nTiempo promedio trabajado máquina 2: {4} minutos\
					\n----------------------\
					\nTiempo promedio desocupado máquina 1: {5} minutos\
					\nTiempo promedio desocupado máquina 2: {6} minutos\
					\n----------------------\
					\nPorcentaje tiempo desocupado promedio máquina 1: {7}%\
					\nPorcentaje tiempo desocupado promedio máquina 2: {8}%\
					'.format(
						self.Packages, #total paquetes
						self.Package01, #paquetes mq 1
						self.Package02, #paquetes mq 2
						round(self.Time_On01/self.shift_worked01,3),
						round(self.Time_On02/self.shift_worked02,3),
						round(self.Time_Off01/self.shift_worked01,3), #tiempo mq 1
						round(self.Time_Off02/self.shift_worked02,3), #tiempo mq 2
						round(self.Time_Off01*100/self.totalTime01,3), #porcentaje mq1
						round(self.Time_Off02*100/self.totalTime02,3), #porcentaje mq2
						)
		else:
			message = u'Paquetes totales creados: {0}\
					\nPaquetes creados maquina 1: {1}\
					\nPaquetes creados maquina 2: {2}\
					\n----------------------\
					\nTiempo promedio trabajado máquina 1: {5} minutos\
					\nTiempo promedio trabajado máquina 2: 0 minutos\
					\n----------------------\
					\nTiempo promedio desocupado máquina 1: {3} minutos\
					\nTiempo promedio desocupado máquina 2: 0 minutos\
					\n----------------------\
					\nPorcentaje tiempo desocupado promedio máquina 1: {4}%\
					\nPorcentaje tiempo desocupado promedio máquina 2: 0%\
					'.format(
						self.Packages, #total paquetes
						self.Package01, #paquetes mq 1
						self.Package02, #paquetes mq 2
						round(self.Time_Off01/self.shift_worked01,3), #tiempo mq 1
						round(self.Time_Off01*100/self.totalTime01,3), #porcentaje mq1
						round(self.Time_On01/self.shift_worked01,3),
						)
		self.ui.results.setText(message)

	def resetValues(self):
		"""
		Se reinician los valores para una nueva simulación
		"""
		self.shift_selector = 0
		self.shift_worked01 = 0
		self.shift_worked02 = 0
		self.TruckLoad = 0
		self.proLoad = 0
		self.Package01 = 0
		self.Package02 = 0
		self.Packages = 0
		self.Time_Off01 = 0
		self.Time_Off02 = 0
		self.Time_On01 = 0
		self.Time_On02 = 0
		self.totalTimeOff01 = 0
		self.totalTimeOff02 = 0
		self.totalTimeOn01 = 0
		self.totalTimeOn02 = 0
		self.totalTime01 = 0
		self.totalTime02 = 0


def main():
	app = QtGui.QApplication(sys.argv)
	main = MainWindow()
	main.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()