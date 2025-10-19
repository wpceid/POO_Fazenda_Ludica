class Animal:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def emitir_som(self):
        return "O animal emite um som"
        
    def apresentar(self, nome, idade):
        return f"Olá, eu sou {nome} e tenho {idade} anos"