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

persona1= Persona(nombre, 560)
persona2 = Persona("Milagros", 790)

# Mostrar saldo inicial
persona1.mostrar_saldo()
persona2.mostrar_saldo()

# Realizar una tranferencia
monto_transferencia = float(input("Ingrese el monto a transferir: "))
persona1.transferencia(monto_transferencia, persona2)

# Mostrar saldo después de la transferencia
persona1.mostrar_saldo()
persona2.mostrar_saldo()






