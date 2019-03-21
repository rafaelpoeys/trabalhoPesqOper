#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

#conteudo_arquivo = open('in.txt','r')

matriz = np.loadtxt('in.txt')


def imprimir_matriz():
	for i in range(0,matriz.shape[0]):
		print ("[", end=" ")
		for j in range(0,matriz.shape[1]):
			if j == (matriz.shape[1]-1):
				print("|", end=" ")
				#print(matriz[i][j], end=" ")
				if matriz[i][j] > 9:
					if matriz[i][j] < 100:
						print(matriz[i][j], end=" ")
					else:
						print(matriz[i][j], end="")
				else:
					print(matriz[i][j], end="  ")
				print ("]", end="\n")
			else:
				print(matriz[i][j], end=" ")

def trocar_linha(a,b):
	print ("troquei a linha: \t", a)
	print ("com a linha: \t", b)

def operacoes_elementares():
	if matriz[0][0] > 0:
		if matriz[0][0] == 1:
			print ("A11 = \t", matriz[0][0])
		else:
			trocar_linha(1,2)
	else:
		if ((matriz[1][0] == 0) and (matriz[2][0] == 0)):
			print("sistema Impossivel")
		else:
			trocar_linha(2,1)

print("Matriz inserida no sistema atravez do arquivo in.txt")
imprimir_matriz()

print("\n")

if matriz.shape[0] == (matriz.shape[1] - 1):
	print("eh uma matriz quadrada,")
	print("vamos para as operacoes elementares...")
	#imprimir_matriz()

	operacoes_elementares()

else:
	print("nao eh uma matrix quadrada,")
	print("nao eh possivel resolver")
	print("utilizando Gauss-Jordan.")
	print("\nTente outra vez!\n")
	print("So que... com uma matriz quadrada...")