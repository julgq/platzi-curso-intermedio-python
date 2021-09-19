
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


if __name__ == '__main__':
	run()