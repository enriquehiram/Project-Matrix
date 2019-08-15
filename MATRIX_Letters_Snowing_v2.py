'''

'''

import pygame
import random

# -------- MAIN VARIABLES USED ---------
NEGRO = (0, 0 , 0)
BLANCO = (255, 255, 255)
TRANSICION_INICIAL = (118, 245, 136)
VERDE = (51, 242, 79)
TRANSICION_MEDIA = (27, 140, 43)
TRANSICION_FINAL = (15, 69, 23)
CARACTERES = ("X", "C", "Y", "S", "Z", "O", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "?", "=", "*", "^", "/", "°", "\\", "#", "<", ">", "G", "L", "D", "V")
delta_y = 10
delta_x = 11
total_pixeles_x = 60
total_pixeles_y = 80
numero_columnas = total_pixeles_x // delta_x # 5
numero_filas = total_pixeles_y // delta_y #  8
filas_extra = numero_filas // 2 # 4
core_info = [] # variable para definir posiciones, letras y demás
columna_impresa = [" "] * (numero_filas + filas_extra) * numero_columnas # 60
input_porcentaje = 0.05 # 2
porcentaje_columnas = int(round((numero_columnas * filas_extra * input_porcentaje), 0))
columna_azar = [" "] * numero_columnas # 5


for j in range (numero_filas + filas_extra): # Genera espacios para cada posible coordena
    for i in range (numero_columnas):  # Con este loop  generamos las coordenas de la primera linea para imprimir sin sobreponerse
        core_info.append([(0, -10), " ", (0, 0, 0)])

for i in range (porcentaje_columnas):
     y = random.randrange(-(filas_extra) , -1) * delta_y
     x = random.randrange(numero_columnas) * delta_x
#     columna_impresa[i] = CARACTERES [random.randrange(len(CARACTERES))]
     core_info [i][0] = [x,y]
     core_info [i][2] = BLANCO

# --------- INITIALIZATING --------
pygame.init()

dimensiones = ( total_pixeles_x, total_pixeles_y )  # Making the Windows where The Matrix will run
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("MATRIX running V.0.6")
fuente = pygame.font.Font( None , 20) #fuente default , size 20 pts, 9 de ancho, 10 de alto

hecho = False   # Until user close the application
reloj = pygame.time.Clock()   # Controlling how quick Window is updated

# -------- PROGRAM MAIN BUCLE --------
while not hecho:

    for evento in pygame.event.get():   # El usuario hizo algo
        if evento.type == pygame.QUIT:  # si el usuario pincha sobre cerrar
            hecho = True                # Acabamos y salimos del bucle

    # EL CODIGO DE  MATRIX SHELL INICIA AQUI
    pantalla.fill(NEGRO) # Primero, limpia la pantalla con negro.


#    for i in range (len(core_info), numero_columnas, -1):
#        columna_impresa[i-1] = columna_impresa[i-numero_columnas]
#        core_info[i-1][3] = NEGRO

    #Ciclo para renderizar todos los caracteres anteriores en color verde
#    for i in range (len(core_info)):
#        core_info[i][2] = VERDE

    #Ciclo for para  seleccionar y renderizar lo nuevo en letras blancas
    for i in range (porcentaje_columnas): # El for es porque son mas de una columna
#        columna_azar[i] = random.randrange(numero_columnas) # selecciona el # para una columna al azar
        caracter_aleatorio = random.randrange(len(CARACTERES)) # Selecciona un # para caracter aleatorio
        columna_impresa [i] = CARACTERES [caracter_aleatorio] # asigna el caracter a la columna
        core_info [i] [2] = BLANCO

        for j in range (len(core_info)):
            core_info [j][1] = fuente.render(columna_impresa[j] , True, core_info[j][2])
            pantalla.blit(core_info [j][1], core_info [j][0])

        core_info [i][0][1] += delta_y

        if core_info [i][0][1] > total_pixeles_y:
            y = random.randrange(-(filas_extra) , -1) * delta_y
            x = random.randrange(numero_columnas) * delta_x
            core_info [i][0] = [x,y]

    pygame.display.flip() # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    #pygame.time.wait(500)
    reloj.tick(2) # Limita a 60 fotogramas por segundo (frames per second)
pygame.quit()
