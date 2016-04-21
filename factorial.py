def factorial (n):
	num = 1
	while n > 0:
		num = num * n
		n = n -1 
	print ("el factorial es: ",num)
n = int (input ("ingrese un numero: "))
num = factorial (n)