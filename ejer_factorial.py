""" 1. e) Funcion que calcula el factorial de un numero x, ingresado por el usuario """

def factorial(n):
	fact = 1
	while n > 0:
		fact = fact * n
		n = n-1
	return fact

n = int (input ('Ingrese un numero: '))
fact = factorial(n)
print 'El factorial de n: ', fact
