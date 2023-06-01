class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def escreve(self):
        print(self.nome, self.idade)
        
class Estudante(Pessoa):
    def __init__(self, nome, idade):
        Pessoa.__init__(self, nome, idade)
        
#Use a palavra-chave pass quando não quiser adicionar nenhuma outra propriedade ou metodo à classe.

x = Estudante("Jo", 21)
x.escreve()