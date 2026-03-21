import numpy as np

def sequencia_fib(qtde_valores):
    resposta = np.empty(qtde_valores, dtype=int)
    a = 0
    b = 1
    aux = b
    idx = 0
    while idx < qtde_valores:
        resposta[idx] = a
        aux = b
        b = a + b
        a = aux
        idx += 1
    return resposta

def enesimo_fib(n):
    a = 0
    b = 1
    aux = b
    while n > 0:
        aux = b
        b = a + b
        a = aux
        n -= 1
    return a

def estimar_prop_aurea(n_fibonacci):
    a = 0
    b = 1
    aux = b
    while n_fibonacci > 0:
        aux = b
        b = a + b
        a = aux
        n_fibonacci -= 1
    return b/a