def programa():
    print("¡Bienvenido al programa!")

    continuar = 's'
    # la funcion "lower" sirve para convertir la cadena en letras minusculas, sin importar como se ingreso el texto
    while continuar.lower() == 's':
        nombre = input("Por favor, ingresa tu nombre: ")
        apellido = input("Ahora, ingresa tu apellido: ")
        dni= input("Ingresa tu numero de documento: ")

        print("\nHola,", nombre, apellido + "!")

        edad = int(input("\nIngresa tu edad: "))
        if edad >= 18:
            print("¡Eres mayor de edad!")
        else:
            print("Eres menor de edad.")

        # Uso de lista
        numeros = []
        for i in range(4):
            #la funcion "RANGE" indica la cantidad de elementos en la lista
            numero = int(input("\nIngresa un número entero: "))
            numeros.append(numero)

        print("\nLos números que ingresaste son:", numeros)

        # Uso de tupla
        tupla = tuple(numeros)
        print("Tupla creada a partir de los números ingresados:", tupla)

        # Uso de diccionario
        diccionario = {'nombre': nombre, 'apellido': apellido, 'edad': edad, 'numeros': numeros}
        print("\nDiccionario creado con los datos ingresados:", diccionario)

        # Suma de los números ingresados
        suma_numeros = sum(numeros)
        print("La suma de los números ingresados es:", suma_numeros)

        # Verificar si la suma es par o impar
        if suma_numeros % 2 == 0:
            print("La suma de los números es par.")
        else:
            print("La suma de los números es impar.")

        continuar = input("\n¿Deseas continuar? (s/n): ")

    print("\n¡Gracias por utilizar el programa interactivo!")

if programa ():
    print("¡Bienvenido al programa!")