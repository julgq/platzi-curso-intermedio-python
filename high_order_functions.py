
from functools import reduce

def run():

	# FILTER
	# obtener una lista con los numeros impares de otra lista
	# resolverlo con list comprehensions
	my_list = [1, 4, 5, 6, 9, 13, 19, 21]
	odd = [i for i in my_list if i % 2 !=0]
	print(odd)
	print("\n")

	# filter
	# resolver el problema anterior con filter y lambda
	odd = list(filter(lambda x: x%2 != 0, my_list))
	print(odd)
	print("\n")


	# MAP
	# Convertir una lista pero con los números elevados al cuadrado
	# resolverlo con list comprehensions
	my_list = [1,2,3,4,5]
	squares = [i**2for i in my_list]
	print(squares)
	print("\n")

	# map
	# resolver el problema anterior con map y lambda
	squares = list(map(lambda x: x**2, my_list))
	print(squares)
	print("\n")

	# REDUCE
	# Tengo una lista y requiere reducirse, en este caso multiplicar los numeros de la lista

	# for
	# resolverlo de una forma tradicional
	my_list = [2, 2, 2, 2, 2]
	all_multiplied = 1

	for i in my_list:
		all_multiplied = all_multiplied * i

	print(all_multiplied)

	# reduce
	# resolverlo con reduce
	# el parametro a y b son los primeros 2 elementos de la lista en la primer iteración
	# en la siguiente iteración a es el resultado de la primer multiplicación y b el siguiente elemento
	all_multiplied = reduce(lambda a,b: a*b, my_list)

	print(all_multiplied)


if __name__ == '__main__':
	run()
