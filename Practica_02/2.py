class Persona:
    def __init__(self, nombre, saldo=0):
        self.nombre = nombre
        self.saldo = saldo

    def transferencia(self, monto, persona_destino):
        if self.saldo >= monto:
            self.saldo -= monto
            persona_destino.saldo += monto
            print(f"Transferencia de {monto} realizada a {persona_destino.nombre}.")
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"El saldo de {self.nombre} es {self.saldo}.")


nombre = str(input("Ingrese el nombre: "))
print("Bienvenido/a {}".format(nombre))
print("Tus saldo es el siguiente, saldo = 560")

nombre = Persona("nombre", 560)
persona2 = Persona("Milagros", 790)

# Saldos iniciales
nombre.mostrar_saldo()
persona2.mostrar_saldo()

# Realizar una transferencia
nombre.transferencia(300, persona2)

# Mostrar los saldos después de la transferencia
nombre.mostrar_saldo()
persona2.mostrar_saldo()

# Tiene saldo insuficiente
nombre.transferencia(800, persona2)





