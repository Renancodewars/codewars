def remove_char(s):
    if len(s) == 2:
        return ""
    
    lista = list(s)
    lista.pop(0)      # remove o primeiro
    lista.pop(-1)     # remove o último
    
    return "".join(lista)


# Outra frma simples tambem de resolver

def remove_char(s):
    #your code here
    
    remove = s[1:-1]
    return remove