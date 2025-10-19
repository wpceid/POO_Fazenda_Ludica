from animal import Animal
from cachorro import Cachorro
from gato import Gato
from vaca import Vaca

c1 = Cachorro("Rex", 3, "Labrador")
g1 = Gato("Mimi", 5, "Branco")
v1 = Vaca("Mimosa", 7, 25.5)

c1.emitir_som()
g1.emitir_som()
v1.emitir_som()
c1.apresentar()
g1.apresentar()
v1.apresentar()