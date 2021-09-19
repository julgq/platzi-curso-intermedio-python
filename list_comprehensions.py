
def run():
	squares = []

	# Obtener una lists de los 100 primeros numeros naturales elevados al cuadrado
	# los que no son divisibles entre 3
	for i in range(1, 101):
		if i % 3 !=0: 
			squares.append(i**2)

	print(squares)
	print('\n')


	# solución con list comprehensions, la misma solución pero con list comprenhensions:
	squares_comprenhension = [i**2 for i in range(1, 101) if i % 3 != 0]
	print(squares_comprenhension)
	print('\n')

	# RETO: Crear un list comprehension, 
	# una lista de todos los múltiplos de 4 que la vez también  
	# son múltiplos de 6 y de 9, hasta 5 dígitos.

	squares_reto = [i for i in range(1, 501) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
	print(squares_reto)


if __name__ == '__main__':
	run()