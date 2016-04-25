#from package.module import function
# -*- coding: utf-8 -*-
"""Dado un número natural k, si la suma de sus divisores (sin contar a sí mismo) es igual al
número se dice que éste es perfecto, si es inferior se lo llama deficiente y si es mayor es
un número abundante. Por ejemplo:
i. 6 tiene como divisores a 1, 2,3: la suma es 6, es un número perfecto.
ii. 9 tiene como divisores a 1,3: la suma es 4, es un número deficiente
iii. 12 tiene como divisores a 1, 2, 3, 4, 6: la suma es 16, es un número
Desarrolle una función que determine si un número es perfecto, deficiente o
abundante."""

def perfecto (x):
	cont = 1
	acum = 0
	while cont < x :
		if x % cont == 0:
			acum = acum + cont
		cont = cont + 1
	return acum


x = int(input("Ingrese un numero: "))
acum = perfecto (x)
if acum > x:
	print "%s es abundante" %x
elif acum < x:
	print "%s es deficiente" %x
else:
	print "%s es perfecto" %x


