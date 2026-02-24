def alphabet_position(text):                  # função que recebe uma string
    ordem = []                                # lista onde guardaremos os números

    for caractere in text.lower():            # percorre cada letra em minúsculo
        if caractere.isalpha():               # verifica se é uma letra
            posicao = ord(caractere) - 96     # converte letra para posição (a=1, b=2...)
            ordem.append(str(posicao))        # adiciona na lista como texto

    return " ".join(ordem)                    # junta tudo separado por espaço


# teste rápido
if __name__ == "__main__":
    frase = "The sunset sets at twelve o' clock."   # texto de exemplo
    print(alphabet_position(frase))                 # imprime o resultado
```
