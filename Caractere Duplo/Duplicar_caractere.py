"""
Problema: Caractere Duplo
Autor: Renan
Linguagem: Python

A função recebe uma string e retorna uma nova string
onde cada caractere aparece duas vezes.
"""

def double_char(s):

resultado = []

for letra in s:
    resultado.append(letra * 2)

return "".join(resultado)
