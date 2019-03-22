#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fpformat
import numpy as np

# Funcao para Imprimir matriz
def impri(m):
    print "\n"
    print "\t||" + ("\t" * (len(m[0]) + 1)) + "||"
    for i in range(len(m)):
        print "\t||\t",
        for j in range(len(m[0])):
            if m[i][j] == 0:
                print fpformat.fix((m[i][j]+0),2),"\t",
            else:
                print fpformat.fix(m[i][j],2),"\t",
        print "||"
        print "\t||" + ("\t" * (len(m[0]) + 1)) + "||"
    print "\n"
    
# Somar linha1 com linha2
def som(l1, l2):
    ln = [0]*len(l1)
    for i in range(len(l1)):
        ln[i] = l1[i] + l2[i]
    return ln

# Multiplicar por Constante
def multi(l1, k):
    ln = [0]*len(l1)
    for i in range(len(l1)):
        ln[i] = k * l1[i]
    return ln

# Trocar caso o pivo seja zero
def swap_linha(m, l, x):
    if l == (x-1):
        print "Esta matriz eh singular.\n Isso atrapalha na resolucao"
        return m, False
    else:
        for i in range(l, x):
            if m[i][l] != 0:
                m[l], m[i] = m[i], m[l]
                return m, True
        print "Esta matriz eh singular.\n Isso atrapalha na resolucao"
        return m, False

# Operacoes Elementares (Gauss-Jordan)
def oper(m,p):
    for i in range(p):
        aux = True
        if m[i][i] == 0:
            m, aux = swap_linha(m, i, p)
            impri(m)
        if aux:
            m[i] = multi(m[i], 1/float(m[i][i]))
            impri(m)
        else:
            return m
        for j in range(i+1,len(m)):
            m[j] = som(m[j], multi(m[i], -1*float(m[j][i])))
            impri(m)
    for k in range(p-1, -1, -1):
        for l in range(k-1, -1, -1):
            m[l] = som(m[l], multi(m[k], -1*float(m[l][k])))
            impri(m)
    return m

# Funcao Main #
mat = np.loadtxt('in1.txt')
oper(mat, mat.shape[0])
# Fim