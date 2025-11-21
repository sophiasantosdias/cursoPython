# Tocando um MP3
import pygame
print('====== DESAFIO 21 ======')
pygame.mixer.init()
pygame.init()
pygame.mixer_music.load('ex021.mp3')
pygame.mixer_music.play()
pygame.event.wait()
