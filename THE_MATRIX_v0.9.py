'''
Cambio de estrategia. Mejor lo que cambia es la coordena
Tal como el archivo MATRIX_Letter_Snowing_v2.py
'''
# Coding: UTF-8
import pygame
import random

# -------- MAIN VARIABLES USED ---------
NEGRO = (0, 0 , 0)
BLANCO = (255, 255, 255)
TRANSICION_INICIAL = (118, 245, 136)
VERDE = (51, 242, 79)
TRANSICION_MEDIA = (27, 140, 43)
TRANSICION_FINAL = (15, 69, 23)
CARACTERES = ("X", "C", "Y", "S", "Z", "O", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "?", "=", "\\", "#", "<", ">", "G", "L", "D", "V")
# CARACTERES = ("X", chr(0x30AF))
DELTA_Y = 10
DELTA_X = 11
TOTAL_PIXELES_X = 60
TOTAL_PIXELES_Y = 120
NUMERO_COLUMNAS = TOTAL_PIXELES_X // DELTA_X # 5
NUMERO_FILAS = TOTAL_PIXELES_Y // DELTA_Y #  12
FILAS_EXTRA = NUMERO_FILAS // 2 # 6
core_info = [] # variable para definir posiciones:(x, y)--> core_info[N][0], caracter --> core_info[N][1], color --> core_info [N][2] y permanencia core_info [N][3]
columna_impresa = [" "] * (NUMERO_FILAS + FILAS_EXTRA) * NUMERO_COLUMNAS # 90, Esta variable se usa para preparar las letras antes de imprimir
INPUT_PORCENTAJE = 0.1 # 2
porcentaje_columnas = int(round((NUMERO_COLUMNAS * FILAS_EXTRA * INPUT_PORCENTAJE), 0)) # 3
columna_azar = [" "] * NUMERO_COLUMNAS # 3

# Este for sirve para popular todos los campos de la lista con una sola posición PERO VACIAS Y EN COLOR NEGRO
for j in range (NUMERO_FILAS + FILAS_EXTRA): # Genera espacios para cada posible coordena
	for i in range (NUMERO_COLUMNAS):  # Con este loop  generamos las coordenas de la primera linea para imprimir sin sobreponerse
		core_info.append([[0, -10], " ", [0, 0, 0],0])

def inicio_de_cadenas():		
	"""Funcion que asigna las informacion de las columnas cascada nuevas (letras blancas)"""
	for i in range (porcentaje_columnas):
		y = random.randrange(-(FILAS_EXTRA) , -1) * DELTA_Y
		x = random.randrange(NUMERO_COLUMNAS) * DELTA_X
		core_info [i][0] = [x,y]
		core_info [i][2] = BLANCO
		core_info [i][3] = 10
	for i in range (porcentaje_columnas-1):
		if core_info [i][0][0] == core_info [i+1][0][0]:
			x = random.randrange(NUMERO_COLUMNAS) * DELTA_X
			core_info [i+1][0][0] = x
	for i in range (porcentaje_columnas-1):
		if core_info [i][0][1] == core_info [i+1][0][1]:
			y = random.randrange(-(FILAS_EXTRA) , -1) * DELTA_Y
			core_info [i+1][0][1] = y

# --------- INITIALIZING --------
pygame.init()

dimensiones = ( TOTAL_PIXELES_X, TOTAL_PIXELES_Y )  # Making the Windows where The Matrix will run
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("MATRIX running V.0.9")
fuente = pygame.font.Font( None , 20) #fuente default , size 20 pts, 9 de ancho, 10 de alto

hecho = False   # Until user close the application
reloj = pygame.time.Clock()   # Controlling how quick Window is updated
inicio_de_cadenas()
# -------- PROGRAM MAIN BUCLE --------
while not hecho:

	for evento in pygame.event.get():   # El usuario hizo algo
		if evento.type == pygame.QUIT:  # si el usuario pincha sobre cerrar
			hecho = True                # Acabamos y salimos del bucle

    # EL CODIGO DE  MATRIX SHELL INICIA AQUI
	pantalla.fill(NEGRO) # Primero, limpia la pantalla con negro.

	for i in range (porcentaje_columnas): # El for es porque son mas de una columna
		caracter_aleatorio = random.randrange(len(CARACTERES)) # Selecciona un # para caracter aleatorio
		columna_impresa [i] = CARACTERES [caracter_aleatorio] # asigna el caracter a la columna		
		core_info [i][0][1] += DELTA_Y	
	

	for j in range (porcentaje_columnas,(len(core_info)),1):	
		for i in range (porcentaje_columnas):	
			if core_info [i][3] == 10 and core_info [j][3] == 0:
				core_info [i] [3] = 50
				core_info [j] = core_info [i]
				core_info [j] [2] = VERDE
				core_info [j] [3] =+ 10
	
	for i in range (porcentaje_columnas): # El for es porque son mas de una columna
		if core_info [i][0][1] > (TOTAL_PIXELES_Y * 1.3):
			inicio_de_cadenas()

	for j in range (len(core_info)):
		core_info [j][1] = fuente.render(columna_impresa[j] , True, core_info[j][2])
		pantalla.blit(core_info [j][1], core_info [j][0])

	pygame.display.flip() # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    #pygame.time.wait(500)
	reloj.tick(2) # Limita a 60 fotogramas por segundo (frames per second)
pygame.quit()
