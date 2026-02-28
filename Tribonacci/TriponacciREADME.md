# Sequência de Tribonacci - Python

Implementação da sequência **Tribonacci** em Python.

A sequência Tribonacci é semelhante à sequência de Fibonacci, porém, ao invés de somar apenas os 2 últimos números, somamos os **3 últimos** para gerar o próximo termo.

---

## Como funciona

Na sequência de Fibonacci:

F(n) = F(n-1) + F(n-2)

Na sequência de Tribonacci:

T(n) = T(n-1) + T(n-2) + T(n-3)

Ou seja, cada número depende dos **três anteriores**.

---

## Assinatura (Signature)

A função recebe uma lista inicial chamada **assinatura**, contendo 3 números iniciais da sequência.

Exemplo:

```
[1, 1, 1]
```

A partir disso, a sequência gerada será:

```
[1, 1, 1, 3, 5, 9, 17, 31, ...]
```

Outro exemplo:

```
[0, 0, 1]
→ [0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
```

---

## Objetivo da função

Criar uma função que:

* Recebe uma lista com 3 números (assinatura)
* Recebe um número `n`
* Retorna os **n primeiros elementos da sequência**, incluindo a assinatura inicial

Se `n = 0`, deve retornar uma lista vazia.

---

## Exemplo de uso

Entrada:

```
signature = [1, 1, 1]
n = 10
```

Saída:

```
[1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
```

---

## O que é praticado neste projeto

* Manipulação de listas
* Loops `while` / `for`
* Acesso por índice
* Soma de elementos
* Lógica de geração de sequência
* Pensamento iterativo

---

## Observação

O tamanho da sequência depende do valor `n`.
A assinatura inicial sempre possui 3 números, mas a função deve funcionar para qualquer valor válido de `n`.

---

## Finalidade

Projeto desenvolvido para prática de lógica de programação e treino em resolução de problemas (Codewars - 6 kyu).
