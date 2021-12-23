#vamos aprender operações com String no Python. 
# As principais operações que vamos aprender são o Fatiamento de String, 
# Análise com len(), count(), find(), transformações com replace(), 
# upper(), lower(), capitalize(), title(), strip(), junção com join().

# --Manipulando Cadeias de Texto--
# "Curso em video Pytho"= cadeia de texto=STRING


frase = "Curso em video python"
print(frase)

frase = "Curso em video python"
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15])
print(frase[3:13:2])#print(frase[3:13:2(pula a letra de 2 em 2)]
print(frase[::2])
print("""vamos aprender operações com String no Python. As principais operações que 
vamos aprender são o Fatiamento de String, Análise com len(), count(), 
find(), transformações com replace(), upper(), lower(), capitalize(),
 title(), strip(), junção com join().""")
#desta maneira ela faz a print de todo

print(frase.count("o")) #count conta o que estiver escrito no parantetiese
#neste caso conta vezes existe na frase "Curso em video python" a letra o.

print(frase.upper().count("o"))#contar a quantitade de o apatir da frase ~
#jogada para a letra maisculas

print(len(frase))#conta na frase o numero total de letras((os espaços tbm contam como letras))

print(len(frase.strip()))# conta a frase sem os espaços indesejados

print(frase.replace("python","Android"))#substitui o python por android

print(frase[0])#mostra-me a primeira letra da frase

frase=frase.replace("python","Android")

print("Curso" in frase)# mostra se "Curso " está na frase,, neste caso
#é verdadeiro, mas se fosse "curso", seria falso.
print(frase.find("video"))#este 9 siginfica neste caso que existe, se fosse
#-1 seria falso.

print(frase.split())# sepaara as letras

divido= frase.split()
print(divido[2][3])
