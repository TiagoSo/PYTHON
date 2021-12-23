#Pintando a parede
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
print("Então sempre queres pintar a parede")
print("Então eu preciso das Medidas: 1ºAlturae 1º Largura ")
altura=float(input())
largura=float(input())
area=altura*largura
print("A area da sua parede é",area)
parede_pintada=area/2
print ("São precisos ",parede_pintada)
input("Carrege no ENTER para terminar")