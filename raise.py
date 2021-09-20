if __name__ == '__main__':
    try:
        if len("") == 0:
            raise ValueError("No se puede ingresar una cadena vacia")
        print('sin error')
    except ValueError as ve:
        print(ve)
        

