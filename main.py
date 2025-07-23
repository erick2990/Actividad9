clientes = {} #Diccionario vacio de clientes



def ingreso_viajero():
    cantidad_destinos = 0 #se inicializa para que esta variable sea local y pueda usarse

    cantidad = int(input('Ingrese cuantos viajeros desea registrar: '))
    for i in range(1, cantidad+1):
        print(f'Ingrese datos del {i} viajer@: ')
        codigo = input('Ingrese el codigo del cliente: ')
        clientes[codigo] = {

            ["nombre"] = input('Ingrese el nombre del cliente: ')
        }
        clientes[codigo]["destinos"] = [] #"lista vacia de viajes"
        paso  = True
        while paso:
            cantidad_destinos = int(input('Ingrese la lista de destinos turisticos minimo 1 maximo 5: '))
            if 1<=cantidad_destinos<=5:
                paso = False
                break
            elif cantidad_destinos<0:
                print('Si no hay destinos entonces no se puede guardar el registro vuelva a intentarlo...')
            elif cantidad_destinos>5:
                print('Solo puede ser un minimo de 1 destino o maximo 5')

        for j in range(1, cantidad_destinos+1):
            print(f'Ingrese los datos del {i} destino')
            nombre_destino = input('Ingrese el nombre del destino: ')
            clientes[codigo]["destinos"] = {
                "destino" : nombre_destino
            }



fin_menu = True

while fin_menu:
    print('1.Ingresar viajeros \r\n2.Mostrar viajeros \r\n3.Salir')
    opcion = int(input('Seleccione la opcion que desea: '))

    match opcion:
        case 1:
            ingreso_viajero()
        case 2:
            print('ola')
            #mostrar_viajero()

        case 3:
            print('Gracias por usar el sistema')
            fin_menu = False
        case _:
            print('error ingreso un dato incorrecto')
