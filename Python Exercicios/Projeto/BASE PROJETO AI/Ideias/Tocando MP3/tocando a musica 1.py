import pygame
pygame.mixer.init()
pygame.mixer.music.load('1.mp3')
#pygame.mixer.music.__loader__('1.mp3')
pygame.mixer.music.play()

input()
pygame.event.wait()
