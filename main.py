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
		Sets up button listeners
		"""
		self.ui.aboutUs.triggered.connect(self.about)
		self.ui.simulate.clicked.connect(self.simulate)


	def CreaCarga(self, TruckLoad):#Creamos los camiones que llegan ese turno
		Time = 0 #Inicializamos la variable en 0
		Trucks_shift = 0
		while Time < 480: #agregamos mas camiones al turno hasta que se completen los 480 minutos
			Time = Time + random.expovariate(0.05) #agregamos una cantidad de tiempo al azar a los minutos para simular la llegada de un camion
			Trucks_shift = Trucks_shift + 1 #agregamos un contador al contador de camiones
		Trucks_shift = math.ceil(Trucks_shift)
		Trucks_shift = Trucks_shift + self.TruckLoad #agregamos los camiones sobrantes del turno anterior a los camiones para este turno
		return Trucks_shift


	def Machine01(self, carga):#Turno de la maquina 1
		time = 480
		while time > 0 and carga > 0:#Maquina opera mientras dure el turno o duren las cargas de los camiones, lo que se acabe primero
			time = time - random.normalvariate(12,5)
			carga = carga-1
			self.Package01 = self.Package01 + 1
		if time > 0: #Si el turno se termina por falta de cargas se suma el tiempo sobrante al tiempo desocupado
			self.Time_Off01 = self.Time_Off01 + time
			self.Time_On01 = 480 - time
		self.shift_worked01 = self.shift_worked01 + 1
		return carga


	def Machine02(self, carga):#Turno de la maquina 2
		time = 480
		while time > 0 and carga > 0:#Maquina opera mientras dure el turno o duren las cargas de los camiones, lo que se acabe primero
			time = time - random.uniform(12,15)
			carga = carga - 2
			self.Package02 = self.Package02 + 1
		if time > 0: #Si el turno se termina por falta de cargas se suma el tiempo sobrante al tiempo desocupado
			self.Time_Off01 = time
			self.Time_On01 = 480 - time
		self.shift_worked02 = self.shift_worked02 + 1
		return carga

	def simulate(self):
		shift_count = self.ui.shifts.value() #En esta variable se guarda la cantidad de turnos a contar (" aca va el input de los turnos")
		for i in range(0,shift_count): # el proceso funciona hasta pasar por todos los turnos introducidos
			if self.shift_selector == 0: #Turno de la primera maquina
				self.shift_selector = 1
				self.proLoad = self.CreaCarga(self.TruckLoad)
				self.TruckLoad = self.Machine01(self.proLoad)
			if self.shift_selector == 1: #Turno de la segunda maquina
				self.shift_selector = 2
				self.proLoad = self.CreaCarga(self.TruckLoad)
				self.TruckLoad = self.Machine02(self.proLoad)
			if self.shift_selector == 2: #Turno de descanso, no se hace nada, no llegan camiones.
				self.shift_selector = 0
		self.Packages = self.Package01 + self.Package02
		message = u'Carga sobrante final = {0}  cargas\
					\nPaquetes totales creados = {1}\
					\nPaquetes creados maquina 2 = {2}.\
					\nPaquetes creados maquina 2 = {3}.\
					\nTiempo desocupado promedio maquina 1 = {4} minutos.\
					\nTiempo desocupado promedio maquina 2 = {5} minutos.\
					\nPorcentaje tiempo desocupado promedio maquina 1 = {6}%\
					\nPorcentaje tiempo desocupado promedio maquina 2 = {7}%\
					'.format(
						self.TruckLoad, #Carga sobrante
						self.Packages, #total paquetes
						self.Package01, #paquetes mq 1
						self.Package02, #paquetes mq 2
						str(self.Time_Off01/self.shift_worked01), #tiempo mq 1
						str(self.Time_Off02/self.shift_worked02), #tiempo mq 2
						str(self.Time_Off01*100/self.Time_On01), #porcentaje mq1
						str(self.Time_Off02*100/self.Time_On02), #porcentaje mq2
						)
		self.ui.results.setText(message)


def main():
	app = QtGui.QApplication(sys.argv)
	main = MainWindow()
	main.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()