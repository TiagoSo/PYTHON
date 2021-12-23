#BIBLIOTECAS IMPORTADAS
from os import pipe
from typing import Text
import pygame,random
from time import sleep
import time
from random import choice
from pygame import display
pygame.init()
pygame.mixer.init()

#------------------------//--------------------------------------
#Mensagem Inicial Abertura     
final=""
print("")
print(("\033[34mOlá seja bem vindo ao MultiGames"),"\U0001F579")

# Perguntas usadas no (Jogo 1)
#Usamos um dicionário armazenar perguntas e a palavra chave da pergunta.
perguntas = {
'Pergunta 1':{
        'pergunta':"De que cidade são os Beatles?",
                'respostas':{
                        'a':'Manchester',
                        'b':'Londres',
                        'c':'Liverpool',},
                'resposta_certa':'c',
    },
        'Pergunta 2':{
                'pergunta':"Em que ano é que o Brasil foi descoberto??",
                        'respostas':{
                                'a':'1500',
                                'b':'1450',
                                'c':'100 a.c',},
                'resposta_certa':'a',
    },
        'Pergunta 3':{
                'pergunta':"Qual destas hipoteses não é um açucar?",
                        'respostas':{
                                'a':'Amidol',
                                'b':'Glicose',
                                'c':'Frutose',},
                'resposta_certa':'a',
        },
        'Pergunta 5':{
                'pergunta':"Quem foi o primeiro homem a orbitar a Terra?",
                        'respostas':{
                                'a':'John Glenn',
                                'b':'Sergei Korolev',
                                'c':'Yuri Gagarin',},
                'resposta_certa':'c',
        },
        'Pergunta 6':{
                'pergunta':"Em que cidade norte-americana morreu George Floyd em 2020, provocando uma onda de protestos mundiais?",
                        'respostas':{
                                'a':'Atlanta',
                                'b':'Minneapolis ',
                                'c':'Houston',},
                'resposta_certa':'b',
        
        },
        'Pergunta 7':{
                'pergunta':"A Bielorrussia nao faz fronteira com qual destes paises?",
                        'respostas':{
                                'a':'Letonia',
                                'b':'Eslovenia',
                                'c':'Lituania',},
                'resposta_certa':'b',
        },
        'Pergunta 8':{
                'pergunta':"A que familia animal pertencem as renas?",
                        'respostas':{
                                'a':'Cervideos',
                                'b':'Equideos ',
                                'c':'Anatideos',},
                'resposta_certa':'a',
        },
        'Pergunta 9':{
                'pergunta':"Qual das seguintes ilhas pertence ao arquipelago da Madeira?",
                        'respostas':{
                                'a':'Barreta',
                                'b':'Faial',
                                'c':'Deserta Grande ',},
                'resposta_certa':'c',
        },
        'Pergunta 10':{
                'pergunta':"Qual foi o primeiro ser vivo terrestre a orbitar o planeta Terra?",
                        'respostas':{
                                'a':'Cão ',
                                'b':'Homem',
                                'c':'Macaco',},
                'resposta_certa':'a',
        },
        'Pergunta 11':{
                'pergunta':"Qual dos seguintes é um excentrico e visionario empreendedor nascido na Africa do Sul?",
                        'respostas':{
                                'a':'Jeff Bezos',
                                'b':'Elon musk',
                                'c':'Tim cook',},
                'resposta_certa':'b',
        },
        'Pergunta 12':{
                'pergunta':"Qual era a deusa Grega do amor e da beleza?",
                        'respostas':{
                                'a':'Hera',
                                'b':'Afrodite',
                                'c':'Minerva',},
                'resposta_certa':'b',
        },
}

#--------------------------------//---------------------------------------

