#Sorteando um item na lista
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
print("Digite o nome dos 4 alunos")
n_1=str(input())
n_2=str(input())
n_3=str(input())
n_4=str(input())
lista=[n_1,n_2,n_3,n_4]
escolhido=random.choice(lista)
print("Escolhido é",escolhido)
input()



#random.choice escolhe apenas um numero
#compras=[pao, arrpz, leite]