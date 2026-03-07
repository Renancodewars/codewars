def queue_time(customers, n):  # função recebe lista de clientes e número de caixas
    caixas = [0] * n  # cria uma lista com n caixas iniciando com tempo 0
    
    for cliente in customers:  # percorre cada cliente da fila
        indice_menor = caixas.index(min(caixas))  # encontra o caixa com menor tempo acumulado
        caixas[indice_menor] += cliente  # adiciona o tempo do cliente nesse caixa
    
    return max(caixas)  # retorna o maior tempo entre os caixas (tempo total da fila)