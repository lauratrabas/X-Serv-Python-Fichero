#!/usr/bin/python

fd = open("/etc/passwd","r")

lineas = fd.readlines()

diccionario = {}

for linea in lineas:
	caracteres = linea.split(":")
	diccionario[caracteres[0]] = caracteres[-1][:-1]

try:

	print diccionario["root"]
	print diccionario["imaginario"]
	
except KeyError:
	print("El nombre no existe")

fd.close()

