import pygame
import time
import random

pygame.font.init()
ancho_pantalla, alto_pantalla = 1000, 700
ventana = pygame.display.set_mode((ancho_pantalla, alto_pantalla)) #set_mode obtiene los ajustes predefinidos de pantalla
pygame.display.set_caption('Combate')

background = pygame.transform.scale(pygame.image.load("image/img.jpg"), (ancho_pantalla, alto_pantalla))
jugador_principal = pygame.transform.scale(pygame.image.load("image/personaje.png"),(150,200))
bala = []
enemigo1 = pygame.transform.scale(pygame.image.load("image/enemigo1.png"), (60,60))
enemigo2 = pygame.transform.scale(pygame.image.load("image/enemigo2.png"), (70,65))
enemigo3 = pygame.transform.scale(pygame.image.load("image/enemigo3.png"), (80,80))
bala1 = pygame.transform.rotate(pygame.image.load("image/bala1.png"), 90)
bala2 = pygame.transform.rotate(pygame.image.load("image/bala2.png"), 90)
bala3 = pygame.transform.rotate(pygame.image.load("image/bala3.png"), 90)

class Personaje:
    def __init__(self, ejex, ejey, vida = 100):
        self.ejex = ejex
        self.ejey = ejey
        self.vida = vida
        self.imagen_personaje = None
        self.disparo = None
        self.disparos = [] 
        self.enfriar = 0

    def dibujar_personaje(self, ventana):
        ventana.blit(self.imagen_personaje, (self.ejex, self.ejey))


class Jugador(Personaje): #SUPER CLASE ES PERSONAJE y SUBCLASE ES JUGADOR
    def __init__(self, ejex, ejey, vida=100):
        super().__init__(ejex, ejey, vida)  
        self.imagen_personaje = jugador_principal
        self.disparo = bala
        self.mask = pygame.mask.from_surface(self.imagen_personaje) #MASK es una máscara que permite conocer y evaluar las colisiones
        self.vida_maxima = vida

class Enemigo(Personaje):
    soldados_enemigos = {
        "enemigo1": (enemigo1, bala1),
        "enemigo2": (enemigo2, bala2),
        "enemigo3": (enemigo3, bala3),        
    }

    def __init__(self, ejex, ejey, soldado_enemigo, vida=100):
        super().__init__(ejex, ejey, vida)
        self.imagen_personaje, self.disparo = self.soldados_enemigos[soldado_enemigo]
        self.mask = pygame.mask.from_surface(self.imagen_personaje)

    def movimiento_enemigo(self, velocidad_enemigo): 
        self.ejex -= velocidad_enemigo
         




def main():
    fts = 60
    temporizador = pygame.time.Clock()
    arrancar = True
    Nivel = 1
    Vidas = 3
    texto_pantalla = pygame.font.SysFont("italic", 40, True, False )
    velocidad_jugador = 5
    jugador = Jugador(100,600)
    lista_enemigos = []
    velocidad_enemigo = 3
    oleada = 5 #cantidad de enemigos que aparecerán
    

    def actualizar():
        ventana.blit(background, (0,0))
        texto_vidas = texto_pantalla.render(f'Vidas: {Vidas}', True, (255,0,0))
        texto_nivel = texto_pantalla.render(f'Nivel: {Nivel}', True, (0,0,255))
        ventana.blit(texto_vidas, (10,10))
        ventana.blit(texto_nivel, (850,10))
        jugador.dibujar_personaje(ventana)
        for enemigo in lista_enemigos:
            enemigo.dibujar_personaje(ventana)

        pygame.display.update()
        

    while arrancar:
        temporizador.tick(fts)
        actualizar()
        if len (lista_enemigos)== 0:
            Nivel += 1
            oleada += 10
            for i in range(oleada):
                enemigo = Enemigo(random.randrange(ancho_pantalla +100, ancho_pantalla +1000),
                                  random.randrange(100, alto_pantalla -100), 
                                  random.choice(["enemigo1", "enemigo2", "enemigo3"]))
                lista_enemigos.append(enemigo)

                           
        for evento1 in pygame.event.get():
            if evento1.type == pygame.QUIT:
                arrancar = False
        teclas_activadas = pygame.key.get_pressed()
        if teclas_activadas[pygame.K_LEFT] and jugador.ejex-velocidad_jugador>0:
            jugador.ejex-=velocidad_jugador
        elif teclas_activadas[pygame.K_RIGHT] and jugador.ejex+velocidad_jugador+80<ancho_pantalla:
            jugador.ejex+=velocidad_jugador
        elif teclas_activadas[pygame.K_UP] and jugador.ejey-velocidad_jugador>0:
            jugador.ejey-=velocidad_jugador
        elif teclas_activadas[pygame.K_DOWN] and jugador.ejey+velocidad_jugador+80<alto_pantalla:
            jugador.ejey+=velocidad_jugador
        for enemigo in lista_enemigos:
            enemigo.movimiento_enemigo(velocidad_enemigo)
                       

if __name__ == '__main__':
    main()




