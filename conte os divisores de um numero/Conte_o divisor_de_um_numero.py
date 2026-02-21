def divisors(n):
    count = 0
    i = 1

    while i * i <= n:
        if n % i == 0:
            count += 2
        i += 1

    if int(n ** 0.5) ** 2 == n:
        count -= 1

    return count

    ## Explicação da solução

#A função começa inicializando um contador de divisores (`count`) e uma variável `i` começando em 1.

#Em vez de testar todos os números até `n`, o algoritmo verifica apenas enquanto `i * i <= n`.
#Isso equivale a testar apenas até a raiz quadrada do número.

#Para cada valor de `i`, verifico se `n % i == 0`.
#Quando isso acontece, significa que encontrei dois divisores ao mesmo tempo:

#* o próprio `i`
#* e o número `n // i`

#Por isso o contador é incrementado em 2.

#Exemplo:
#Se `i = 2` divide 12, então `12 // 2 = 6` também é divisor.

#No final, existe um caso especial: quando `n` é um quadrado perfeito.
#Por exemplo, 9.

#Nesse caso:
#3 × 3 = 9

#O divisor 3 seria contado duas vezes, então faço uma verificação final para remover essa duplicação, decrementando 1 do contador.

#Essa abordagem torna o algoritmo muito mais eficiente do que verificar todos os números até `n`.
