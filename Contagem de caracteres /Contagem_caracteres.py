"""
Problema: Contagem Caractere
Autor: Renan
Linguagem: Python

A função recebe uma string e retorna a contagem de caracteres
e verificar se aparecem mesmo valores de contagem.
"""


def xo(s):

    # contadores das letras
    count_x = 0
    count_o = 0

    # percorre cada caractere da string
    for l in s:

        # verifica se é X ou x
        if l == 'x' or l == 'X':
            count_x += 1

        # verifica se é O ou o
        elif l == 'O' or l == 'o':
            count_o += 1

        # outros caracteres são ignorados
        else:
            pass

    # comparação final
    # se as quantidades forem iguais → True
    # se forem diferentes → False
    return count_x == count_o