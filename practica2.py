'''
Práctica 2.
Mostrar un menú con tres opciones: 
1- comenzar programa, 
2- imprimir listado, 
3- finalizar programa. 
A continuación, el usuario debe poder seleccionar 
una opción (1, 2 ó 3). Si elige una opción incorrecta, 
informarle del error. El menú se debe volver a mostrar
luego de ejecutada cada opción, permitiendo volver a elegir.
Si elige las opciones 1 ó 2 se imprimirá un texto. 
Si elige la opción 3, se interrumpirá la impresión del menú 
y el programa finalizará.
#Luis Enrique Olazarán Laureano
'''
frutas = ["Manzana", "Pera", "Sandia", "Coco", "Tuna"]

while(True):	
	print("1.- Comenzar Programa \n2.- Imprimir listado \n3.- Finalizar programa ")
	
	try:
		opcion = int(input("Elige una opcion: "))
	except:
		print("Opcion Incorrecta o Dato Incorrecto")

	if opcion == 1:
		print("Programa Inicializado Hello World!")
	elif opcion == 2:
		print("Imprimiendo Listado de frutas: ", frutas)
	elif opcion == 3:
		print("Fin del Programa")
		break
	else:
		print("No existe esa opcion")
