#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

#conteudo_arquivo = open('in.txt','r')

np.matriz = np.loadtxt('in.txt')

n_linhas = list(range(np.matriz.shape[0]))
n_colunas = list(range(np.matriz.shape[1]))
n_impressoes = 0

def imprimir_matriz():
	for i in n_linhas:
		print ("[", end=" ")
		for j in n_colunas:
			if j == (np.matriz.shape[1]-1):
				print ("|", end=" ")
				print(np.matriz[i][j], end=" ")
				#if np.matriz[i][j] > 9:
				#	if np.matriz[i][j] < 100:
				#		print(np.matriz[i][j], end=" ")
				#	else:
				#		print(np.matriz[i][j], end="")
				#else:
				#	print(np.matriz[i][j], end="  ")
				print ("]", end="\n")
			else:
				print(np.matriz[i][j], end=" ")
	

def operacoes_elementares():
	#i = 0
	for i in range(0,np.matriz.shape[1]-1):
		if np.matriz[i][i] == 0:
			c = 1
			while (np.matriz[i+c][i] == 0 and (i+c) < n_linhas):
				c = c + 1
				#pass
				if (i+c) == n_linhas:
					flag = 1
					break

				k = 0
				for j in range(i,n_colunas):
					temp = np.matriz[j][k]
					np.matriz[j+c][k]
					np.matriz[j][k] = temp
					k = k + 1

		for j in range(0,np.matriz.shape[1]-1):
			if i != j:
				pro = (np.matriz[j][i] / np.matriz[i][i])

				for k in (n_colunas):
					np.matriz[j][k] = np.matriz[j][k] - (np.matriz[i][k] * pro)
	return flag

def resultado_final():
	print ("Resultado eh : ")

	if flag == 2:
		print("Existem infinitas solucoes [SPI - Sistema Possivel Inderterminado]")
	elif flag == 3:
		print("Nao existe solucao [SI - Sistema Impossivel]")
	else:
		for i in (n_colunas-1):
			print(np.matriz[i][n_colunas-1] / np.matriz[i][i])

def verificar_consistencia():
	flag = 3

	for i in (n_colunas-1):
		soma = 0
		for j in (n_colunas-1):
			soma = soma + np.matriz[i][j]
			if soma == np.matriz[i][j]:
				flag = 2
	return flag



print("Matriz lida do arquivo: \n")
imprimir_matriz()
print ("\n")


print("Matriz sera escalonada pelo metodo de Gauss-Jordam: ")
flag = operacoes_elementares()

if flag == 1:
	flag = verificar_consistencia

imprimir_matriz()
print ("\n")

