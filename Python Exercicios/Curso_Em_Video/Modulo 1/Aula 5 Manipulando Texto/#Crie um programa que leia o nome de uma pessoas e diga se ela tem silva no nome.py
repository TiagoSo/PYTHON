#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
#Função tira verifica os caracteres iniciais e finais contra um conjunto definido pelo usuário de caracteres, e exclui-los até correr em um personagem não- correspondência

print("Qual é o seu nome")
nome=str(input().strip())
print("O seu nome tem silva?",("silva" in nome.lower()))
