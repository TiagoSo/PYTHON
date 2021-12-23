#Aluguel de carros
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print ("Olá informe os dias em que teve com o o carro ")
n_dias=int(input())
print("Quantos KM andou com o carro?")
km_carro=float(input())
preco_pagar=((60*n_dias)+(km_carro*0.15))
print("O preço a pagar é",preco_pagar)
input("Carregue no ENTER para terminar a operação")



