#Faça um Programa que leia algo pelo teclado e mostre na tela 
#o seu tipo primitivo e todas as informações sobre elas.

print("Digite algo")
algo_lido=input()
print ("O tipo primitivo desse valor é",type(algo_lido))
print("Só tem espaços",algo_lido.isspace())
print ("É um número?",algo_lido.isnumeric())
print("É alfabético",algo_lido.isalpha())
print("É alfanumerico",algo_lido.isalnum())
print("Está em maisculas? ",algo_lido.isupper())
print("Está em minusculas? ",algo_lido.islower())

#algo_lido é um objeto