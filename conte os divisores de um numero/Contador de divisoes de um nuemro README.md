# Conte os Divisores de um Número

## Descrição do problema

Dado um número inteiro positivo `n`, o objetivo é retornar quantos divisores esse número possui.

Um divisor é qualquer número inteiro que divide `n` sem deixar resto.

Por exemplo, o número 12 possui os divisores:
1, 2, 3, 4, 6 e 12.

Logo, a resposta para 12 é 6.

## Exemplos

Entrada:
4
Saída:
3 (1, 2, 4)

Entrada:
5
Saída:
2 (1 e 5)

Entrada:
12
Saída:
6 (1, 2, 3, 4, 6, 12)

Entrada:
30
Saída:
8 (1, 2, 3, 5, 6, 10, 15, 30)

## O que este desafio trabalha

Este problema envolve lógica matemática, divisão inteira e otimização de algoritmos.

Uma solução ingênua verificaria todos os números de 1 até `n`, porém isso seria lento para números grandes.
A ideia principal é perceber que os divisores sempre aparecem em pares.
Por exemplo:

Se 2 divide 12, então 6 também divide 12.

Ou seja:
2 × 6 = 12

Isso permite verificar apenas até a raiz quadrada do número, reduzindo bastante o tempo de execução.
