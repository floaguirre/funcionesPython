"""i) Dado un numero natural k, si la suma de sus divisores (sin contar a si mismo) es igual al
nnmero se dice que este es perfecto, si es inferior se lo llama deficiente y si es mayor es
un numero abundante. Por ejemplo:
i. 6 tiene como divisores a 1, 2,3: la suma es 6, es un numero perfecto.
ii. 9 tiene como divisores a 1,3: la suma es 4, es un numero deficiente
iii. 12 tiene como divisores a 1, 2, 3, 4, 6: la suma es 16, es un numero abundante.
Desarrolle una funcion que determine si un numero es perfecto, deficiente oabundante."""


def perfectodeficienteabundante (condicion,x):
	acumulador = 0
	cont = 0
	while condicion == "S" or condicion == "s":
		while cont < x - 1:
			cont = cont + 1
			if x % cont == 0:
				acumulador = acumulador + cont
		
		if x > acumulador:
			print ("el numero",x," es deficiente.")

		elif x < acumulador:
			print ("el numero",x," es abundante.")

		else:
			print ("el numero",x," es perfecto")

		condicion = raw_input ("Desea ingresar otro numero?: S/N")
		
	print ("salio del programa")


condicion = raw_input ("desea ingresar un numero? S/N")
x = int(raw_input("ingrese un numero: "))
perfectodeficienteabundante (condicion,x)