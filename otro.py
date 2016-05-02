# -*- coding: utf-8 -*-
#TODOS LOS JUEGOS
def FuncionGigante():
	
	cont = 1
	acum = 0
	while cont < 4:
		desea = raw_input ("Para lanzar el %s dado ingrese 'dado'" % cont)
		if desea != "dado":
			continue
		da2 = random.randint (1,6) 
		print da2
		acum = acum + da2
		cont = cont + 1
	return acum


def Atacar (x,y):
	if cpu == "D" and user  == "C": 
		print "Gano CPU"
		result = 1
	elif cpu == "C" and user == "D":	
		print "Gano USER"
		result = 2
	elif cpu == user:
		print "Empate"	
		result = 3
	else: 
		print ("Las acciones ingresadas no son validas")
	return result

def Contragolpear(x,y):
	if cpu == "A" and user  == "D": 
		print "Gano CPU"
		result = 1
	elif cpu == "D" and user == "A":	
		print "Gano USER"
		result = 2
	elif cpu == user:
		print "Empate"	
		result = 3
	else: 
		print ("Las acciones ingresadas no son validas")
	return result

def Defender_Con_Escudo(X,Y):
	if cpu == "C" and user  == "A": 
		print "Gano CPU"
		result = 1
	elif cpu == "A" and user == "C":	
		print "Gano USER"
		result = 2
	elif cpu == user:
		print "Empate"	
		result = 3
	else: 
		print ("Las acciones ingresadas no son validas")
	return result


def shootuser(a, b):
	if user != cpu:
		
		print "GOOOL! de ", equipo
		result = 1
	else:
		print "Penal Atajado por la CPU"
		result = 2
	return result


def atajaruser(a,b):
	if user == cpu:
		print "MUY BIEN!! el arquero de ", equipo, " ha atajado el penal."
		result = 1
	else:
		print "GOOOL del CPU"
		result = 2
	return result









