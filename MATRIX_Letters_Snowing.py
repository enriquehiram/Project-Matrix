import pygame  #importando pygame
import random

#Definiendo colores
NEGRO = (0, 0 , 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
CARACTERES = ("X", "x", "Y", "y", "Z", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "%", "=", "*", "+", "~", "°", "¬", "/")


pygame.init()  #initializating

dimensiones = (700, 700) #Haciendo la ventana
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("MATRIX?") #poniendole titulo
fuente = pygame.font.Font( None , 20) #fuente default , size 20 pts, 9 de ancho, 10 de alto
numero_caracteres = 50
columna = [] * numero_caracteres
posicion_caracteres = [] * numero_caracteres
lista_caracteres = [] * numero_caracteres

for i in range(numero_caracteres):
    x = random.randrange(0, 700)
    y = random.randrange(0, 700)
    posicion_caracteres.append([x, y])

    caracter_aleatorio = random.randrange(24)
    lista_caracteres.append(CARACTERES[caracter_aleatorio])

    columna.append(0)


hecho = False #Hasta que el usuario cierre la aplicacion.
reloj = pygame.time.Clock() #gestionar cuan rapido se actualiza la pantalla

#-----Bucle principal del programa------
while not hecho:

    for evento in pygame.event.get():   # El usuario hizo algo
        if evento.type == pygame.QUIT:  # si el usuario pincha sobre cerrar
            hecho = True                # Acabamos y salimos del bucle

    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERIAN IR ENCIMA DE ESTE COMENTARIO

    # TODA LA LOGICA DEL JUEGO DEBERIA IR DEBAJO DE ESTE COMENTARIO
    # TODA LA LOGICA DEL JUEGO DEBERIA IR ENCIMA DE ESTE COMENTARIO

    # EL CODIGO DE DIBUJO DEBERIA IR DEBAJO DE ESTE COMENTARIO
    # EL CODIGO DE DIBUJO DEBERIA IR ENCIMA DE ESTE COMENTARIO

    pantalla.fill(NEGRO) # Primero, limpia la pantalla con negro.

    for i in range(len(lista_caracteres)):
        # Dibuja el copo de nieve
        # pygame.draw.circle(pantalla, BLANCO, lista_nieve[i], 2) ejemplo
        columna [i] = fuente.render(lista_caracteres[i], True, BLANCO)
        pantalla.blit(columna [i], posicion_caracteres[i])
        posicion_caracteres[i][1] += 1  # Mueve el copo un pixel hacia abajo

        if posicion_caracteres[i][1] > 700:  # Si el copo ya se salió de la pantalla
            y = random.randrange(-50, -10)
            posicion_caracteres[i][1] = y
            x = random.randrange(0, 700)
            posicion_caracteres[i][0] = x

    pygame.display.flip() # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.

    reloj.tick(60) # Limita a 60 fotogramas por segundo (frames per second)
pygame.quit()
