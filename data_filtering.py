def data_filtering(file_path):
    # first of all, we have a txt file with a lot of portuguese words.
    # lets read the file and then convert it to list, to be easier to manipulate
    words_list = read_file_as_list(file_path)

    # We need to filter some of those words
    words_list = remove_non_alpha(words_list)

    words_list = remove_smaller_than_3_bigger_than_8(words_list)

    words_list = remove_upper_only_words(words_list)

    words_list = convert_to_lowercase(words_list)

    words_list = remove_accents(words_list)

    words_list = remove_repeated_words(words_list)

    # todo: remove the plural of words and substring
    # words_list = remove_substrings()

    # end of first filtering batch. Exporting the output to file
    file_name = write_list_as_file(words_list)

    read_file_as_list(file_name)


def debug_print(output_list, removed_list, message):
    # this is just a tool for fast check if the results seems as they should be
    # it shows like a list head, the first 25 values
    print('---\n'
          '{}.\n'
          'List length is {}.\n'
          'LIST:\n'
          '{}\n'
          'DISCARD:\n'
          '{}\n'
          '---\n'
          .format(message, len(output_list), output_list[:25], removed_list[:25]))


def read_file_as_list(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        words_list = list(file)
        debug_print(words_list, [], 'Converting '+str(file_path)+' to list')
        words_list = remove_spaces_linebreak(words_list)

    return words_list


def write_list_as_file(words_list):
    with open('PT_words_2', 'w', encoding="utf-8") as file:
        for word in words_list:
            file.write(word + "\n")

    return 'PT_words_2'


def remove_spaces_linebreak(words_list):
    aux_list = list(word.strip() for word in words_list)
    debug_print(aux_list, [], 'Removing white spaces and \\n')
    return aux_list


def remove_non_alpha(words_list):
    aux_list = []
    removed_list = []
    for word in words_list:
        if word.isalpha():
            aux_list.append(word)
        else:
            removed_list.append(word)

    debug_print(aux_list, removed_list, 'Removed non-aplha charactered words')
    return aux_list


def remove_smaller_than_3_bigger_than_8(words_list):
    aux_list = []
    discard_list = []
    for word in words_list:
        if 3 < len(word) < 8:
            aux_list.append(word)
        else:
            discard_list.append(word)

    debug_print(aux_list, discard_list, 'removed words bigger than 3 and smaller than 8')
    return aux_list


def remove_upper_only_words(words_list):
    aux_list = []
    remove_list = []
    for word in words_list:
        if not word.isupper():
            aux_list.append(word)
        else:
            remove_list.append(word)

    debug_print(aux_list, remove_list, 'removed uppercase-only words')
    return aux_list


def convert_to_lowercase(words_list):
    aux_list = list(word.lower() for word in words_list)
    debug_print(aux_list, [], 'Converting to lowercase')
    return aux_list


def remove_accents(words_list):
    import unidecode
    aux_list = []
    remove_list = []
    for word in words_list:
        aux_list.append(unidecode.unidecode(word))
        remove_list.append(word)

    debug_print(aux_list, remove_list, 'o acento das palavras')
    return aux_list


def remove_repeated_words(words_list):
    # convert to set and then sort again
    lista_auxiliar = list(set(words_list))
    lista_auxiliar.sort()
    debug_print(lista_auxiliar, [], 'palavras repetidas')
    return lista_auxiliar


# todo: use str.replace()
def remove_substrings(words_list):
    lista_auxiliar = []
    refugo = []
    for palavra in words_list:
        for palavra2 in words_list:
            if not palavra2.find(palavra):
                print('Entrou', palavra2)
                lista_auxiliar.append(palavra2)
            else:
                refugo.append(palavra2)
    debug_print(lista_auxiliar, refugo, 'palavras no plural')
    return lista_auxiliar


data_filtering('PT_words_1')
