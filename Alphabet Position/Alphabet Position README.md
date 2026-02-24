# Replace With Alphabet Position (Python)

Projeto de prática em lógica de programação e manipulação de strings em Python.

O programa recebe um texto qualquer e substitui cada letra pela sua posição no alfabeto:

a = 1
b = 2
c = 3
...
z = 26

Caracteres que não são letras são ignorados (números, espaços, pontuação, símbolos).

---

## Exemplo

Entrada:
The sunset sets at twelve o' clock.

Saída:
20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11

---

## Como funciona

O Python guarda cada caractere como um número interno (Unicode/ASCII).

A função `ord()` retorna esse valor numérico.

Exemplo:

ord('a') = 97
ord('b') = 98

Para obter a posição no alfabeto basta:

posição = ord(letra) - 96

Assim:
97 - 96 = 1 (a)
98 - 96 = 2 (b)

Ou seja, o programa usa matemática para descobrir a posição da letra sem precisar criar um dicionário.

---

## O que é praticado neste projeto

* Loops `for`
* Strings
* Listas
* `append()`
* `join()`
* `lower()`
* `isalpha()`
* `ord()`
* Lógica de transformação de dados

---

## Como executar

1. Instale o Python 3
2. Baixe ou clone o repositório
3. No terminal execute:

python alphabet_position.py

---

## Objetivo

Projeto criado para treino de lógica e entendimento de como o computador representa texto internamente.
