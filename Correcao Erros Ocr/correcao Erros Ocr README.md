# 🧠 Correção de Erros em OCR (Reconhecimento de Caracteres)

## 📖 Descrição do Desafio

Softwares de OCR (*Optical Character Recognition*) são utilizados para digitalizar textos impressos e transformá-los em texto editável no computador.
Porém, especialmente em documentos antigos ou escritos à máquina, esses sistemas costumam cometer erros ao identificar alguns caracteres.

O objetivo deste desafio é simular a correção automática desses erros.

Alguns caracteres são confundidos por terem formas visuais muito parecidas:

| Caractere incorreto | Deve ser corrigido para |
| ------------------- | ----------------------- |
| `5`                 | `S`                     |
| `0`                 | `O`                     |
| `1`                 | `I`                     |

A função desenvolvida deve receber uma string contendo um texto digitalizado com possíveis falhas e retornar o texto corrigido.

Os números presentes no texto não são intencionais — eles aparecem apenas por erro de leitura do OCR.

---

## 🎯 O que este desafio trabalha

Este exercício tem foco em fundamentos importantes de programação:

* Manipulação de **strings**
* Substituição de caracteres
* Criação de funções
* Tratamento de dados imperfeitos (dados do mundo real)
* Pensamento algorítmico
* Reconhecimento de padrões

Esse tipo de problema é comum em áreas como:

* Processamento de texto
* Automação
* Análise de documentos
* Data cleaning (limpeza de dados)

---

## 💡 Conceito envolvido

O desafio simula um cenário real: computadores frequentemente lidam com dados incorretos.
Antes de analisar ou armazenar informações, muitas vezes é necessário **corrigir os dados automaticamente**.

Esse processo é chamado de:

> **Pré-processamento de dados** — etapa essencial em programação, ciência de dados e inteligência artificial.

---

## 🚀 Objetivo

Criar uma função que:

1. Receba um texto com possíveis erros de OCR
2. Identifique os caracteres incorretos
3. Retorne o texto corrigido

---

## 🧩 Exemplo

Entrada:
HELLO W0RLD

Saída:
HELLO WORLD

---

## 🛠 Linguagem utilizada

Python 3
