# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 08:19:12 2017

@author: Samsung
"""

#Selecionar número

#lista = []
# n = int(input('Quantos números você quer na lista?'))
def ler_numeros(n):
    lista = []
    for i in range(n):
          x = float(input('escreva um número'))
        lista.append(x)
    return lista
#    print(lista)    
        
    