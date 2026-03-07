# 🛒 Tempo Total da Fila no Supermercado

## 📖 Descrição do Desafio

Em um supermercado com caixas de autoatendimento, vários clientes aguardam na fila para finalizar suas compras. Cada cliente leva um tempo específico para concluir o pagamento.

O objetivo deste desafio é calcular **quanto tempo total será necessário para que todos os clientes da fila terminem suas compras**, considerando que existem vários caixas funcionando ao mesmo tempo.

Cada caixa pode atender apenas **um cliente por vez**, mas assim que termina de atender um cliente, já começa a atender o próximo da fila.

---

## 📥 Entrada

A função recebe dois parâmetros:

**clientes**
Uma lista de números inteiros positivos representando os clientes na fila.
Cada número indica o **tempo necessário** para que aquele cliente finalize sua compra.

Exemplo:
[5, 3, 4]

Isso significa:

* cliente 1 leva **5 minutos**
* cliente 2 leva **3 minutos**
* cliente 3 leva **4 minutos**

**n**
Um número inteiro positivo que representa **quantos caixas registradoras estão disponíveis**.

---

## 📤 Saída

A função deve retornar um **número inteiro**, que representa o **tempo total necessário** para que todos os clientes sejam atendidos.

---

## 🎯 O que este desafio trabalha

Este exercício desenvolve conceitos importantes de lógica de programação:

* Simulação de filas
* Distribuição de tarefas
* Manipulação de listas
* Pensamento algorítmico
* Otimização de processos

Esse tipo de problema aparece em áreas como:

* Sistemas de atendimento
* Balanceamento de carga
* Processamento paralelo
* Simulação de sistemas reais

---

## 💡 Conceito envolvido

O desafio simula um problema clássico da computação chamado:

**Balanceamento de carga (Load Balancing)**

A ideia é distribuir tarefas entre vários "trabalhadores" (neste caso, os caixas) de forma eficiente para minimizar o tempo total de execução.

Esse mesmo conceito é usado em:

* servidores web
* processamento em nuvem
* renderização de gráficos
* sistemas distribuídos

---

## 🧩 Exemplo

Entrada:

clientes = [5, 3, 4]
n = 1

Saída:

12

Explicação:

Existe apenas **um caixa**, então os clientes serão atendidos um após o outro:

5 + 3 + 4 = 12 minutos

---

Outro exemplo:

Entrada:

clientes = [10, 2, 3, 3]
n = 2

Saída:

10

Explicação:

Os clientes são distribuídos entre dois caixas, permitindo atendimento simultâneo.