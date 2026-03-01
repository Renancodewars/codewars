def correct(s):  # função recebe uma string com erros do OCR
    troca = str.maketrans({  # cria uma tabela de substituição de caracteres
        "5": "S",  # 5 vira S
        "0": "O",  # 0 vira O
        "1": "I"   # 1 vira I
    })

    novo = s.translate(troca)  # aplica a tabela na string inteira de uma vez
    return novo  # retorna o texto já corrigido


# exemplo da segunda forma de solucionar este problema

    """
    def correct(s):  # função recebe a string com erro
    novo = s.replace("5", "S")  # troca todos os 5 por S
    novo = novo.replace("0", "O")  # troca todos os 0 por O
    novo = novo.replace("1", "I")  # troca todos os 1 por I
    return novo  # devolve a string corrigida
   
    """