#-------------------------Menu do Programa-----------------------------------
while final != "sair" and final != "SAIR" and final != "S" and final != "s":
    print ("-=-" *13)
    print ("| 1  - Quem quer ser milionário 2.0    |")
    print ("| 2  - Pedra Papel e Tesoura           |")
    print ("| 3  - Jogo da Forca                   |")
    print ("-=-" *13)
    print ("| 4  -        SOBRE NÓS                |")
    print ("-=-" *13)
    
    print("           Selecione o jogo             ")
    opseleciona=int (input())
    
    #--------------------/Quem quer ser milionário 2.0/-------------------------
    if opseleciona == 1:
               

        print("Vamos jogar ao jogo do Quem quer ser milionário")
        print("")
        
        
        pygame.mixer.music.load('1.mp3') #Faz o load da Musica do ficheiro que está na pasta
        pygame.mixer.music.play()

        
        print("Senhores e Senhoras!!")
        print(" ")
        sleep(1.3)
        print("Seja bem vindo a primeira rodada de")
        print(" ")
        sleep(3.7)
        print("QUEM")
        sleep(3.7)
        print("QUER")
        sleep(2.7)
        print("SER")
        sleep(2.7)
        print("UM")
        sleep(3.7)
        print("MILLIONÁRIO?!")
        print("")
        sleep(3.0)
        print("E o primeiro canditado de hoje é...")
        nome=str(input()).strip()
        print(nome.upper(),"espero que esteja preparado para o desafio de hoje")
        pygame.mixer.music.load('2.mp3')
        sleep(3.0)
        print("UM APLAUSO PARA O NOSSO CANDITADO \U0001F44F")
        pygame.mixer.music.play()
        print()
        sleep(3.0)
        print("Esta edição, temos uma supressa para o nosso candidato.")
        sleep(3.0)
        print("Desta vez,cada pergunta vale 50€ e se você acertar mais de 9, ganha automaticamente 5000€, além de o número de acerto por pergunta.")
        sleep(3.0)
        print("Lembrando que são 12 perguntas, se não ganhará apenas 200€")
        sleep(3.0)
        print()

        
        #---------------------Acessando as Perguntas no dicionário criado-------------------------------------
        #---------------------(Desenvolvendo as funcionalidades do jogo)--------------------------------------
        dinheiro_conta=0     
        respostas_certas=0
        for chave_pergunta, chave_respostas in perguntas.items(): # Para acessar as perguntas(chave_pergunta) e a resposta das perguntas(no dicionário) usamos "for", e para a acessar o dicionario com essas variaveis usamos in perguntas(dicionário).itens para acessar;
                        print(f'{chave_pergunta}: {chave_respostas["pergunta"]}')
                        sleep(1.5)
                        print("Respostas:")
                        for respostas_pergunta, resposta_pergunta in chave_respostas['respostas'].items(): #f' permite-nos imprimir de uma só vez o texto. É benefico pois permite-nos adicionar variaveis diretamente, diretamente nas nossas string;
                                print(f'[{respostas_pergunta}]:{resposta_pergunta}')
                        resposta_usario= input("Sua resposta:")
                        if resposta_usario==chave_respostas["resposta_certa"]:
                                print("Ehhh!!!!Você acertou!!!!")
                                pygame.mixer.music.load('certo.mp3')
                                pygame.mixer.music.play()
                                respostas_certas +=1    #+ = adiciona 1 resposta certa a variável(respostas_certas),usamos para modificar logo a variável;
                                dinheiro_conta+=50
                                sleep(2.0)
                        elif resposta_usario!=chave_respostas["resposta_certa"]:
                                print("Errou, a resposta certa era",resposta_pergunta)
                                pygame.mixer.music.load('erro.mp3')
                                pygame.mixer.music.play()
                                sleep(2.0)
                                dinheiro_conta-=50
                              
                        print()

        print(f"Você acertou {respostas_certas} resposta.")# Busca a variavel respostas_certas e mostra em tempo real que o utilizador acertou aquela pergunta;
        if respostas_certas >=9:
                now=time.gmtime()
                print("Você ganhou o QUEM QUER SER MILIONÁRIO EDIÇÃO DE",now[0],".")#Diz o tempo(como dentro está [0], aparecerá o tempo(ano));
                soma=respostas_certas*100
                premio_final=5000
                sleep(2.0)
                print("O seu prémio é de",dinheiro_conta,"€, mais o prémeio final de",premio_final,"€")
                pygame.mixer.music.load('sourica.mp3')
                pygame.mixer.music.set_volume(6)
                pygame.mixer.music.play()
                sleep(2.0)

        elif respostas_certas <=9:
                
                print("Ohhhh, você ganhou apenas 200€")
                pygame.mixer.music.load('ohh.mp3')
                pygame.mixer.music.play()
                sleep(2.0)
               
        sleep(2)





    #--------------------/Pedra Papel e Tesoura/-------------------------    
    elif opseleciona ==2:

        from  random import randint
           
        print("Vamos jogar ao Pedra Papel e Tesoura")
        sleep(1)
        print("..."*12)
        pedra_papel_tesoura=('Pedra','Papel','Tesoura')
        pc = randint(0,2) #Gera um número aleatório entre (0-3) num  intervalo positivo
        print("""[Suas opções:]
[0] Pedra
[1] Papel
[2] Tesoura""")
        print()
        print("Qual é a sua jogada?")
        #-------------------/SOM/---------------------------
        pygame.mixer.music.load('pedrapapeltesoura.mp3')
        pygame.mixer.music.set_volume(5)
        pygame.mixer.music.play()
        #--------------------//---------------------------
        print("Pedra")
        sleep(1.0)
        print("Papel")
        sleep(1.0)
        print("Tesoura...")
        sleep(1.0)
        jogador= int(input())
        print("Computador jogou",pedra_papel_tesoura[pc])
        print("Jogador jogou",pedra_papel_tesoura[jogador])
        print("-=-"*10)
        if pc == 0:
                if jogador == 0:
                        print("EMPATE","\U0001F60E")
                elif jogador ==1:
                        print("VOCÊ VENCEU","\U0001F451")
                elif jogador ==2:
                        print("COMPUTADOR VENCEU","\U0001F631")
                else:
                        print("Jogada Invalida")
        elif pc == 1:
                if jogador ==0:
                        print("COMPUTADOR VENCEU")

                elif jogador ==1:
                        print("EMPATE","\U0001F60E")
                elif jogador ==2:
                        print("VOCÊ VENCEU","\U0001F451")
                else:
                        print("Jogada Invalida")
                        
        elif pc ==2:
                if jogador ==0:
                        print("VOCÊ VENCEU","\U0001F451")

                elif jogador ==1:
                        print("COMPUTADOR VENCEU","\U0001F631")
                elif jogador ==2:
                        print("EMPATE","\U0001F60E")
                else:
                        print("Jogada Invalida")
        print()
        input("Carregue ENTER para ir para o menu ")
            
        
   #----------------------/Jogo Da forca/---------------------------

    elif opseleciona ==3:
            #ESCOLHA DA FUNCIONALIDADE DA BIBLIOTECA RANDOM
            from random import choice
            
            #-------------------------------------------------//Configurando Definicões//------------------------------------------------------------------------
            vocabulario = ["astronauta","lua","sol","nasa","jupiter","foguete",",universo","cosmo","galaxia"]  #Lista com palavras relacionadas com a temática espacial          
            palavra = choice(vocabulario) #O programa escolhe dentro da lista [vocabulario] 1 palavra aleatório para as palavras surgidas ao utilizador não serem as mesmas. 

            #------------------------------------------------//Display ao utilizador//--------------------------------------------------------------------------
            print("-=-"*2,"Seja bem vindo ao JOGO DA FORCA","-=-"*2)
            print("Dica: Temática Espacial")
            print("Regra:Só 6 chances")
            sleep(0.5)
            print("Por isso, boa sorte...")

            #------------------------------------------------//Configurando Definicões//------------------------------------------------------------------------
            chances = 6
            alfabeto = list("abdcefghijklmnopqrstuvwxyz")# ou podiamos usar a função list()
            tentativas = [] # Armazenar as tentativas do usuário(põem a letra que está errada)
            
            while True:                         
                print(tentativas)
                print("Chances: ",chances)
                    
                for letra in palavra:                           #Laço for
                        if letra in tentativas:
                                print(letra, end = ' ')         #end = '' serve pra dizer que o print deve ser encerrado com um caractere de espaço em branco, e não com uma nova linha, como é o padrão no Python;
                        else:
                                print('_', end= ' ')
                        
                palpite = input("\nDigite seu palpite ou 'SAIR' para sair do programa!:").lower() #\n para quebra de linhas, e o .lower() para independentemente de o utilizador digitar letra Grande, ele escreve sempre letra pequena para não dar erro, pois nós só fizemos o alfabeto com letra pequena;
                if palpite == "sair":
                        break	
                elif palpite not in alfabeto or palpite == '':
                        print("Errado")
                        continue	
                elif palpite in tentativas:
                        print("Essa letra ja foi usada")
                        continue
                tentativas.append(palpite)
                if palpite in palavra:
                        print("Certo!")
                else:
                        print("Errado")
                        chances-=1
                if chances == 0:
                        print("Perdeu, Game over!!!)")
                        break
                elif set(palavra).issubset(set(tentativas)): #O método issubset () retorna True se todos os itens no conjunto existirem no conjunto especificado, caso contrário, retorna False;
                        print("Parabéns!!!!!")
                        sleep(2)
                        break
            sleep(2.0)
            
        #continue --> Serve para que o fluxo do programa seja interrompido no local do código onde o continue está inserido e volte para o início do laço
        # break ---> Encerra o laço while no local onde o comando se encontra
        # continue =! break
        #continue encerra "apenas" a repetição presente do loop, enquanto o break encerra o laço de vez
        #pass ---> "prossiga";pass é utilizado quando estamos no início de um projeto e queremos esquematizar as funções que utilizaremos, mas não pretendemos implementá-las ainda.

    elif opseleciona == 4 : 

        # --------------------//Criando uma INTERFACE com o título “Quem Somos?”//---------------------
         
         #---------------------//Janela//-------------------------
         janela = pygame.display.set_mode((770, 800))
         deve_continuar = True
         pygame.display.set_caption("Quem Somos?!")
         #---------------------------------------------------------
         
         #--------------------//COLORES USADAS//-------------------
         branco=[255,255,255]
         preto=[0,0,0]
         janela.fill(branco)
         #---------------------------------------------------------

         #---------------//FONTES E IMAGENS E TEXTO//--------------
         font_titulo = pygame.font.Font(None, 80)
         font=pygame.font.Font(None, 27)
         titulo = font.render("Quem Somos?",True,(49, 46, 240))
         texto= font.render("Olá, nós somos os criadores da empresa MULTIGAMES.",True,(240, 179, 12))
         texto_c=font.render("Somos uma empresa sem fins lucrativos, com o desejo de entreter as pessoas.",True,(240, 179, 12))
         texto_c_c=font.render("A nossa empresa fica situada em Sesimbra, e nós desenvolvedores  amamos música. ",True,(240, 179, 12))
         image = pygame.image.load('criadores.png')
         janela.blit(image,(0,0))
         #---------------------------------------------------------
         #-----------------------//Música//------------------------
         pygame.mixer.music.load('jajao.mp3')
         pygame.mixer.music.play()

         #----------------//Desenhando Linha//---------------------
         pygame.draw.line(janela,preto,(0,600),(800,600),9)
         #-------//Mostra na tela tudo o que foi desenhado//-------
         pygame.display.update()
         
         # ----------------//LOOP DO JOGO/JANELA//-----------------
         while deve_continuar:
                # Checando eventos
                for event in pygame.event.get(): 
                 pygame.mixer.music.play()      
                # Se for um evento QUIT
                 if event.type == pygame.QUIT:
                        deve_continuar = False
                        # Encerrando módulos de Pygame
                        pygame.quit()
         #-----------//ESCREVE E MOSTRA NA TELA//-----------       
                janela.blit(titulo,(317,605))
                janela.blit(texto,(15,640))
                janela.blit(texto_c,(15,660))
                janela.blit(texto_c_c,(15,680))
                pygame.display.flip()
                 
print ("Escreva sair ou s para terminar o programa:")
final = input()