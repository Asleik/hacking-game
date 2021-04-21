def debug_print(words_list, discard_list, message):
    # todo: make message optional parameter. If null, do not show "was deleted from the list"
    print('---\n'
          '{} was deleted from the list.\n'
          'List length is {}.\n'
          'LIST:\n'
          '{}\n'
          '---\n'
          'DISCARD:\n'
          '{}\n'
          '---\n'
          .format(message, len(words_list), words_list[:25], discard_list[:25]))


def select_bigger_than_3_smaller_than_8(list_of_words):
    aux_list = []
    discard_list = []
    for word in list_of_words:
        if 3 < len(word) < 8:
            aux_list.append(word)
        else:
            discard_list.append(word)

    debug_print(aux_list, discard_list, '3 > Words > 8')
    return aux_list


def retira_nao_letras(lista_de_palavras):
    lista_auxiliar = []
    refugo = []
    for palavra in lista_de_palavras:
        if palavra.isalpha():
            lista_auxiliar.append(palavra)
        else:
            refugo.append(palavra)

    debug_print(lista_auxiliar, refugo, 'não letras')
    return lista_auxiliar


def retira_palavras_maiusculas(lista_de_palavras):
    lista_auxiliar = []
    refugo = []
    for palavra in lista_de_palavras:
        if not palavra.isupper():
            lista_auxiliar.append(palavra)
        else:
            refugo.append(palavra)

    debug_print(lista_auxiliar, refugo, 'palavras totalmente maiusculas')
    return lista_auxiliar


def remove_acento(lista_de_palavras):
    import unidecode
    lista_auxiliar = []
    refugo = []
    for palavra in lista_de_palavras:
        lista_auxiliar.append(unidecode.unidecode(palavra))
        refugo.append(palavra)

    debug_print(lista_auxiliar, refugo, 'o acento das palavras')
    return lista_auxiliar


def converte_palavras_minuscula(lista_de_palavras):
    lista_auxiliar = list(palavra.lower() for palavra in lista_de_palavras)
    debug_print(lista_auxiliar, [], 'convertido tudo para minusculo')
    return lista_auxiliar


def retira_palavras_repetidas(lista_de_palavras):
    # outra solução é usar set()
    # transformei em set para retirar os itens repetidos e em list novamente pq set não tem indice
    # lista_de_palavras = list(set(list(palavra.lower() for palavra in lista_de_palavras)))
    lista_auxiliar = []
    refugo = []
    # todo: for inside another for is outrageous. Fix later
    for palavra in lista_de_palavras:
        if palavra not in lista_auxiliar:
            lista_auxiliar.append(palavra)
        else:
            refugo.append(palavra)
            print('Está rodando:', palavra)

    debug_print(lista_auxiliar, refugo, 'palavras repetidas')
    return lista_auxiliar


def retira_substrings(lista_de_palavras):
    lista_auxiliar = []
    refugo = []
    for palavra in lista_de_palavras:
        for palavra2 in lista_de_palavras:
            if not palavra2.find(palavra):
                print('Entrou', palavra2)
                lista_auxiliar.append(palavra2)
            else:
                refugo.append(palavra2)
    debug_print(lista_auxiliar, refugo, 'palavras no plural')
    return lista_auxiliar


def data_treatment_1(file_path):
    with open(file_path, 'r', encoding="utf-8") as arquivo:
        # convertendo para lista
        lista_de_palavras = list(arquivo)
        debug_print(lista_de_palavras, [], 'nada')

        # retirando os espaçoe e \n das palavras
        lista_de_palavras = list(palavra.strip() for palavra in lista_de_palavras)
        debug_print(lista_de_palavras, [], 'espaço e \\n')

        # retirando as palavras menores que 3 e maiores que 8
        lista_de_palavras = select_bigger_than_3_smaller_than_8(lista_de_palavras)

        # retirando palavras que tem caracteres que não são considerados letras pelo banco de dados do unicode
        lista_de_palavras = retira_nao_letras(lista_de_palavras)

        # retirando palavras que são feitas apenas de caracteres maiúsculos
        lista_de_palavras = retira_palavras_maiusculas(lista_de_palavras)

        # converte todas as palavras para minusculas
        lista_de_palavras = converte_palavras_minuscula(lista_de_palavras)

        # retirando palavras cuja diferença é só um acento
        lista_de_palavras = remove_acento(lista_de_palavras)

        # retirar palavras repetidas (fazer um set) e tudo minusculo
        lista_de_palavras = retira_palavras_repetidas(lista_de_palavras)

        with open('Lista_Palavras_PT_2.txt', 'w', encoding="utf-8") as arquivo2:
            for palavra in lista_de_palavras:
                arquivo2.write(palavra + "\n")


def data_treatment_2(file_path):
    with open(file_path, 'r', encoding="utf-8") as arquivo:
        pass
        # todo: retirando o plural das palavras
        # esta será a ultima pq demanda muito tempo
        # lista_de_palavras = retira_substrings(lista_de_palavras)


data_treatment_1('Lista_Palavras_PT_1.txt')  # Não rodar novamente pq o arquivo já foi gerado.
# tratamento_dados_2('Lista_Palavras_PT_2.txt')
