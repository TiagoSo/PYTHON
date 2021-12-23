# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

print("Digite um numero inteiro para ver se ele é PAR ou ÍMPAR")
n=int(input())
resultado=n%2 # se for n%2 ==0 é par se for 1 é impar
if resultado==0:
    print("O número é PAR")
else:
    print("O número é impar")