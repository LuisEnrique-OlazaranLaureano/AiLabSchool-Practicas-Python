'''
Práctica 1.
Crear un programa que solicite el ingreso de números 
enteros positivos, hasta que el usuario ingrese el 0.
Por cada número, informar cuántos dígitos pares y cuántos 
impares tiene. Al finalizar, informar la cantidad de dígitos 
pares y de dígitos impares leídos en total.
#Luis Enrique Olazarán Laureano
'''
num = 1
pares = []
impares = []

while True:
	try:
		num = int(input("Ingresa un dato numerico: "))
		if num == 0:
			break
	except:
		print("No se permiten (Letras/Palabras/Caracteres Especiales)")
		continue

	if(num % 2 == 0):
		pares.append(num)
	else:
		impares.append(num)


print("Cantidad de dígitos pares:", len(pares))
print(pares)
print("Cantidad de dígitos impares:", len(impares))
print(impares)

