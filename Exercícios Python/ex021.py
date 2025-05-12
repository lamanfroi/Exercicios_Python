#Vou ficar devendo o mpe3 por preguiça, mas era para tocar um mp3 nesse programa

import pygame
pygame.init()
pygame.mixer.music.load('ex022.mp3')
pygame.mixer.music.play()
pygame.event.wait()