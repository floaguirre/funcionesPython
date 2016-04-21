"""def escribe_media(x,y):
	media=(x+y)/2
	print("La media de ",x," y ",y," es :", media)

a=3
b=5
escribe_media(a,b)
print("Programa terminado")


def calcula_media(x,y):
	resultado=(x+y)/2
	return resultado
	
a=3
b=5
media = calcula_media(a,b)
print("La media de ",a," y ",b," es :", media)
print("Programa terminado")"""


def numeros_nat(a):
	cont=0
	while cont < a:
		cont=cont+1
		print " ", cont
a=int(input("Ingrese un numero: ")) 
cont = numeros_nat(a)