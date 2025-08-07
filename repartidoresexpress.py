class Repartidor:
    def __init__(self, nombre, paquetes, zona):
        self.nombre = nombre
        self.paquetes = paquetes
        self.zona = zona

    def __str__(self):
        return f'{self.nombre} - {self.paquetes} Paquetes - Zona: {self.zona}'


class EmpresaMensajera:
    def __init__(self, repartidores):
        self.repartidores = []

    def agregar_repartidores(self, repartidor):
        if not repartidor.nombre == "":
            print("Error: Nombre inválido.")
            return False
        if repartidor.paquetes < 0:
            print("Error: Paquetes deben ser un entero positivo.")
            return False
        if not repartidor.zona == "":
            print("Error: Zona inválida.")
            return False

        if self.busqueda_de_valor(repartidor.nombre) is not None:
            print(f"Error: Ya existe repartidor con nombre '{repartidor.nombre}'.")
            return False
        self.repartidores.append(repartidor)
        return True

    def repartidores_repetidos(self, nombre):
        while True:
            if nombre in self.repartidores:
                print("Este nombre ya existe")
            else:
                break

    def ordenar_por_paquetes(self):
        def quick_sort(lista):
            if len(lista) <= 1:
                return lista

            pivote = lista[0]
            mayores = [x for x in lista[1:] if x.paquetes > pivote.paquetes]
            menores = [x for x in lista[1:] if x.paquetes < pivote.paquetes]

            return quick_sort(mayores) + [pivote] + quick_sort(menores)

        self.repartidores = quick_sort(self.repartidores)

    def busqueda_de_valor(self, nombre):
        for elemento in self.repartidores:
            if elemento == nombre:
                return elemento
        return None


mensajeria = {}
print("=== Rendimiento repartidores ===")
