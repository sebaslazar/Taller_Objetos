from os import system


def pantalla_de_inicio():
    system('cls')
    print("+------------------------------------------------------------+")
    print("| BIENVENIDO A NUESTRA APLICACIÓN DE ADMINISTRACIÓN BANCARIA |")
    print("+------------------------------------------------------------+")


def login(cuentaclientes):
    check = True
    if not cuentaclientes:
        print("**NO HAY CUENTAS REGISTRADAS**\n")
    print("OPCIONES:")
    if cuentaclientes:
        print("  1. Depositar dinero")
        print("  2. Retirar dinero")
        print("  3. Mostrar datos de cuenta")
        print("  4. Registrar nueva cuenta")
        print("  5. Salir\n")
    else:
        print("  1. Registrar nueva cuenta")
        print("  2. Salir\n")
    while check:
        try:
            respuesta = int(input("¿Qué desea hacer?: "))
            if (cuentaclientes and (respuesta > 5 or respuesta < 0)) or (
                    not cuentaclientes and (respuesta < 1 or respuesta > 2)):
                mensajes(1)
            else:
                check = False
        except ValueError:
            mensajes(6)
    system('cls')
    return respuesta


def registrar():
    print("\n")
    try:
        numero_cuenta = int(input("Número de cuenta: "))
        identificacion = int(input("Documento de identidad: "))
        nombre_usuario = input("Nombre del cliente: ")
        system('cls')
        return numero_cuenta, identificacion, nombre_usuario
    except ValueError:
        system('cls')
        return -1, -1, -1


def elegir_cuenta(cuentaclientes):
    check = True
    numerador = 1
    print("**CUENTAS REGISTRAS**\n")
    for cuenta in cuentaclientes:
        print("-->" + str(numerador) + ") Documento de identidad: " + str(cuenta.documento_identidad))
        print("      Nombre del cliente: " + str(cuenta.nombre) + "\n")
        numerador += 1
    while check:
        try:
            respuesta = int(input("¿Cuál cuenta desea elegir?: "))
            if respuesta > len(cuentaclientes) or respuesta < 1:
                mensajes(1)
            else:
                check = False
        except ValueError:
            mensajes(6)
    system('cls')
    return respuesta-1


def verificar_fondos(saldo_cuenta):
    print("Saldo disponible: $" + str(saldo_cuenta) + "\n")
    try:
        retiro = int(input("¿Cuánto desea retirar?: "))
        system('cls')
        if saldo_cuenta - retiro < 0:
            return retiro, False
        else:
            return retiro, True
    except ValueError:
        return -1, False


def depositar(saldo_cuenta):
    print("Saldo actual: $" + str(saldo_cuenta) + "\n")
    try:
        deposito = int(input("¿Cuánto desea depositar a esta cuenta?: "))
    except ValueError:
        deposito = -1
    system('cls')
    return deposito


def mensajes(identificador):
    if identificador == 0:
        print("\n\n")
        print("+-----------------------------------+")
        print("| PROGRAMA FINALIZADO. HASTA PRONTO |")
        print("+-----------------------------------+\n")
    elif identificador == 1:
        print("\n  **ERROR: OPCIÓN INVÁLIDA**\n")
    elif identificador == 2:
        print("\n  **ERROR: LA CUENTA ELEGIDA NO TIENE FONDOS**\n")
    elif identificador == 3:
        print("\n  **ERROR: FONDOS INSUFICIENTES PARA RETIRO**\n")
    elif identificador == 4:
        print("\n\n")
        print("+----------------------------+")
        print("| RETIRO REALIZADO CON ÉXITO |")
        print("+----------------------------+\n")
    elif identificador == 5:
        print("\n\n")
        print("+------------------------------+")
        print("| DEPÓSITO REALIZADO CON ÉXITO |")
        print("+------------------------------+\n")
    elif identificador == 6:
        print("\n  **ERROR: TIPO DE DATO INVÁLIDO**\n")
