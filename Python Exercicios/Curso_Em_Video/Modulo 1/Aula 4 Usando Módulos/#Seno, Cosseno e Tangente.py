#Seno, Cosseno e Tangente
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import cos, sin, tan, radians
print("Digite o ângulo")
an=float(input())
seno=sin(radians(an))
print("O angulo",an,"tem Seno de",seno)
cosseno=cos(radians(an))
print("O angulo",an,"tem Cosseno de",cosseno)
tangente=tan(radians(an))
print("O angulo",an,"tem Cosseno tangente",tangente)
input()