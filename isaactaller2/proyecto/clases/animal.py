class Animal:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

    def imprimirnombre(self):
        return f'el nombre del ave es {self.nombre} y su peso es {self.peso} kg' 