from owlready2 import *
import unicodedata
import random

class SistemaRecomendacao:
    def __init__(self, caminho_ontologia):
        self.onto = get_ontology(caminho_ontologia).load()

    def salvar_ontologia(self):
        self.onto.save(file="filmesV3.rdf", format="rdfxml")

    def cadastrar_usuario(self, email, nome, telefone=None, idade=None):
        # Verifica se os campos obrigatórios foram fornecidos
        if not email or not nome:
            return "Erro: Email e Nome são obrigatórios para o cadastro."

        # Verifica se o email já está cadastrado
        usuario_existente = self.onto.search_one(iri=f"*{email}")
        if usuario_existente:
            return f"Erro: Usuário com email '{email}' já cadastrado."

        # Cria uma nova instância de usuário
        novo_usuario = self.onto.Usuario(email)  # Usa o email como identificador único
        novo_usuario.nome = [nome]  # Define o nome
        if telefone:
            novo_usuario.telefone = [telefone]  # Define o telefone, se fornecido
        if idade:
            novo_usuario.idade = [idade]  # Define a idade, se fornecida

        # Salva as alterações na ontologia
        self.salvar_ontologia()
        return f"Usuário '{nome}' cadastrado com sucesso!"
    
    def adicionar_atores_favoritos(self, email_usuario, lista_atores):
        # Busca o usuário na ontologia pelo email
        usuario = self.onto.search_one(iri=f"*{email_usuario}")
        if not usuario:
            return f"Erro: Usuário com email '{email_usuario}' não encontrado."
        
        # Verifica quantos atores já estão associados ao usuário
        atores_atuais = getattr(usuario, "gostaDe", [])
        if len(atores_atuais) >= 5:
            return f"Erro: Usuário já possui 5 atores favoritos. Não é possível adicionar mais."
        
        # Adiciona os novos atores, respeitando o limite de 5
        for nome_ator in lista_atores:
            if len(atores_atuais) >= 5:
                break  

            ator = self.onto.search_one(iri=f"*{nome_ator}")
            if not ator:
                print(f"Erro: Ator '{nome_ator}' não encontrado.")
                continue

            # Verifica se o ator já está associado ao usuário
            if ator in atores_atuais:
                print(f"Usuário já gosta do ator '{nome_ator}'.")
                continue

            # Associa o ator ao usuário
            usuario.gostaDe.append(ator)
            atores_atuais.append(ator)
            print(f"Ator '{nome_ator}' associado ao usuário '{email_usuario}'.")

        # Salva as alterações na ontologia
        self.salvar_ontologia()
        return f"Atores favoritos atualizados para o usuário '{email_usuario}'."
        
if __name__ == "__main__":
    sistema = SistemaRecomendacao("filmesV2.rdf")
    
    ''' testando resultados '''

    # Cadastro de usuário com todos os campos
    resultado = sistema.cadastrar_usuario(
        email="usuario@email.com",
        nome="João Silva",
        telefone="123456789",
        idade=30
    )
    print(resultado)

    # Adicionar atores favoritos ao usuário cadastrado
    resultado = sistema.adicionar_atores_favoritos(
        email_usuario="carlos@exemplo.com",
        lista_atores=["Sigourney_Weaver"]
    )
    print(resultado)