#!/usr/bin/python

from random import randint

def gerar_seis_numeros():
    numeros = []

    while len(numeros) < 6:
        x = randint(1, 60)
        if x not in numeros: numeros.append(x)

    return numeros

x = gerar_seis_numeros()
print('***********************************************')
print('Numeros para apostar são : ', x)
print('***********************************************')
