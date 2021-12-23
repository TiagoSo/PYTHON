
import pygame, random





pygame.mixer.init()
pygame.mixer.music.load('1.mp3')
pygame.mixer.music.play()

print("Digite o nome dos 4 alunos")
n_1=str(input())
n_2=str(input())
n_3=str(input())
n_4=str(input())
lista=[n_1,n_2,n_3,n_4]
escolhido=random.choice(lista)
print("Escolhido é",escolhido)


input("Enter")
pygame.event.wait()


