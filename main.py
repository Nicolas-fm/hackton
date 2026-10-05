class Tutores:
    def __init__(self, nombre, clases):
        self.nombre = nombre
        self.clases = clases

    def __str__(self):
        return f"{self.nombre} - Clases: {', '.join(self.clases)}"


class Estudiantes:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clases = []

    def __str__(self):
        return self.nombre


class Clases:
    def __init__(self, dia, nombre_clase):
        self.dia = dia
        self.nombre_clase = nombre_clase    
        self.limite = 10
        self.personas = []
        self.lista_espera = []

    def inscribir(self, estudiante):
        if estudiante in self.personas or estudiante in self.lista_espera:
            return "El estudiante ya está inscrito o en la lista de espera."

        if len(self.personas) < self.limite:
            self.personas.append(estudiante)
            estudiante.clases.append(self.nombre_clase)
            return f"{estudiante.nombre} quedó inscrito en la clase."

        self.lista_espera.append(estudiante)
        return f"La clase está llena. {estudiante.nombre} quedó en la lista de espera."

    def retirar(self, estudiante):
        if estudiante not in self.personas:
            return "El estudiante no está inscrito en esta clase."

        self.personas.remove(estudiante)
        estudiante.clases.remove(self.nombre_clase)

        if self.lista_espera:
            siguiente = self.lista_espera.pop(0)
            self.personas.append(siguiente)
            siguiente.clases.append(self.nombre_clase)
            return (
                f"{estudiante.nombre} salió de la clase. "
                f"{siguiente.nombre} pasó de la lista de espera a la clase."
            )

        return f"{estudiante.nombre} salió de la clase. El puesto quedó libre."

    def __str__(self):
        return (
            f"{self.nombre_clase} ({self.dia}) - "
            f"Cupos: {len(self.personas)}/{self.limite} - "
            f"Lista de espera: {len(self.lista_espera)}"
        )


estudiantes = []
tutores = []
clases = []


def elegir(lista, mensaje):
    if not lista:
        print("No hay opciones disponibles.")
        return None

    for numero, elemento in enumerate(lista, start=1):
        print(f"{numero}. {elemento}")

    try:
        opcion = int(input(mensaje)) - 1
    except ValueError:
        print("Ingrese un número válido.")
        return None

    if opcion < 0 or opcion >= len(lista):
        print("Opción inválida.")
        return None
    return lista[opcion]


def menu():
    while True:
        print("\nSistema de clases")
        print("1. Crear estudiante")
        print("2. Crear tutor")
        print("3. Crear clase")
        print("4. Inscribir estudiante")
        print("5. Retirar estudiante y liberar cupo")
        print("6. Ver estudiantes, tutores y clases")
        print("7. Salir")

        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre del estudiante: ").strip()
            if nombre:
                estudiantes.append(Estudiantes(nombre))
                print(f"Estudiante {nombre} creado.")
            else:
                print("El nombre no puede estar vacío.")

        elif opcion == "2":
            nombre = input("Nombre del tutor: ").strip()
            clases_tutor = input("Clases que imparte, separadas por coma: ")
            lista_clases = []
            for clase in clases_tutor.split(","):
                clase = clase.strip()
                if clase:
                    lista_clases.append(clase)
            if nombre:
                tutores.append(Tutores(nombre, lista_clases))
                print(f"Tutor {nombre} creado.")
            else:
                print("El nombre no puede estar vacío.")

        elif opcion == "3":
            nombre = input("Nombre de la clase: ").strip()
            dia = input("Día de la clase: ").strip()
            if nombre and dia:
                clases.append(Clases(dia, nombre))
                print(f"Clase {nombre} creada.")
            else:
                print("El nombre y el día son obligatorios.")

        elif opcion == "4":
            estudiante = elegir(estudiantes, "Elija el estudiante: ")
            if estudiante:
                clase = elegir(clases, "Elija la clase: ")
                if clase:
                    print(clase.inscribir(estudiante))

        elif opcion == "5":
            clase = elegir(clases, "Elija la clase: ")
            if clase:
                estudiante = elegir(clase.personas, "Elija el estudiante que saldrá: ")
                if estudiante:
                    print(clase.retirar(estudiante))

        elif opcion == "6":
            print("\nEstudiantes:")
            for estudiante in estudiantes:
                clases_estudiante = ", ".join(estudiante.clases) or "Ninguna"
                print(f"- {estudiante.nombre} - Clases: {clases_estudiante}")

            print("\nTutores:")
            for tutor in tutores:
                print(f"- {tutor}")

            print("\nClases:")
            for clase in clases:
                print(f"- {clase}")
                if clase.lista_espera:
                    nombres = ""
                    for estudiante_espera in clase.lista_espera:
                        if nombres:
                            nombres += ", "
                        nombres += estudiante_espera.nombre
                    print(f"  En espera: {nombres}")

        elif opcion == "7":
            print("Gracias por usar el sistema.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
