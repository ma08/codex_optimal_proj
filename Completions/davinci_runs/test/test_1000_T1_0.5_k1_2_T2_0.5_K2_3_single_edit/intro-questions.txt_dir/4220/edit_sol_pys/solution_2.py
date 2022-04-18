#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 19:06:21 2019


@author: mauri
"""


def abrirArchivo():
    file = open('/home/mauri/Documentos/Python/Archivos/file.txt', 'r')
    linea = file.readline()
    while linea != "":
        print(linea)
        linea = file.readline()
    file.close()


def escribirArchivo():
    file = open('/home/mauri/Documentos/Python/Archivos/file.txt', 'w')
    file.write('Hola mundo')
    file.close()


def escribirArchivo2():
    file = open('/home/mauri/Documentos/Python/Archivos/file.txt', 'w')
    file.write('Hola mundo \n')
    file.write('Segunda linea')
    file.close()


def escribirArchivo3():
    file = open('/home/mauri/Documentos/Python/Archivos/file.txt', 'w')
    file.write('Hola mundo \n')
    file.writelines(['Segunda linea \n', 'Tercera linea'])
    file.close()


def escribirArchivo4():
    file = open('/home/mauri/Documentos/Python/Archivos/file.txt', 'a')
    file.write('\nCuarta linea')
    file.close()


escribirArchivo4()
abrirArchivo()
