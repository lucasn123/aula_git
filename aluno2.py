def Maior(lista):
    if len(lista) == 0:
        return 0
    m = lista [0]
    for i in range (1, len(lista)):
        if m < lista[i]:
            m = lista[i]
    return m
