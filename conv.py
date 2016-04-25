"""N Convertir medidas dadas en metros a pies y pulgadas (1 metro = 39,37 pulgadas y
1 pie= 12 pulgadas)."""

def piesypulgadas (x):
	conver = x * 39.37
	print  x ,  'metros son ', conver, 'pulgadas '
	conver = x * 3.28
	print  x, " metros son " ,conver, "pies"

print ""
print "Conversor de metros a pies y pulgadas"
print ""
cond = raw_input("Desea convertir metro en pies y pulgadas: S/N: ")
while (cond =="S") or (cond == "s"):
	x = float (input ("Ingrese una medida en metros: "))
	piesypulgadas (x)
	cond = raw_input ("Desea realizar otra conversion? S/N: ")
print "fin del programa"