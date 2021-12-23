
listaQuestoes = [{'pergunta': {'Pergunta 1': {'pergunta': 'cor do carro', 'respostas': {'a': 'branca', 'b': 'preto', 'c': 'cinza', 'd': 'prata', 'e': 'vermelho'}, 'resposta_certa': 'marca'}, 'Pergunta 2': {'pergunta': 'fiat', 'respostas': {'a': 'fiat', 'b': 'chevrolet', 'c': 'volkswage', 'd': 'volvo', 'e': 'celta'}, 'resposta_certa': 'c'}}},
                 {'pergunta2': {'Pergunta 1': {'pergunta': 'cor do carro', 'respostas': {'a': 'ciano', 'b': 'violeta', 'c': 'roxa', 'd': 'marrom', 'e': 'amarela'}, 'resposta_certa': 'd'}, 'Pergunta 2': {'pergunta': 'nome do carro', 'respostas': {'a': 'celta', 'b': 'corsa', 'c': 'camaro', 'd': 'gol', 'e': 'golf'}, 'resposta_certa': 'd'}}}]

titulo = ''
perguntas = None
for d in listaQuestoes: # para cada elemento em listaQuestoes
    # "d", no caso, será o dicionário que contém a chave "carro", depois o que tem a chave "carro2"...
    if titulo in d: # se o titulo é chave do dicionário
        perguntas = d[titulo] # pega o dicionário interno (o que tem as chaves "Pergunta 1" e "Pergunta 2")
        break # se já encontrei o que queria, posso interromper o loop




if perguntas: # se encontrou o titulo
    print(f'Perguntas para {titulo}')
    respostasCertas = 0
    for numero, dados in perguntas.items():
        print(f'{numero} - {dados["pergunta"]}\nEscolha uma das opções: ')
        for opcao, resp in dados["respostas"].items():
            print(f'[{opcao}]: {resp}')
        respostaUsuario = input('Sua resposta:')
        if respostaUsuario == dados['resposta_certa']:
            print('Muito bem! Você acertou.')
            respostasCertas += 1
        else:
            print('Errou! Preste mais atenção!')

    porcentagemAcerto = respostasCertas / len(perguntas)
    print(f'Você acertou {respostasCertas} resposta(s).')
    print(f'Sua porcentagem foi {porcentagemAcerto:.2%}')

    print()