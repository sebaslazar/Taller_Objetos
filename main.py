from UI import menu as ui
from Modelo.cuenta import Cuenta


def main():
    cuentaClientes = []
    ejecutar = True
    ui.pantalla_de_inicio()
    while ejecutar:
        respuesta = ui.login(cuentaClientes)
        if (respuesta == 2 and not cuentaClientes) or (respuesta == 5 and cuentaClientes):
            ui.mensajes(0)
            ejecutar = False
        elif (respuesta == 1 and not cuentaClientes) or (respuesta == 4 and cuentaClientes):
            numero_cuenta, identificacion, nombre_usuario = ui.registrar()
            if numero_cuenta < 0 and identificacion < 0 and nombre_usuario < 0:
                ui.mensajes(6)
            else:
                cuentaClientes.append(Cuenta(numero_cuenta, identificacion, nombre_usuario, 0))
        elif respuesta == 3:
            cuenta_elegida = cuentaClientes[ui.elegir_cuenta(cuentaClientes)]
            cuenta_elegida.mostrar_datos()
        elif respuesta == 2:
            cuenta_elegida = cuentaClientes[ui.elegir_cuenta(cuentaClientes)]
            if cuenta_elegida.saldo <= 0:
                ui.mensajes(2)
            else:
                retiro, verificador_retiro = ui.verificar_fondos(cuenta_elegida.saldo)
                if retiro >= 0 and not verificador_retiro:
                    ui.mensajes(3)
                elif retiro < 0 or not verificador_retiro:
                    ui.mensajes(6)
                else:
                    cuenta_elegida.retirarDinero(retiro)
                    ui.mensajes(4)
        elif respuesta == 1:
            cuenta_elegida = cuentaClientes[ui.elegir_cuenta(cuentaClientes)]
            deposito = ui.depositar(cuenta_elegida.saldo)
            if deposito < 0:
                ui.mensajes(6)
            else:
                cuenta_elegida.depositarDinero(deposito)
                ui.mensajes(5)


main()
