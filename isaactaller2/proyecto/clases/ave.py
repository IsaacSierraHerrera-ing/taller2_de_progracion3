from clases.animal import Animal


class Ave(Animal):  
    
    def __init__(self, nombre, peso, año_nacimiento, propietario):
        super().__init__(nombre, peso)
        self.año_nacimiento = año_nacimiento
        self.propietario = propietario

    def imprimirpropietario(self):
        return f'el nombre del propietario es {self.propietario} y su año de nacimiento es {self.año_nacimiento}'     

    def calcular_edad(self):
        
        año_actual = 2025 
        edad = año_actual - self.año_nacimiento

        if edad >= 5:
            print(f"El ave {self.nombre} es MAYOR DE EDAD.")
        else:
            print(f"El ave {self.nombre} es MENOR DE EDAD.")