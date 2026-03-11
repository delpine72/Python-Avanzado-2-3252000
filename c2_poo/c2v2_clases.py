class Persona:

    tipo = "Humano"

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento_identidad = None

    def agregar_documento_identidad(self, numero_documento):
        self.documento_identidad = numero_documento
        print("Documento guardado")


paco = Persona("Paco", "Botero", 27)
print(paco.tipo)
print(paco.nombre)
paco.agregar_documento_identidad(1234)

maria = Persona("Maria", "Gomez", 30)
print(maria.tipo)
maria.agregar_documento_identidad(5678)
print(maria.documento_identidad)
