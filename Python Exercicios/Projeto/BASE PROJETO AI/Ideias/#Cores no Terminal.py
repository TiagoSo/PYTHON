#Cores no Terminal
#Padrão ANSI (escaoe sequence)-->Terminal -- cor (código \033[m)
#\033[mstyle,text,back m

# Style:            text:   branco=30          background: 40=fundo branco
# nenhum (0)                vermelho =31                   41=fundo vermelho
# negrito/Bold (1)          verde=32                       42=fundo verde
# underline  (4)            amarelo=33                     43=fundo amarelo
#                           azul=34                        44=fundo azul
#                           cizento=37

#Nas preferências do aplicativo Terminal, você pode definir cores ANSI personalizadas 
# para azul, verde, amarelo, vermelho brilhante, etc., mas elas não alteram nada no Shell

print("\033[31mErrou, a resposta é...")
print("\033[32mErrou, a resposta é...")
print("\033[34mErrou, a resposta é...")
#print("\033[34;40mErrou, a resposta é...")
#print("\033[34;42mErrou, a resposta é...")
#print("\033[32mTeste 1 e ","\033[34mTeste 2")
#print("\033[40,31mErrou miserável")