#Modulos são necessários para melhorar um programa
#Exemplo import "bebida", ele importa todas as bebibas
#se eu quiser algum em especifico como por exemplo uma coca-cola eu ponho
# from bebida import coca-cola

#Bibliotecas 
#math,(a função ceil arrendonda um valor para cima (nota:7.255--->7.3))
#      a floor arrendonda para baixo ( nota:7.255---->7)    


import math
from math import sqrt
print ("Digite um numero")
n=float(input())
raiz=sqrt(n)
print("A raiz quadrada é",raiz)
print("A raiz quadrada arrendondada para cima é",math.ceil(raiz))
print("A raiz quadrada arrendondada para baixo é",math.floor(raiz))

#E se eu quiser mais bibliotecas?
#Vou a python.org















#-----------------------------------------------------------------------------------------------------------------------
#Nessa aula, vamos aprender como utilizar módulos em Python utilizando 
# os comandos import e from/import no Python. 
# Veja como carregar bibliotecas de funções e utilizar vários 
# recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi.
