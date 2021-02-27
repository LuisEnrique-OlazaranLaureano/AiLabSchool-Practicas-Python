'''
Práctica 3.
Leer números enteros de teclado, hasta que el usuario ingrese el 0.
Finalmente, mostrar la sumatoria de todos los números positivos 
ingresados
#Luis Enrique Olazarán Laureano
'''
sumatoria = 0
while(True):
	try:
		numeros = int(input("Ingrese numeros enteros: "))
	except:
		print("No se permiten (Letras/Palabras/Caracteres Especiales)")
		continue	

	if(numeros == 0):
		break
	sumatoria += numeros
print("La sumatoria es: ", sumatoria)