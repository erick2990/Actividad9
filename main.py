clientes = {} #Diccionario vacio de clientes



def ingreso_viajero():
    cantidad_destinos = 0 #se inicializa para que esta variable sea local y pueda usarse

    cantidad = int(input('Ingrese cuantos viajeros desea registrar: '))
    for i in range(1, cantidad+1):
        print(f'Ingrese datos del {i} viajer@: ')
        codigo = input('Ingrese el codigo del cliente: ')
        clientes[codigo] = {
              "nombre" :  input('Ingrese el nombre del cliente: '),
              "destinos" : {}
        }

        paso  = True
        while paso:
            cantidad_destinos = int(input('Ingrese la lista de destinos turisticos minimo 1 maximo 5: '))
            if 1<=cantidad_destinos<=5:
                paso = False
                break
            else:
                print('Solo puede ser un minimo de 1 destino o maximo 5')

        for j in range(1, cantidad_destinos+1):
            print(f'Ingrese los datos del {i} destino')
            n_destino = input('Ingrese el numero de destino segun el mapa: ')
            nombre_destino = input('Ingrese el nombre del destino: ')
            clientes[codigo]["destinos"][n_destino] = {
                "nombre_lugar" : nombre_destino
            }
def mostrar_viajeros(codigos):
    if not codigos:
        return 0 #Aqui es donde finaliza el diccionario
    codigo_unico = codigos[0] #se extrae el primer codigo del diccionario y luego se vuelve a referenciar
    tmp = clientes[codigo_unico] #este cliente es temporal y debe tener los datos del primer cliente
    print(f'\nCodigo: {codigo_unico}')
    print(f'Cliente: {tmp["nombre"]}')
    for




fin_menu = True

while fin_menu:
    print('1.Ingresar viajeros \r\n2.Mostrar viajeros \r\n3.Salir')
    opcion = int(input('Seleccione la opcion que desea: '))

    match opcion:
        case 1:
            ingreso_viajero()
        case 2:

            mostrar_viajeros(clientes.items())

        case 3:
            print('Gracias por usar el sistema')
            fin_menu = False
        case _:
            print('error ingreso un dato incorrecto')
