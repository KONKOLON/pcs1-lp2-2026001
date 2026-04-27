class Pasajero:
    RUTAS_VALIDAS=["Iquitos-Nauta", "Iquitos-Yurimaguas", "Iquitos-Requena", "Iquitos-Contamana"]
    PESO_lIBRE = 15.0
    PESO_MAXIMO = 25.0

    def __init__(self, nombre_completo, ruta, peso_equipaje, dni, edad):
        self.nombre_completo = nombre_completo
        self.ruta = ruta
        self.peso_equipaje = peso_equipaje
        self.dni = dni
        self.edad = edad