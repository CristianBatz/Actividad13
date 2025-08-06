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
