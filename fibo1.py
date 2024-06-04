# Series de Fibonacci:
# la suma de dos elementos define el siguiente

def ingresar_tope():
    '''Solicita al operador un número para la serie de fibo'''
    numero = input('ingrese un valor numérico límite:')
    return int(numero)

def fibo(limite): 
    """Devuelve una lista conteniendo la serie de Fibonacci hasta cierto límite."""
    sucesion = []
    a, b = 0, 1
    while a < limite:
        sucesion.append(a) # ver abajo
        a, b = b, a+b
        return sucesion
    
# Cuerpo principal del programa   
tope = ingresar_tope() 
resultado = fibo(tope) 
print(resultado)

ejecuciones = 0
while True:
    borrar_pantalla()
    limite = ingresar_tope()
    if not limite:
        break
    sucesion = fibonacci(limite)
    mostrar_serie(sucesion)
    ejecuciones += 1
    pausar('pulse <ENTER> para otra serie.')

borrar_pantalla()
print('ud ha solicitado', ejecuciones,'sucesiones de Fibonacci, gracias por utilizar este programa') 