def edades (x,y):
	if x > y:
		resta = x - y
		print "La primer persona es la mayor"
		print "a la segunda persona le faltan %s anios para alcanzar a la primera" % resta
	elif x < y:
		resta = y - x
		print "La segunda persona es la mayor"
		print "A la primer persona le faltan" ,resta, "anios para alcanzar a la primera"
	else:
		print "Las dos personas tienen la misma edad"



x = int(input("Ingrese la edad de la primer presona: "))
y = int(input ("Ingrese la edad de la segunda persona: "))
edades (x,y)
