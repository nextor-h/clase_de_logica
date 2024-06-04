from os import system

def borrar_pantalla():
    '''Borra la pantalla de la terminal en sistema operativo Linux'''
    system('clear')
    return

def ingresar_texto():
      '''permite que el operador ingrese un texto y lo procesa'''
      entrada = input('Introduzca un texto: ').upper().strip()
      return entrada

while True:
       borrar_pantalla()
       cartel = ingresar_texto()
       largo = len(cartel)

       if largo == 0:
          break
       cartel_dos = ''
       cartel_tres = '╔═════'  
       cartel_cuatro = cartel_tres * len(cartel)
       cartel_cinco = '╚═════'
       cartel_cinco = cartel_cinco * len(cartel)
       for letra in cartel:
                cartel_dos +='║  ' + letra + '  '
       print(cartel_cuatro + '╗' + '\n' + cartel_dos + '║' + '\n' + cartel_cinco+ '╝')
       print()
       nada = input ('pulse <ENTER> para retornar')