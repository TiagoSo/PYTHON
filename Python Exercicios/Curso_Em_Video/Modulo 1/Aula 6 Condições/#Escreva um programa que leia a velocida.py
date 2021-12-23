#Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite

from time import sleep

print("Olá agente, escreva a velocidade do carro registrada")
v=float(input())
print("Aguarde...")
sleep(2)
if v>=80:
    print("MULTADO! O condutor passou do limite da velocidade permitido que é de 80Km/h")
    multa=v*7.00
    print("A multa é de",multa,"€")
else:
    print("O condutor está entre a velocidade permitida")

input("Carregue no ENTER para terminar")