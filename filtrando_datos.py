DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
	# obtener los nombres de los programadores que utilizan python
	all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]

	for worker in all_python_devs:
		print(worker)
	print("\n")

	# obtener todos los trabajadores de platzi
	all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == "Platzi"]

	for worker in all_platzi_workers:
		print(worker)
	print("\n")

	# una lista con todos los adultos
	# generamos un filter para obtener solo los mayores a 18.
	adults = list(filter(lambda worker: worker["age"] > 18, DATA))
	# generamos un map para solo extraer el valor de llave nombre
	adults = list(map(lambda worker: worker["name"], adults))

	for worker in adults:
		print(worker)
	print("\n")

	# generar una lista de diccionarios, pero con un elemento llamado old, el cual tenga una validación de true or false, en caso de ser mayor a 70
	# el pipe solo funciona en python 3.9
	old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

	for worker in old_people:
		print(worker)
	print("\n")



if __name__ == '__main__':
	run()