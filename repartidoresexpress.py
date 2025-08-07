class Repartidor:
    def __init__(self, nombre, paquetes, zona):
        self.nombre = nombre
        self.paquetes = paquetes
        self.zona = zona

    def __str__(self):
        return f'{self.nombre} - {self.paquetes} Paquetes - Zona: {self.zona}'


class EmpresaMensajera:
    def __init__(self):
        self.repartidores = []

    def agregar_repartidores(self, repartidor):
        if repartidor.nombre == "":
            print("Error: Nombre inválido.")
            return False
        if repartidor.paquetes < 0:
            print("Error: Paquetes deben ser un entero positivo.")
            return False
        if repartidor.zona == "":
            print("Error: Zona inválida.")
            return False
        if self.busqueda_de_valor(repartidor.nombre) is not None:
            print(f"Error: Ya existe repartidor con nombre '{repartidor.nombre}'.")
            return False

        self.repartidores.append(repartidor)
        return True

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
            if elemento.nombre == nombre:
                return elemento
        return None

    def mostrar_ranking(self):
        for elemento in self.repartidores:
            print(elemento)

    def estadisticas(self):
        if not self.repartidores:
            print("No hay repartidores registrados.")
            return

        total = sum(r.paquetes for r in self.repartidores)
        promedio = total / len(self.repartidores)

        max_entregas = -1
        min_entregas = 10 * 9

        repartidor_max = None
        repartidor_min = None

        for j in self.repartidores:
            if j.paquetes > max_entregas:
                max_entregas = j.paquetes
                repartidor_max = j
            if j.paquetes < min_entregas:
                min_entregas = j.paquetes
                repartidor_min = j

        print(f"Total de entregas: {total}")
        print(f"Promedio de entregas: {promedio:.2f}")
        print(f"Mayor número de entregas: {repartidor_max.nombre} ({max_entregas})")
        print(f"Menor número de entregas: {repartidor_min.nombre} ({min_entregas})")


empresa = EmpresaMensajera()

print("=== Rendimiento repartidores ===")

cantidad = int(input("Cantidad de repartidores: "))
for i in range(cantidad):
    print(f"Ingrese datos del repartidor {i + 1}:")
    while True:
        nombre = input("Ingrese el nombre: ")
        if nombre == "" or empresa.busqueda_de_valor(nombre):
            print("Este nombre ya existe")
        else:
            break
    paquetes = int(input("Ingrese los paquetes: "))
    zona = input("Ingrese la zona: ")
    repartidor = Repartidor(nombre, paquetes, zona)
    empresa.agregar_repartidores(repartidor)

print("=== Lista original ===")
for i in empresa.repartidores:
    print(i)

empresa.ordenar_por_paquetes()

print("=== Ranking ===")
empresa.mostrar_ranking()

print("=== Buscar repartidor ===")
buscar_repartidor = input("Ingrese el repartidor que quiere buscar: ")
resultado = empresa.busqueda_de_valor(buscar_repartidor)
if resultado is not None:
    print(resultado)
else:
    print("El repartidor no encontrado")

print("=== Estadisticas ===")
empresa.estadisticas()
