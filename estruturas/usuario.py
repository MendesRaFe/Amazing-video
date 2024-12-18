class Usuario:
    def __init__(self, nome=None, idade=None, email=None, telefone=None, generos_prediletos=None, atores_prediletos=None):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.generos_prediletos = generos_prediletos if generos_prediletos else []
        self.atores_prediletos = atores_prediletos if atores_prediletos else []
    
    def __str__(self):
        return f"Usuário: {self.nome}, Idade: {self.idade}, Email: {self.email}"

    def adicionar_genero(self, genero):
        if genero not in self.generos_prediletos:
            self.generos_prediletos.append(genero)

    def adicionar_ator(self, ator):
        if ator not in self.atores_prediletos:
            self.atores_prediletos.append(ator)