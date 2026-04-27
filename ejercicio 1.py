class Pasajero:
    RUTAS_VALIDAS=["Iquitos-Nauta", "Iquitos-Yurimaguas", "Iquitos-Pucallpa"]
    PESO_lIBRE = 15.0
    PESO_MAXIMO = 25.0

    def __init__(self, nombre_completo, ruta, peso_equipaje, dni, edad):
        self.nombre_completo = nombre_completo
        self.ruta = ruta
        self.peso_equipaje = peso_equipaje
        self.dni = dni
        self.edad = edad

    @property 
    def dni(self):
        return self._dni
    @dni.setter
    def dni(self, value):
        if len(value) != 8 or not value.isdigit():
            raise ValueError("El DNI debe tener exactamente 8 dígitos numéricos.")
        self._dni = value
    
    @property
    def ruta(self):
        return self._ruta
    @ruta.setter
    def ruta(self, value):
        if value not in self.RUTAS_VALIDAS:
            raise ValueError(f"La ruta debe ser una de las siguientes: {', '.join(self.RUTAS_VALIDAS)}.")
        self._ruta = value

    @property
    def peso_equipaje(self):
        return self._peso_equipaje
    @peso_equipaje.setter
    def peso_equipaje(self, value):
        if value < 0 or value > self.PESO_MAXIMO:
            raise ValueError(f"El peso del equipaje debe estar entre 0 y {self.PESO_MAXIMO}.")
        self._peso_equipaje = value

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, value):
        if value < 0:
            raise ValueError("La edad no puede ser negativa.")
        self._edad = value

    @property
    def nombre_completo(self):
        return self._nombre_completo
    @nombre_completo.setter
    def nombre_completo(self, value):
        if not value.strip():
            raise ValueError("El nombre completo no puede estar vacío.")
        self._nombre_completo = value.strip()


    

    @property
    def categoria_edad(self):
        if self._edad < 12:
            return "Niño/a"
        if self._edad <=17:
            return "Adolescente"
        if self._edad <=59:
            return "Adulto/a"
        else:
            return "Adulto/a mayor"
        
    @property
    def tarifa_base(self):
        tarifas = {
            "Iquitos-Nauta": 50.0,
            "Iquitos-Yurimaguas": 70.0,
            "Iquitos-Pucallpa": 60.0
        }
        
        
