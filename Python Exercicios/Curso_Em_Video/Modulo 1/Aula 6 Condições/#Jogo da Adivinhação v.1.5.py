#Jogo da Adivinhação v.1.0
#Escreva um programa que faça o computador “pensar” em um número inteiro 
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número 
# escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from time import sleep #o pc demora tempo a processar 
from random import randint
pc=randint(0,5) #randint gera numeros aleatórios entre o intervalo definido
print("-=-" *20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar... ")
print("-=-" *20)
print("Em que número eu pensei?")
jogar=int(input())
print("Processando...")
sleep(3)
if jogar==pc:
    print("Parabéns!! Você conseguio me vencer")
else:
    print("OHH, Eu ganhei e pensei no numero",pc,"e tu pensaste no",jogar)
