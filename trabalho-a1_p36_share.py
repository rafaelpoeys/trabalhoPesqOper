#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Rafael Poeys <rafaelpoeys@gmail.com>

import numpy as np

# Funcao para Imprimir matriz
def Imprimir(m):
    print ("\n", file=arquivo)
    print ("\t||" + ("\t" * (len(m[0])+1)) + "||", file=arquivo)
    for i in range(len(m)):
        print ("\t||\t", end=" ", file=arquivo)
        for j in range(len(m[0])):
            if m[i][j] == 0:
                print ("%.2f\t" % (float(m[i][j])+0), end="", file=arquivo)
                # aqui eu somo 0 "positivo" para sumir o sinal
            else:
                print ("%.2f\t" % float(m[i][j]), end="", file=arquivo)
        print ("||", file=arquivo)
        print ("\t||" + ("\t" * (len(m[0])+1)) + "||", file=arquivo)
    print ("\n", file=arquivo)

# Somar linhaX com linhaY
def Somar(linhaA, linhaB):
    ln = [0]*len(linhaA) # crio uma linha de 'n' elementos com zeros
    for i in range(len(linhaA)):
        ln[i] = linhaA[i] + linhaB[i]
    return ln

# Multiplicar por uma Constante
def Multiplicar(linhaA, k):
    ln = [0]*len(linhaA) # crio uma linha de 'n' elementos com zeros
    for i in range(len(linhaA)):
        ln[i] = k * linhaA[i]
    return ln

# Trocar caso o pivo seja zero
def TrocarLinha(m, l, x): # recebo a matriz(m), a linha atual(l) e o numero de linhas(x) da matriz em questao #
    if l == (x-1): # se a linha recebida for a ultima, encerro a funcao retorno a matriz e 'False' #
        print ("Ho Hooow, esta matriz eh singular.\n\n", file=arquivo)
        return m, False
    else:
        for i in range(l, x):
            if m[i][l] != 0: # se o pivo for diferente de zero, troco a linha e retorno a matriz e 'True' #
                m[l], m[i] = m[i], m[l]
                return m, True
        print ("Eita, essa matriz eh singular.\n\n", file=arquivo)
        return m, False

# Operacoes Elementares (Gauss-Jordan)
def OperacoesElementares(m,p): # p='numero de linhas' | m='matriz' #
    for i in range(p):
        aux = True
        if m[i][i] == 0: # se o pivo da linha for igual a zero, eu troco a linha #
            m, aux = TrocarLinha(m, i, p) # envio a matriz(m), a linha atual(i) e o numero de linhas(p) da matriz em questao #
            Imprimir(m) # realizo a opecao e imprimo o 'passo' #
        if aux:
            m[i] = Multiplicar(m[i], 1/float(m[i][i]))
            Imprimir(m) # realizo a opecao e imprimo o 'passo' #
        else:
            return m
        for j in range(i+1,len(m)): # Troque a linha e meu pivo eh 1, objetivo eh zerar os que estao em baixo do pivo #
            m[j] = Somar(m[j], Multiplicar(m[i], -1*float(m[j][i])))
            Imprimir(m) # realizo a opecao e imprimo o 'passo' #
    for k in range(p-1, -1, -1): # processo inverso, zerando os valores acima da diagonal principal #
        for l in range(k-1, -1, -1):
            m[l] = Somar(m[l], Multiplicar(m[k], -1*float(m[l][k])))
            Imprimir(m) # realizo a opecao e imprimo o 'passo' #
    return m

# Funcao Main #
matriz = np.loadtxt('in.txt')

arquivo = open('out.txt', 'w')
print ("Saida do programa esta em out.txt")
print ("Inicio da execucao")


OperacoesElementares(matriz, matriz.shape[0])

Imprimir(matriz)

arquivo.close()
print ("Fim da execucao")
# Fim