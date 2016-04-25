"""def calcula_media(x,y):
	resultado=(x+y)/2
	return resultado
	
a=3
b=5
media = calcula_media(a,b)
print("La media de ",a," y ",b," es :", media)
print("Programa terminado")


def numeros_nat(a):
	cont=0
	while cont < a:
		cont=cont+1
		print " ", cont
a=int(input("Ingrese un numero: ")) 
cont = numeros_nat(a)"""

def area_lateral(r,g):
	pi = 3.14159265359
	resultado_lat = pi * r * g
	return resultado_lat

r = float (input("Ingrese el radio de la base: "))
g = float (input("Ingrese la generatriz del cono: "))
lateral = area_lateral(r,g)
print "el area lateral es: ", lateral


def area_total(r):
	p=3.14159265359
	r=r*r
	resultado_total = lateral + p * r
	return resultado_total

area = area_total(r)
print"el area total: ", area


