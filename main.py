from animal import Animal
from cachorro import Cachorro
from gato import Gato
from vaca import Vaca

c1 = Cachorro("Rex", 3, "Labrador")
g1 = Gato("Mimi", 5, "Branco")
v1 = Vaca("Mimosa", 7, 25.5)

lista_animais = [c1,g1,v1]

for animal in lista_animais:
    animal.emitir_som()
    animal.apresentar()
    
v1.obter_producao_leite()
v1.registrar_ordenha(28.8)