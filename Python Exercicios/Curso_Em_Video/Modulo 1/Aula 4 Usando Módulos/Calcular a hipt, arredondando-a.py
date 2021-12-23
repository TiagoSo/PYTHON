#aça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa
#import math
#print("Digite 1º C.oposto e em 2º C.adjacente")
#c_oposto=float(input())
#c_adjacente=float(input())
#hipt=math.sqrt((c_oposto**2)+(c_adjacente**2))
#print("A hip é",hipt)

#ou
from math import hypot
print("Digite 1º C.oposto e em 2º C.adjacente")
c_oposto=float(input())
c_adjacente=float(input())
hi=hypot(c_adjacente,c_oposto)
print("A hip é",round(hi))