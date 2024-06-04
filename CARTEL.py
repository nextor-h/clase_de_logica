cartel = input('Introduzca un texto: ')
if cartel:
        cartel_dos = ''
        cartel_tres = '+-----'
        cartel_cuatro = cartel_tres * len(cartel)
        for letra in cartel:
                cartel_dos +='|  ' + letra + '  '
        print(cartel_cuatro + '+' + '\n' + cartel_dos + '|' + '\n' + cartel_cuatro+ '+')