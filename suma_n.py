def suma_nat(a):
	suma = 0
	while a > 0:
		suma = suma + a
		a = a - 1
	print "la suma de todos los numeros naturales es", suma
a = int (input ("ingrese un numero natural: "))
suma = suma_nat(a)
