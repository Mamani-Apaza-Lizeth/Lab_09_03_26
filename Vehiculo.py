class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __lt__(self, otro):
        """Sobrecarga del operador < (menor que) por precio."""
        if not isinstance(otro, Vehiculo):
            return NotImplemented
        return self.precio < otro.precio

    def __eq__(self, otro):
        """Sobrecarga del operador == por marca y modelo."""
        if not isinstance(otro, Vehiculo):
            return NotImplemented
        return self.marca == otro.marca and self.modelo == otro.modelo

    def mostrar(self):
        print(f"{self.marca} {self.modelo} - ${self.precio}")


class Coche(Vehiculo):
    def __init__(self, marca, modelo, precio, num_puertas):
        super().__init__(marca, modelo, precio)
        self.num_puertas = num_puertas

    def mostrar(self):
        super().mostrar()
        print(f"Puertas: {self.num_puertas}")


class Moto(Vehiculo):
    def __init__(self, marca, modelo, precio, cilindrada):
        super().__init__(marca, modelo, precio)
        self.cilindrada = cilindrada

    def mostrar(self):
        super().mostrar()
        print(f"Cilindrada: {self.cilindrada} cc")

# Demostración
if __name__ == "__main__":
    coche1 = Coche("Toyota", "Corolla", 20000, 4)
    coche2 = Coche("Honda", "Civic", 22000, 4)
    moto1 = Moto("Yamaha", "MT-07", 7500, 689)

    # Uso de operadores sobrecargados
    print(coche1 < coche2)   
    print(coche1 == coche2) 

    coche3 = Coche("Toyota", "Corolla", 25000, 4)
    print(coche1 == coche3)  

    print(moto1 < coche1)    