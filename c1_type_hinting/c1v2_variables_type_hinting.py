
from typing import Dict, List, Mapping, Tuple


nombre: str = "Ana"
nombre = "Ana"

edad: int = 25

pi: float  = 3.1416

# apellidos : list[str] = ["Botero", "Tafur", "Quiñonez"]
apellidos : List[str] = ["Botero", "Tafur", "Quiñonez"]

# lenguajes_programacion: tuple[str, str, str, str] = ("python", "java", "javascript", "golang")
lenguajes_programacion: Tuple[str, str, str] = ("python", "java", "javascript", "golang")

# lenguaje: dict = {"nombre": "python", "creador": "Guido Van Rossum"}
lenguaje: Dict[str, str] = {"nombre": "python", "creador": "Guido Van Rossum"}

print(nombre)
print(edad)
print(pi)
print(apellidos)
print(lenguajes_programacion)
print(lenguaje)
D3lp1n072
