#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Velázquez Larriva Rodrigo Gibran
316252667
'''
x = 10.5;y= 1.0/3;z = 15.3
#x,y,z=10.5,1.0/3,15.3
H = """
El punto en R3 es :
(x,y,z)=(%.2f,%g,%G)
""" % (x,y,z)
print H

G="""
El punto en R3 es:
(x,y,z)=({laX:.2f},{laY:G},{laZ:G})
""".format(laX=x,laY=y,laZ=z)

print G

import math as m
from math import sqrt as s
from math import * #No se recomienda
x=16
x=input("Cual es el valor al que le quieres\n" +
        "calcular la raiz")
print "la raiz cuadrada de %.2f es %f" % (x,m.sqrt(x))
print sqrt(16.5)
print s(16.5)
