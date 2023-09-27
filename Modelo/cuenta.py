class Cuenta:
    def __init__(self, cuenta, identificacion, nombre_usuario, saldo_usuario):
        self.__numero_cuenta = cuenta
        self.__documento_identidad = identificacion
        self.__nombre = nombre_usuario
        self.__saldo = saldo_usuario

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @property
    def documento_identidad(self):
        return self.__documento_identidad

    @documento_identidad.setter
    def documento_identidad(self, identificacion):
        self.__documento_identidad = identificacion

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre_usuario):
        self.__nombre = nombre_usuario

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo_usuario):
        self.__saldo = saldo_usuario

    def mostrar_datos(self):
        print("Número de cuenta: " + str(self.__numero_cuenta))
        print("Documento de Identidad: " + str(self.__documento_identidad))
        print("Nombre: " + str(self.__nombre))
        print("Saldo: $" + str(self.__saldo))

    def retirarDinero(self, retiro):
        self.__saldo -= retiro

    def depositarDinero(self, deposito):
        self.__saldo += 0.81 * deposito
