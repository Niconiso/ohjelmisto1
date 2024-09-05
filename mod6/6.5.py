def parilliset(kokolista):
    lista = [luku for luku in kokolista
             if luku % 2 == 0]
    return lista
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Lista2 = parilliset(lista1)
print("Alkuperäinen lista:", lista1)
print("Parillinen lista:", Lista2)