print ""
print ""
print "##############################################################"
print ""
print"                (:    Divertite con Qbits   :)"
print ""
print"#################################S##############################"
print"                                               Hecho por Qbits"
print""
print""
import random
condicion = raw_input ("Queres divertirte con Qbits? S/N: ")
while condicion == "s" or condicion == "S":
	print "**Con cual de todos estos juegos te queres divertir?**\n"
	print "1. El camino del Gigante"
	print "2. Juego de Tronos"
	print "3. Penales"
	print "4. Ahorcado Recargado"
	print "5. AdiviNumero"
	eleccion = raw_input ("")
	if eleccion == "1":
		print ""
		print "-----------------EL GIGANTE-----------------"
		print""
		print "Un gigante quiere llegar a su caverna, para eso debe hacer 10 largos pasos.\n Si la suma de tus tres dados iguala a la cantidad de pasos, el gigante te lo agradecera! "
		desea = raw_input ("Sie animas a ayudar al gigante presiona 'S': ") 
		if desea == "s" or desea == "S": 
				acum = FuncionGigante()
		print "La suma de todos tus dados es:", acum
		if acum == 10:
			print "Felicitaciones!! Hiciste que el gigante llegue a su caverna sano y salvo :) "
			print "................."
			print "Creado por Qbits"
			print "................."
		elif acum < 10:
			print "Que lastima :( El gigante no pudo llegar a su caverna "
			print "................."
			print "Creado por Qbits "
			print "................."
		else:
			print "Nooo :O El gigante se paso de largo cayo a un precipicio"
			print ".................."
			print "Creado por Qbits. "
			print ".................."
		condicion = raw_input ("\nQueres seguir jugando con Qbits? S/N: ")
	elif eleccion =="2":
		print""
		print"------------Juego de Tronos-----------"
		print "En una batalla entre dos caballeros (uno el Jugador, el otro la PC) cada "
		print "caballero tiene la posibilidad de hacer 3 movimientos: Atacar con espada, "
		print "Defenderse con Escudo y Contragolpear con espada. Se juegan 4 rondas y "
		print "gana el jugador con mayor cantidad de puntos. Cada ronda ganada suma 5 " 
		print "puntos, cada ronda perdida resta 5 puntos, cada ronda empatada da a cada  " 
		print "jugador 1 punto.En caso de empate, se puede realizar una ronda de "
		print "desempate. Los movimientos posibles son:"
		print "Atacar con espada: Gana a defenderse con escudo. Pierde con Contragolpear con"
		print "espada."
		print "Contragolpear con espada: Gana a atacar con espada. Pierde contra Defender con"
		print "escudo."
		print "Defender con escudo: Gana a contragolpear con espada. Pierde con Atacar con "
		print "espada."

		cond = raw_input ("Para comenzar la partida presione S, Para salir cualquier tecla:  ").upper()
		puntcpu = 0
		puntuser = 0
		flags = True
		while cond == "S" or flags == False:
			if flags:
					ronda = 5
			else:
					ronda = 1
			while ronda > 0 :
				print ""
				print "Ingrese el movimiento que desea hacer: "
				mov = raw_input ("Atacar A, Defender con escudo D, Contragolpear C :  ").upper()
				if mov == "A":
					cpu = random.choice(['C', 'D',])
					print "Ingrese la accion que desea hacer:"
					user= raw_input ("Defender con escudo D, Contragolpear C ").upper()
					print ""
					if user == "C" or user == "D":
						combate = Atacar(cpu,user)
						if combate == 1:
							puntcpu = puntcpu + 5
						elif combate == 2:
							puntuser = puntuser + 5
						else:
							puntcpu = puntcpu + 1
							puntuser = puntuser + 1
					else:
						print "Ingreaste mal la accion, PRESTA ATENCION e intentalo de nuevo"
						ronda = ronda + 1
				elif mov == "C":
					cpu = random.choice(['A', 'D',])
					print "Ingrese la accion que desea hacer:"
					user= raw_input ("Atacar A, Defender con escudo D ").upper()
					print ""
					if user == "A" or user == "D":
						combate = Contragolpear(cpu,user)	
						if combate == 1:
							puntcpu = puntcpu + 5
						elif combate == 2:
							puntuser = puntuser + 5
						else:
							puntcpu = puntcpu + 1
							puntuser = puntuser + 1		
					else:
						print "Ingreaste mal la accion, PRESTA ATENCION e intentalo de nuevo"
						ronda = ronda + 1
				elif mov == "D":
					cpu = random.choice(['A', 'C',])
					print "Ingrese la accion que desea hacer:"
					user= raw_input ("Atacar A, Contragolpear C ").upper()
					print ""
					if user == "A" or user == "C":
						combate = Defender_Con_Escudo(cpu,user)	
						if combate == 1:
							puntcpu = puntcpu + 5
						elif combate == 2:
							puntuser = puntuser + 5
						else:
							puntcpu = puntcpu + 1
							puntuser = puntuser + 1		
					else:
						print "Ingreaste mal la accion, PRESTA ATENCION e intentalo de nuevo"
						ronda = ronda + 1
				else:
					print ""
					print "Ingreaste mal el movimiento, PRESTA ATENCION e intentalo de nuevo"
					ronda = ronda + 1
				ronda = ronda - 1
			print ""
			print "Tus puntos son: ",puntuser
			print "Los puntos de la cpu son: ",puntcpu
			print ""
			if puntuser == puntcpu:
				print "PARTIDA EMPATADA"
				print "RONDA DE DESEMPATE"
				flags = False
			elif puntuser > puntcpu:
				print "Felicitaciones!! Ganaste la batalla !"
				print ""
				cond = raw_input ("Si deseas seguir jugando presiona S, para salir cualquier tecla ").upper()
				flags = True
				puntcpu = 0
				puntuser = 0
			else:
				print "Perdiste la partida"
				print "Intentalo de nuevo"
				print ""
				cond = raw_input ("Si deseas seguir jugando presiona S, para salir cualquier tecla ").upper()
				flags = True
				puntcpu = 0
				puntuser = 0
		print ""
		print "*****************"
		print "Creado por Qbits"
		print "*****************"
		condicion = raw_input ("Queres seguir jugando con Qbits? S/N: ")
	elif eleccion =="3":

		contgoluser=0
		contgolpc=0
		ronda = 1

		print "------------PENALES------------"
		print "El juego consiste en una serie de penales entre usuario y PC. \nLas direcciones en las que podes tirar y atajar son 1-2-3-4-5-6. \nSi el partido termina en empate, se procedera a patear un penal c/u \nhasta que haya un ganador"
		preg = raw_input("Para iniciar el juego presiona S")
		#equipo = raw_input("Ingrese el nombre de su equipo: ")
		while preg == "S" or preg == "s":
			equipo = raw_input("Ingrese el nombre de su equipo: ")
			print "Bienvenido ", equipo, "!!"
			print " "
			print "1. Para patear arriba-izquierda "
			print "2. Para patear arriba-medio "
			print "3. Para patear arriba-derecha"
			print "4. Para patear abajo-izquierda"
			print "5. Para patear abajo-medio "
			print "6. Para patear abajo-derecha"
			print " "

			while ronda <= 5:
				print "Tanda NRO %s" % ronda
				print " "
				
				user = int(input("Ingresa un numero de 1 a 6 que sera la direccion donde queres PATEAR el penal: "))
				print " "


				cpu = random.randint (1,6)

				if user != cpu:
								shootuser(user,cpu)
								contgoluser = contgoluser + 1
				else:
								shootuser(user,cpu)
				
				print " "			
				print "El resultado parcial es: ", equipo, " ", contgoluser, " - CPU ", contgolpc
				print " "
							
				user = int(input("Ingresa un numero de 1 a 6 que sera la direccion donde queres ATAJAR el penal: "))
				print " "
				cpu = random.randint(1,6)

				if cpu != user:
					atajaruser(cpu, user)
					contgolpc = contgolpc + 1
				else:
					atajaruser(cpu, user)

				print " "	
				print "El resultado parcial es: ", equipo, " ", contgoluser, " - CPU ", contgolpc

				print " "
				print " "
						#print "Tanda NRO %s" % ronda
				print " "
						#print "El resultado parcial es: ", equipo, " ", contgoluser, " - CPU ", contgolpc 
				print " "

				ronda = ronda + 1
			
			
				
			print " "
			print "Resultado final: ", equipo, " ", contgoluser, " - CPU ", contgolpc
			print " "
			if contgoluser > contgolpc:
				print " Felicitaciones!! El ganador es: ", equipo
			elif contgolpc > contgoluser:
				print "EL ganador es la PC"
			else:
				print "No pueden empatar!!"

			print " "
			print ""	
			preg = raw_input("Si queres seguir jugando presiona 'S'... de lo contrario, presiona cualquier tecla: ")
				#equipo = raw_input("Ingrese el nombre de su equipo: ")
			ronda=1
			contgoluser=0
			contgolpc=0
		print " "
		print ""
		print "Creado por Qbits Seguinos en nuestra Fanpage: www.facebook.com/qbits.ar"
		condicion = raw_input ("Queres seguir jugando con Qbits? S/N: ")
			

	elif eleccion == "4":
		print "--------------Ahorcado Recargado-------------"
		intentos = 4
		correcta = 0
		pista = True
		palabra = "MICRO"
		print "Deberas adivinar la palabra. Tendras 4 intentos y la posibilidad de pedir una pista. Si pedis una pista se te resta un intento."
		print ""
		while (intentos != 0):
			letra = str.upper (raw_input ('Ingrese letra: '))
			if letra in palabra:
				print 'Letra correcta!\n'
				correcta += 1
			else:
				intentos -= 1
				print 'Letra incorrecta.'
				print 'Le restan %d intentos' % (intentos)
				pista = raw_input ('Solicitar pista?: (1: Si / 0: No): ')
				if (pista):
					print 'La palabra termina con la letra O.'
					pista = False
					intentos -= 1
					print 'Perdiste un intento. Te quedan %d' % (intentos)
			if (intentos == 0):
				print "\nGame Over! Se terminaron los intentos."
				print "La palabra es %s" % (palabra)
			if (correcta == 5):
				print "Felicidades!! Acertaste todas las letras."
				print "La palabra formada es %s" % (palabra)
		print"\nCreado por Qbits. Seguinos en nuestra Fanpage: www.facebook.com/qbits.ar"
		condicion = raw_input ("Queres seguir jugando con Qbits? S/N: ")

	elif eleccion =="5":
		print("******************************************\n")
		print("\tA d i v i N u m e r o")
		print("******************************************\n")
		print("Estoy pensando en un numero del 1 al 100 \nCual sera?\n")
		print("Tenes 5 oportunidades para adivinarlo\n")
		respuesta=raw_input("Te animas? S/N\n")
		if respuesta=='S' or respuesta == "s":
			print("Bien.\nEl mundo es de los valientes!")
			x= random.random()
			minumero=int(x*100)
			
			intentos=0
			while intentos != minumero or intentos<5:
				intentos=intentos+1
				tunumero=int(input("Estoy pensando en el numero...?\n"))
				
				if tunumero==minumero:
					print("Hazzz azertado tio!, Felizitaziones. !\n")
					
				else:
					print("Intentalo de nuevo.\n ")
					
					
				if tunumero != minumero and intentos==5:
					print("Chauuuu chauuuu chauuuuu. Hazzz perdido !\n El numero era %d "%(minumero))
					break
				
		else:
			print("Juira .")
		print("Juego creado por Qbits. Seguinos en nuestra Fanpage: www.facebook.com/qbits.ar\n")
		condicion = raw_input ("Queres seguir jugando con Qbits? S/N: ")