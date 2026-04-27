class Pasajero:
    RUTAS_VALIDAS=["Iquitos-Nauta", "Iquitos-Yurimaguas", "Iquitos-Pucallpa"]
    PESO_LIBRE = 15.0
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
        return tarifas[self._ruta]
    

    @property
    def recargo_equipaje(self):
        exceso = max(0, self._peso_equipaje - self.PESO_LIBRE)
        return exceso * 2
    
    @property
    def tarifa_total(self):
        base = self.tarifa_base
        if self.categoria_edad in ["Niño/a", "Adulto/a mayor"]:
            base *= 0.5
        return base + self.recargo_equipaje
    
    
    def __str__(self):
        return (f"Pasajero: {self.nombre_completo}\n"
                f"Ruta: {self.ruta}\n"
                f"Peso del equipaje: {self.peso_equipaje} kg\n"
                f"DNI: {self.dni}\n"
                f"Edad: {self.edad} años\n"
                f"Categoría de edad: {self.categoria_edad}\n"
                f"Tarifa base: ${self.tarifa_base:.2f}\n"
                f"Recargo por equipaje: ${self.recargo_equipaje:.2f}\n"
                f"Tarifa total a pagar: ${self.tarifa_total:.2f}")
    
if __name__ == "__main__":
        p1 = Pasajero("juan perez", "Iquitos-Nauta", 10, "12345678", 20)
        print(p1)

        p2 = Pasajero("maria lopez", "Iquitos-Pucallpa", 14, "87654321", 65)
        print(p2)

        p3 = Pasajero("carlos ramirez", "Iquitos-Yurimaguas", 25, "11223344", 30)
        print(p3)
