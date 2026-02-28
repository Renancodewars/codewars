def tribonacci(signature, n):
    if n == 0:
        return []
    
    resultado = signature[:n]
    
    while len(resultado) < n:
        proximo = resultado[-1] + resultado[-2] + resultado[-3]
        resultado.append(proximo)
    
    return resultado