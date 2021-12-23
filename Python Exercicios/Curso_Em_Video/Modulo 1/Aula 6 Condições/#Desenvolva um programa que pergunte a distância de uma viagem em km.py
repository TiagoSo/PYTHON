#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 
# 200Km e R$0,45 parta viagens mais longas.

from time import sleep
print("Olá daqui é a companhia aérea TAP")
print("-=-" *11)
print("Qual é a distância da sua viagem em km")
d=float(input())
if (d <= 200):
    custo_viagem=d * 0.50
    print("A viagem custará",custo_viagem,"$.")
else :
    custo_viagem=d * 0.45
    print("A viagem custará",custo_viagem,"$.")
    
input("ENTER")