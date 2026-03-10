class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar_info(self, detallado=False):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")
        if detallado:
            if self.edad >= 18:
                print("Es mayor de edad.")
            else:
                print("Es menor de edad.")
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def mostrar_info(self, detallado=False, incluir_carrera=False):
        Persona.mostrar_info(self, detallado)

        if incluir_carrera:
            print(f"Carrera: {self.carrera}")
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def mostrar_info(self, prefijo=None):
        if prefijo is not None:
            print(f"{prefijo} {self.nombre} ({self.edad} años) - {self.materia}")
        else:
            super().mostrar_info()
            print(f"Materia: {self.materia}")
if __name__ == "__main__":
    p = Persona("Ana", 25)
    p.mostrar_info()
    p.mostrar_info(detallado=True)

    e = Estudiante("Luis", 20, "Ingenieria")
    e.mostrar_info()
    e.mostrar_info(detallado=True, incluir_carrera=True)

    prof = Profesor("Carlos", 40, "Matematicas")
    prof.mostrar_info()
    prof.mostrar_info(prefijo="Profesor:")