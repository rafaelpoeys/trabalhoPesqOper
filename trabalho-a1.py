#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fpformat
import numpy as np

# Funcao para enumerar os passos
def Contador(c):
    return int(c) + 1

# Esta funcao ira dividir minha matriz aumentada
def Matriz_Aumentada(m):
    matA = np.zeros((m.shape[0],(m.shape[1]-1)))
    matB = np.zeros((m.shape[0],1))

    for i in range(m.shape[0]):
        for j in range(m.shape[1]-1):
            matA[i][j] = m[i][j]

    for g in range(m.shape[0]):
        matB[g][0] = m[g][(m.shape[1]-1)]

    return matA,matB

# Funcao para Imprimir matriz
def Imprimir(m,y):
    print "\n"
    if y:
        global count
        #count = Contador(count)
        count += 1
        print "Passo: ",
        print count
    print "\t||" + ("\t" * (len(m[0]) + 1)) + "||"
    for i in range(len(m)):
        print "\t||\t",
        for j in range(len(m[0])):
            if m[i][j] == 0:
                print fpformat.fix((m[i][j]+0),2),"\t",
            else:
                print fpformat.fix(m[i][j],2),"\t",
            #print m[i][j],"\t",
        print "||"
        print "\t||" + ("\t" * (len(m[0]) + 1)) + "||"
    print "\n"

# Preciso comentar esta funcao
def MatrizSingular(m):
    print ("Em matematica, uma matriz quadrada eh dita singular quando nao admite uma inversa.")
    print ("- Uma matriz eh singular se e somente se seu determinante eh nulo.")
    print ("\tPor exemplo, se uma matriz quadrada tiver pelo menos uma linha ou coluna nula,")
    print ("\ttera determinante zero (0), o que caracteriza uma matriz singular.")
    print ("\n")
    print ("- Uma matriz A, eh singular se e somente se existir um vetor X, nao nulo tal que:")
    print ("\t Ax = 0")
    print ("\n")
    print ("- Se uma matriz A eh singular, entao o problema Ax = b ou nao possui solucao ou possui infinitas soculoes.")
    print ("\n\n")
    print ("Ultima interacao: ")
    print ("(a matriz ficou desta forma)")
    Imprimir(m,False)
    
    '''
    mat = np.zeros((m.shape[0],(m.shape[1]-1)))
    for i in range(m.shape[0]):
        for j in range(m.shape[1]-1):
            mat[i][j] = m[i][j]
    '''
    mat,tam = Matriz_Aumentada(m)
    print "detA = ",
    print (np.linalg.det(mat))
    exit()
    
# Somar linhaX com linhaY
def Somar(l1, l2):
    ln = [0]*len(l1)
    for i in range(len(l1)):
        ln[i] = l1[i] + l2[i]
    return ln

# Multiplicar por uma Constante
def Multiplicar(l1, k):
    ln = [0]*len(l1)
    for i in range(len(l1)):
        ln[i] = k * l1[i]
    return ln

# Trocar caso o pivo seja zero
def TrocarLinha(m, l, x):
    if l == (x-1):
        print "Ho Hooow, esta matriz eh singular.\n\n"
        return m, False
    else:
        for i in range(l, x):
            if m[i][l] != 0:
                m[l], m[i] = m[i], m[l]
                return m, True
        print "Eita, essa matriz eh singular.\n\n"
        return m, False

# Operacoes Elementares (Gauss-Jordan)
def OperacoesElementares(m,p):
    for i in range(p):
        aux = True
        if m[i][i] == 0:
            m, aux = TrocarLinha(m, i, p)
            Imprimir(m,True)
        if aux:
            m[i] = Multiplicar(m[i], 1/float(m[i][i]))
            Imprimir(m,True)
        else:
            #return m
            MatrizSingular(m)
        for j in range(i+1,len(m)):
            m[j] = Somar(m[j], Multiplicar(m[i], -1*float(m[j][i])))
            Imprimir(m,True)
    for k in range(p-1, -1, -1):
        for l in range(k-1, -1, -1):
            m[l] = Somar(m[l], Multiplicar(m[k], -1*float(m[l][k])))
            Imprimir(m,True)
    return m

# Funcao Main #
matriz = np.loadtxt('in5.txt')
print("Matriz do jeito que estah no arquivo in.txt")
count = 0
OperacoesElementares(matriz, matriz.shape[0])

print ("\n\n")
#print ("\t" * (len(matriz[0]) -2 ) + "Forma Escalonada Reduzida")
print ("\tForma Escalonada Reduzida")
Imprimir(matriz,False)

#np.set_printoptions(precision=2)

alfabeto = ("x", "y", "z", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a", "X", "Y", "Z", "W", "V", "U", "T", "S", "R", "Q", "P", "O", "N", "M", "L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A")
a,b = Matriz_Aumentada(matriz)
#c = np.zeros()
c = np.linalg.solve(a,b)

#c = np.around(c,decimals=5)

print "Solucao {",
for d in range(len(c)):
    #print "\n"+alfabeto[d]+" = %.3f"%float(c[d]),
    print alfabeto[d]+"=%.3f"%float(c[d]),

print "}"
#print np.linalg.solve(Matriz_Aumentada(matriz))
#print ("S {","x=",b[0],"y=",b[1],"z=",b[2],"}")
# Fim