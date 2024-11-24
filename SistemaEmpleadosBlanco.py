from datetime import datetime
from collections import defaultdict

class Empleado:
    def __init__(self, nombre, horas, sector, fecha_ingreso):
        self.nombre = nombre
        self.horas = horas
        self.sector = sector
        self.fecha_ingreso = datetime.strptime(fecha_ingreso, '%Y-%m-%d')
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Horas: {self.horas} - Sector: {self.sector} - Ingreso: {self.fecha_ingreso.strftime('%Y-%m-%d')}"


class SistemaGestion:
    def __init__(self):
        self.empleados = []

    def registrar_empleado(self, nombre, horas, sector, fecha_ingreso):
        empleado = Empleado(nombre, horas, sector, fecha_ingreso)
        self.empleados.append(empleado)
        print(f"Empleado {nombre} ingresado correctamente.")

    def consultar_empleado(self, sector=None):
        if sector:
            sector_empleado = [t for t in self.empleados if t.sector == sector]
            return sector_empleado
        return self.empleados

    def estadisticas_por_sector(self):
        estadisticas = defaultdict(lambda: {'cantidad': 0, 'horas_totales': 0})
        for empleado in self.empleados:
            estadisticas[empleado.sector]['cantidad'] += 1
            estadisticas[empleado.sector]['horas_totales'] += empleado.horas

        for sector, datos in estadisticas.items():
            cantidad = datos['cantidad']
            horas_totales = datos['horas_totales']
            print(f"Sector: {sector} - Empleados: {cantidad}, Horas Totales: {horas_totales}")


class MenuSistema:
    def __init__(self):
        self.sistema_gestion = SistemaGestion()

    def mostrar_menu(self):
        while True:
            print("\n=== Bienvenido a Sistema de gestion de empleados Blanco===")
            print("Menu:")
            print("1- Registrar empleado")
            print("2- Consultar por empleado")
            print("3- Mostrar estadísticas por area")
            print("4- Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.registrar_empleado()
            elif opcion == '2':
                self.consultar_empleado()
            elif opcion == '3':
                self.mostrar_estadisticas()
            elif opcion == '4':
                print("\nSaliendo del sistema...")
                print("Hasta luego")
                break
            else:
                print("Opción erronea. Pruebe nuevamente.")

    def registrar_empleado(self):
        nombre = input("Ingrese el nombre del empleado: ")
        horas = int(input("Ingrese las horas trabajadas del empleado: "))
        sector = input("Ingrese el area del empleado: ")
        fecha_ingreso = input("Ingrese la fecha de ingreso (YYYY-MM-DD): ")
        self.sistema_gestion.registrar_empleado(nombre, horas, sector, fecha_ingreso)

    def consultar_empleado(self):
        if not self.sistema_gestion.empleados:
            print("\nNo hay empleados registrados para mostrar estadísticas.")
        else:
            sector = input("\nIngrese el area (dejar en blanco para ver todas las areas): ")
            empleados = self.sistema_gestion.consultar_empleado(sector)
            if empleados:
                print("\nLista de empleados:")
                for empleado in empleados:
                    print(empleado)
            else:
                print("\nNo hay empleados para mostrar en el sector especificado.")

    def mostrar_estadisticas(self):
        if not self.sistema_gestion.empleados:
            print("\nNo hay empleados registrados para mostrar estadísticas.")
        else:
            print("\nDatos del area: ")
            self.sistema_gestion.estadisticas_por_sector()

# Ejecutar el menú
if __name__ == "__main__":
    menu = MenuSistema()
    menu.mostrar_menu()
