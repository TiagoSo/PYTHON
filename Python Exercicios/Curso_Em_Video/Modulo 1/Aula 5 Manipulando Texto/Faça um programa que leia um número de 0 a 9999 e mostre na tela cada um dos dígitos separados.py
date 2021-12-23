#Faça um programa que leia um número de 0 a 9999 e mostre na tela 
# cada um dos dígitos separados

print("Digite o numero")
num=int(input())
n=str(num)
print("Analisando o número")
print("Unidade:",n[3])
print("Dezena:",n[2])
print("Centena:",n[1])
print("Milhar:",n[0])
