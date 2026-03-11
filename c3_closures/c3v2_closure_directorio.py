def agregar_persona_directorio():
    directorio = {}

    def agregar(nombre, edad, ciudad):
        directorio[nombre] = {"edad": edad, "ciudad": ciudad}
        return directorio

    def remover(nombre):
        directorio.pop(nombre, None)
        return directorio

    agregar.remover = remover

    return agregar


almacenar = agregar_persona_directorio()
directorio = almacenar("Paco", 27, "Cali")
directorio = almacenar("Javier", 25, "Madrid")
directorio = almacenar("Emilio", 26, "Brisbane")

print(directorio)

directorio = almacenar.remover("Javier")
print(directorio)
