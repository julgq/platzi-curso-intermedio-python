import math

def run():
	# crear un diccionario con los numeros que no sean divisibles entre 3.
	my_dict = {}

	for i in range(1, 101):
		if i % 3 !=0:
			my_dict[i] = i**3

	print(my_dict)
	print("\n")

	# solución con dictionary comprehensions:
	my_dict = {i: i**3 for i in range(1, 101) if i % 3 !=0}
	print(my_dict)
	print("\n")
	print("\n")

	# RETO: Crear un dictionary comprehensions: 
	# cuyas llaves sean  los 1000 primeros números naturales con sus raíces cuadradas
	# como valores

	my_dict_reto = {i:math.sqrt(i) for i in range(1, 101)}
	print(my_dict_reto)
	print("\n")



if __name__ == '__main__':
	run()

