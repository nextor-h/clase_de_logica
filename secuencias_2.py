def ingresar_dato(mensaje):
    '''Permite el ingreso de un dato y valida que sea numérico'''
    while True: 
        numero = input (mensaje)
        try:
            numero = int(numero)
            break
        except:
            print('Tipo de dato incorrecto')
            continue
    return numero

def mostrar_secuencia(s):
    for iterador in s:
        print(iterador)
    return    

    #cuerpo principal el programa
valor_inicial = input('Ingrese el valor numerico inicial: ')
valor_final = ingresar_dato('Ingrese el valor numérico final: ')
salto = ingresar_dato ('Ingrese salto: ')
secuencia = range(valor_inicial, valor_final, salto)
mostrar_secuencia(secuencia)
archivo = open('secuencia.txt', 'x')
for valor in secuencia:
    archivo.write(str(valor))
archivo.close()
