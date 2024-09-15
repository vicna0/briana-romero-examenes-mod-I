class Cuenta:
    tasa_conversion = 3.77  # Tasa de conversión de dólares a soles

    def __init__(self, nombre, apellido, saldo_soles=0, saldo_dolares=0):
        self.nombre = nombre
        self.apellido = apellido
        self.saldo_soles = saldo_soles
        self.saldo_dolares = saldo_dolares

    def transferir(self, cantidad, desde, hacia):
        if desde == 'soles' and hacia == 'dolares':
            if self.saldo_soles < cantidad:
                print("No hay suficientes fondos en soles para la transferencia.")
                return
            self.saldo_soles -= cantidad
            self.saldo_dolares += cantidad / Cuenta.tasa_conversion
        elif desde == 'dolares' and hacia == 'soles':
            if self.saldo_dolares < cantidad:
                print("No hay suficientes fondos en dólares para la transferencia.")
                return
            self.saldo_dolares -= cantidad
            self.saldo_soles += cantidad * Cuenta.tasa_conversion
        else:
            print("Tipo de transferencia no válido. Usa 'soles' o 'dolares'.")
            return
        self.mostrar_saldos()

    def retirar(self, cantidad, tipo):
        if tipo == 'soles':
            if self.saldo_soles < cantidad:
                print("No hay suficientes fondos en soles para el retiro.")
                return
            self.saldo_soles -= cantidad
        elif tipo == 'dolares':
            if self.saldo_dolares < cantidad:
                print("No hay suficientes fondos en dólares para el retiro.")
                return
            self.saldo_dolares -= cantidad
        else:
            print("Tipo de cuenta no válido. Usa 'soles' o 'dolares'.")
            return
        self.mostrar_saldos()

    def mostrar_saldos(self):
        print(f"Saldo en soles: {self.saldo_soles:.2f}")
        print(f"Saldo en dólares: {self.saldo_dolares:.2f}")


nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))

print("Bienvenido/a {} {}".format(nombre, apellido))
print("Tus saldos son los siguientes, saldo_soles = 200  y tu saldo_dolares = 600")

cuenta = Cuenta("nombre", "apellido", saldo_soles=200, saldo_dolares=600)

print("Transferencia 1:")
cuenta.transferir(800, 'soles', 'dolares')

print("Transferencia 2:")
cuenta.transferir(3, 'dolares', 'soles')

print("Retiro 1:")
cuenta.retirar(780, 'soles')
