from owlready2 import *
import unicodedata
import random
#from owlready2 import sync_reasoner_pellet

onto = get_ontology("C:\\Users\\phell\\Dropbox\\projetos\\webSemantica\\filmesV1.rdf").load()

# Executar o reasoner para aplicar inferências
#sync_reasoner_pellet()

# Criar instâncias de filme

filmes_conhecidos = [
    {"tituloPortugues": "O Poderoso Chefão", "tituloOriginal": "The Godfather", "anoProducao": 1972, "anoLancamento": 1972, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "A Origem", "tituloOriginal": "Inception", "anoProducao": 2010, "anoLancamento": 2010, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Titanic", "tituloOriginal": "Titanic", "anoProducao": 1997, "anoLancamento": 1997, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Forrest Gump", "tituloOriginal": "Forrest Gump", "anoProducao": 1994, "anoLancamento": 1994, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Matrix", "tituloOriginal": "The Matrix", "anoProducao": 1999, "anoLancamento": 1999, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "O Senhor dos Anéis: A Sociedade do Anel", "tituloOriginal": "The Lord of the Rings: The Fellowship of the Ring", "anoProducao": 2001, "anoLancamento": 2001, "nacionalidade": "Nova Zelândia", "idioma": "Inglês"},
    {"tituloPortugues": "Vingadores: Ultimato", "tituloOriginal": "Avengers: Endgame", "anoProducao": 2019, "anoLancamento": 2019, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Pantera Negra", "tituloOriginal": "Black Panther", "anoProducao": 2018, "anoLancamento": 2018, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Homem-Aranha: Sem Volta para Casa", "tituloOriginal": "Spider-Man: No Way Home", "anoProducao": 2021, "anoLancamento": 2021, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "A Bela e a Fera", "tituloOriginal": "Beauty and the Beast", "anoProducao": 2017, "anoLancamento": 2017, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Gladiador", "tituloOriginal": "Gladiator", "anoProducao": 2000, "anoLancamento": 2000, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Coringa", "tituloOriginal": "Joker", "anoProducao": 2019, "anoLancamento": 2019, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Duna", "tituloOriginal": "Dune", "anoProducao": 2021, "anoLancamento": 2021, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Star Wars: Uma Nova Esperança", "tituloOriginal": "Star Wars: A New Hope", "anoProducao": 1977, "anoLancamento": 1977, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Interestelar", "tituloOriginal": "Interstellar", "anoProducao": 2014, "anoLancamento": 2014, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Toy Story", "tituloOriginal": "Toy Story", "anoProducao": 1995, "anoLancamento": 1995, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Harry Potter e a Pedra Filosofal", "tituloOriginal": "Harry Potter and the Sorcerer's Stone", "anoProducao": 2001, "anoLancamento": 2001, "nacionalidade": "Reino Unido", "idioma": "Inglês"},
    {"tituloPortugues": "A Lista de Schindler", "tituloOriginal": "Schindler's List", "anoProducao": 1993, "anoLancamento": 1993, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Pulp Fiction: Tempo de Violência", "tituloOriginal": "Pulp Fiction", "anoProducao": 1994, "anoLancamento": 1994, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "O Rei Leão", "tituloOriginal": "The Lion King", "anoProducao": 1994, "anoLancamento": 1994, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Procurando Nemo", "tituloOriginal": "Finding Nemo", "anoProducao": 2003, "anoLancamento": 2003, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Os Incríveis", "tituloOriginal": "The Incredibles", "anoProducao": 2004, "anoLancamento": 2004, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Frozen: Uma Aventura Congelante", "tituloOriginal": "Frozen", "anoProducao": 2013, "anoLancamento": 2013, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Encanto", "tituloOriginal": "Encanto", "anoProducao": 2021, "anoLancamento": 2021, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Moana: Um Mar de Aventuras", "tituloOriginal": "Moana", "anoProducao": 2016, "anoLancamento": 2016, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Carros", "tituloOriginal": "Cars", "anoProducao": 2006, "anoLancamento": 2006, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Divertida Mente", "tituloOriginal": "Inside Out", "anoProducao": 2015, "anoLancamento": 2015, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Shrek", "tituloOriginal": "Shrek", "anoProducao": 2001, "anoLancamento": 2001, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Kung Fu Panda", "tituloOriginal": "Kung Fu Panda", "anoProducao": 2008, "anoLancamento": 2008, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Homem de Ferro", "tituloOriginal": "Iron Man", "anoProducao": 2008, "anoLancamento": 2008, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Capitão América: O Primeiro Vingador", "tituloOriginal": "Captain America: The First Avenger", "anoProducao": 2011, "anoLancamento": 2011, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Guardiões da Galáxia", "tituloOriginal": "Guardians of the Galaxy", "anoProducao": 2014, "anoLancamento": 2014, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Thor: Ragnarok", "tituloOriginal": "Thor: Ragnarok", "anoProducao": 2017, "anoLancamento": 2017, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Viúva Negra", "tituloOriginal": "Black Widow", "anoProducao": 2021, "anoLancamento": 2021, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Avatar", "tituloOriginal": "Avatar", "anoProducao": 2009, "anoLancamento": 2009, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Top Gun: Maverick", "tituloOriginal": "Top Gun: Maverick", "anoProducao": 2022, "anoLancamento": 2022, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Cisne Negro", "tituloOriginal": "Black Swan", "anoProducao": 2010, "anoLancamento": 2010, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "A Teoria de Tudo", "tituloOriginal": "The Theory of Everything", "anoProducao": 2014, "anoLancamento": 2014, "nacionalidade": "Reino Unido", "idioma": "Inglês"},
    {"tituloPortugues": "Bohemian Rhapsody", "tituloOriginal": "Bohemian Rhapsody", "anoProducao": 2018, "anoLancamento": 2018, "nacionalidade": "Reino Unido", "idioma": "Inglês"},
    {"tituloPortugues": "O Exorcista", "tituloOriginal": "The Exorcist", "anoProducao": 1973, "anoLancamento": 1973, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "Psicose", "tituloOriginal": "Psycho", "anoProducao": 1960, "anoLancamento": 1960, "nacionalidade": "Estados Unidos", "idioma": "Inglês"},
    {"tituloPortugues": "O Iluminado", "tituloOriginal": "The Shining", "anoProducao": 1980, "anoLancamento": 1980, "nacionalidade": "Estados Unidos", "idioma": "Inglês"}
]


generos_filmes = [
    {"filme": "O_Poderoso_Chefao", "genero": "FilmeDeSuspense"},
    {"filme": "A_Origem", "genero": "FilmeDeFiccao"},
    {"filme": "Titanic", "genero": "FilmeDeSuspense"},
    {"filme": "Forrest_Gump", "genero": "FilmeDeComedia"},
    {"filme": "Matrix", "genero": "FilmeDeFiccao"},
    {"filme": "O_Senhor_dos_Aneis:_A_Sociedade_do_Anel", "genero": "FilmeDeAcao"},
    {"filme": "Vingadores:_Ultimato", "genero": "FilmeDeAcao"},
    {"filme": "Pantera_Negra", "genero": "FilmeDeAcao"},
    {"filme": "Homem-Aranha:_Sem_Volta_para_Casa", "genero": "FilmeDeAcao"},
    {"filme": "A_Bela_e_a_Fera", "genero": "FilmeMusical"},
    {"filme": "Gladiador", "genero": "FilmeDeAcao"},
    {"filme": "Coringa", "genero": "FilmeDeSuspense"},
    {"filme": "Duna", "genero": "FilmeDeFiccao"},
    {"filme": "Star_Wars:_Uma_Nova_Esperanca", "genero": "FilmeDeFiccao"},
    {"filme": "Interestelar", "genero": "FilmeDeFiccao"},
    {"filme": "Toy_Story", "genero": "FilmeDeComedia"},
    {"filme": "Harry_Potter_e_a_Pedra_Filosofal", "genero": "FilmeDeFiccao"},
    {"filme": "A_Lista_de_Schindler", "genero": "FilmeDeSuspense"},
    {"filme": "Pulp_Fiction:_Tempo_de_Violencia", "genero": "FilmeDeSuspense"},
    {"filme": "O_Rei_Leao", "genero": "FilmeMusical"},
    {"filme": "Procurando_Nemo", "genero": "FilmeDeComedia"},
    {"filme": "Os_Incriveis", "genero": "FilmeDeAcao"},
    {"filme": "Frozen:_Uma_Aventura_Congelante", "genero": "FilmeMusical"},
    {"filme": "Encanto", "genero": "FilmeMusical"},
    {"filme": "Moana:_Um_Mar_de_Aventuras", "genero": "FilmeMusical"},
    {"filme": "Carros", "genero": "FilmeDeComedia"},
    {"filme": "Divertida_Mente", "genero": "FilmeDeComedia"},
    {"filme": "Shrek", "genero": "FilmeDeComedia"},
    {"filme": "Kung_Fu_Panda", "genero": "FilmeDeAcao"},
    {"filme": "Homem_de_Ferro", "genero": "FilmeDeAcao"},
    {"filme": "Capitao_America:_O_Primeiro_Vingador", "genero": "FilmeDeAcao"},
    {"filme": "Guardioes_da_Galaxia", "genero": "FilmeDeAcao"},
    {"filme": "Thor:_Ragnarok", "genero": "FilmeDeAcao"},
    {"filme": "Viuva_Negra", "genero": "FilmeDeAcao"},
    {"filme": "Avatar", "genero": "FilmeDeFiccao"},
    {"filme": "Top_Gun:_Maverick", "genero": "FilmeDeAcao"},
    {"filme": "Cisne_Negro", "genero": "FilmeDeSuspense"},
    {"filme": "A_Teoria_de_Tudo", "genero": "FilmeDeSuspense"},
    {"filme": "Bohemian_Rhapsody", "genero": "FilmeMusical"},
    {"filme": "O_Exorcista", "genero": "FilmeDeTerror"},
    {"filme": "Psicose", "genero": "FilmeDeTerror"},
    {"filme": "O_Iluminado", "genero": "FilmeDeTerror"}
]

usuarios = [
    {"nome": "João", "email": "joao@exemplo.com", "telefone": "9999-1111", "idade": 20},
    {"nome": "Maria", "email": "maria@exemplo.com", "telefone": "9999-2222", "idade": 25},
    {"nome": "Carlos", "email": "carlos@exemplo.com", "telefone": "9999-3333", "idade": 30},
    {"nome": "Ana", "email": "ana@exemplo.com", "telefone": "9999-4444", "idade": 22},
    {"nome": "Lucas", "email": "lucas@exemplo.com", "telefone": "9999-5555", "idade": 35},
    {"nome": "Beatriz", "email": "beatriz@exemplo.com", "telefone": "9999-6666", "idade": 28},
    {"nome": "Paulo", "email": "paulo@exemplo.com", "telefone": "9999-7777", "idade": 33},
    {"nome": "Mariana", "email": "mariana@exemplo.com", "telefone": "9999-8888", "idade": 27},
    {"nome": "Ricardo", "email": "ricardo@exemplo.com", "telefone": "9999-9999", "idade": 40},
    {"nome": "Fernanda", "email": "fernanda@exemplo.com", "telefone": "9888-1111", "idade": 23},
    {"nome": "Juliana", "email": "juliana@exemplo.com", "telefone": "9888-2222", "idade": 31},
    {"nome": "Gabriel", "email": "gabriel@exemplo.com", "telefone": "9888-3333", "idade": 29},
    {"nome": "Roberta", "email": "roberta@exemplo.com", "telefone": "9888-4444", "idade": 26},
    {"nome": "Eduardo", "email": "eduardo@exemplo.com", "telefone": "9888-5555", "idade": 32},
    {"nome": "Simone", "email": "simone@exemplo.com", "telefone": "9888-6666", "idade": 38}
]

atores = [
    {"nome": "Marlon Brando"},
    {"nome": "Al Pacino"},
    {"nome": "Leonardo DiCaprio"},
    {"nome": "Joseph Gordon-Levitt"},
    {"nome": "Ellen Page"},
    {"nome": "Kate Winslet"},
    {"nome": "Tom Hanks"},
    {"nome": "Robin Wright"},
    {"nome": "Keanu Reeves"},
    {"nome": "Laurence Fishburne"},
    {"nome": "Carrie-Anne Moss"},
    {"nome": "Elijah Wood"},
    {"nome": "Ian McKellen"},
    {"nome": "Viggo Mortensen"},
    {"nome": "Robert Downey Jr."},
    {"nome": "Chris Evans"},
    {"nome": "Scarlett Johansson"},
    {"nome": "Chadwick Boseman"},
    {"nome": "Michael B. Jordan"},
    {"nome": "Tom Holland"},
    {"nome": "Benedict Cumberbatch"},
    {"nome": "Zendaya"},
    {"nome": "Emma Watson"},
    {"nome": "Dan Stevens"},
    {"nome": "Russell Crowe"},
    {"nome": "Joaquin Phoenix"},
    {"nome": "Connie Nielsen"},
    {"nome": "Timothée Chalamet"},
    {"nome": "Oscar Isaac"},
    {"nome": "Mark Hamill"},
    {"nome": "Harrison Ford"},
    {"nome": "Carrie Fisher"},
    {"nome": "Matthew McConaughey"},
    {"nome": "Anne Hathaway"},
    {"nome": "Jessica Chastain"},
    {"nome": "Tim Allen"},
    {"nome": "Daniel Radcliffe"},
    {"nome": "Rupert Grint"},
    {"nome": "Liam Neeson"},
    {"nome": "Ben Kingsley"},
    {"nome": "Ralph Fiennes"},
    {"nome": "John Travolta"},
    {"nome": "Uma Thurman"},
    {"nome": "Samuel L. Jackson"},
    {"nome": "Matthew Broderick"},
    {"nome": "James Earl Jones"},
    {"nome": "Albert Brooks"},
    {"nome": "Ellen DeGeneres"},
    {"nome": "Craig T. Nelson"},
    {"nome": "Holly Hunter"},
    {"nome": "Kristen Bell"},
    {"nome": "Idina Menzel"},
    {"nome": "Stephanie Beatriz"},
    {"nome": "María Cecilia Botero"},
    {"nome": "Auli'i Cravalho"},
    {"nome": "Dwayne Johnson"},
    {"nome": "Owen Wilson"},
    {"nome": "Larry the Cable Guy"},
    {"nome": "Amy Poehler"},
    {"nome": "Phyllis Smith"},
    {"nome": "Mike Myers"},
    {"nome": "Eddie Murphy"},
    {"nome": "Cameron Diaz"},
    {"nome": "Jack Black"},
    {"nome": "Dustin Hoffman"},
    {"nome": "Angelina Jolie"},
    {"nome": "Gwyneth Paltrow"},
    {"nome": "Jeff Bridges"},
    {"nome": "Hayley Atwell"},
    {"nome": "Chris Pratt"},
    {"nome": "Zoe Saldana"},
    {"nome": "Dave Bautista"},
    {"nome": "Chris Hemsworth"},
    {"nome": "Tom Hiddleston"},
    {"nome": "Cate Blanchett"},
    {"nome": "Florence Pugh"},
    {"nome": "David Harbour"},
    {"nome": "Sam Worthington"},
    {"nome": "Sigourney Weaver"},
    {"nome": "Miles Teller"},
    {"nome": "Jennifer Connelly"},
    {"nome": "Natalie Portman"},
    {"nome": "Mila Kunis"},
    {"nome": "Eddie Redmayne"},
    {"nome": "Felicity Jones"},
    {"nome": "Rami Malek"},
    {"nome": "Lucy Boynton"},
    {"nome": "Linda Blair"},
    {"nome": "Max von Sydow"},
    {"nome": "Anthony Perkins"},
    {"nome": "Janet Leigh"},
    {"nome": "Jack Nicholson"},
    {"nome": "Shelley Duvall"}
]

diretores = [
    {"nome": "Francis Ford Coppola"},
    {"nome": "Christopher Nolan"},
    {"nome": "James Cameron"},
    {"nome": "Robert Zemeckis"},
    {"nome": "Lana Wachowski"},
    {"nome": "Lilly Wachowski"},
    {"nome": "Peter Jackson"},
    {"nome": "Anthony Russo"},
    {"nome": "Joe Russo"},
    {"nome": "Ryan Coogler"},
    {"nome": "Jon Watts"},
    {"nome": "Bill Condon"},
    {"nome": "Ridley Scott"},
    {"nome": "Todd Phillips"},
    {"nome": "Denis Villeneuve"},
    {"nome": "George Lucas"},
    {"nome": "John Lasseter"},
    {"nome": "Chris Columbus"},
    {"nome": "Steven Spielberg"},
    {"nome": "Quentin Tarantino"},
    {"nome": "Roger Allers"},
    {"nome": "Rob Minkoff"},
    {"nome": "Andrew Stanton"},
    {"nome": "Brad Bird"},
    {"nome": "Chris Buck"},
    {"nome": "Jennifer Lee"},
    {"nome": "Jared Bush"},
    {"nome": "Byron Howard"},
    {"nome": "Charise Castro Smith"},
    {"nome": "Ron Clements"},
    {"nome": "John Musker"},
    {"nome": "Joe Ranft"},
    {"nome": "Pete Docter"},
    {"nome": "Ronnie del Carmen"},
    {"nome": "Andrew Adamson"},
    {"nome": "Vicky Jenson"},
    {"nome": "Mark Osborne"},
    {"nome": "John Stevenson"},
    {"nome": "Jon Favreau"},
    {"nome": "Joe Johnston"},
    {"nome": "James Gunn"},
    {"nome": "Taika Waititi"},
    {"nome": "Cate Shortland"},
    {"nome": "Joseph Kosinski"},
    {"nome": "Darren Aronofsky"},
    {"nome": "James Marsh"},
    {"nome": "Bryan Singer"},
    {"nome": "William Friedkin"},
    {"nome": "Alfred Hitchcock"},
    {"nome": "Stanley Kubrick"}
]

def normalizar_nome(nome):
    # Remove acentos e caracteres especiais
    nome_normalizado = unicodedata.normalize('NFKD', nome).encode('ascii', 'ignore').decode('utf-8')
    # Substitui espaços por _
    nome_normalizado = nome_normalizado.replace(" ", "_")
    return nome_normalizado

# Adiciona instâncias de Filmes
for filme in filmes_conhecidos:
    # Normaliza o nome da instância (sem acentos ou caracteres especiais)
    nome_instancia = normalizar_nome(filme['tituloPortugues'])
    filme_instancia = onto.Filme(nome_instancia)  

    # Atribuir propriedades 
    filme_instancia.tituloPortugues.append(filme['tituloPortugues'])
    filme_instancia.tituloOriginal.append(filme['tituloOriginal'])
    filme_instancia.anoProducao.append(filme['anoProducao'])
    filme_instancia.anoLancamento.append(filme['anoLancamento'])
    filme_instancia.nacionalidade.append(filme['nacionalidade'])
    filme_instancia.idioma.append(filme['idioma'])

# Adiciona instâncias de Usuarios
for user in usuarios:
    # Normaliza o nome da instância (sem acentos ou caracteres especiais)
    nome_instancia = normalizar_nome(user['nome'])
    user_instancia = onto.Usuario(nome_instancia)  

    # Atribuir propriedades 
    user_instancia.nome.append(user['nome'])
    user_instancia.email.append(user['email'])
    user_instancia.telefone.append(user['telefone'])
    user_instancia.idade.append(user['idade'])

# Adiciona instâncias de Atores
for ator in atores:
    # Normaliza o nome da instância (sem acentos ou caracteres especiais)
    nome_instancia = normalizar_nome(ator['nome'])
    ator_instancia = onto.Ator(nome_instancia)  

    # Atribuir propriedades 
    ator_instancia.nome.append(ator['nome'])

# Adiciona instâncias de Diretores
for diretor in diretores:
    # Normaliza o nome da instância (sem acentos ou caracteres especiais)
    nome_instancia = normalizar_nome(diretor['nome'])
    diretor_instancia = onto.Diretor(nome_instancia)  

    # Atribuir propriedades 
    diretor_instancia.nome.append(diretor['nome'])


# Adiciona Produtor
produtor = onto.Produtor('Produtor01')
produtor.nome.append('Emma Thomas')

produtor = onto.Produtor('Produtor02')
produtor.nome.append('Jon Landau')

produtor = onto.Produtor('Produtor03')
produtor.nome.append('Wendy Finerman')

produtor = onto.Produtor('Produtor04')
produtor.nome.append('Steve Tisch')

produtor = onto.Produtor('Produtor05')
produtor.nome.append('Joel Silver')


# Adiciona Roteirista
roteirista = onto.Roteirista('Roreirista01')
roteirista.nome.append('Pete Docter')

roteirista = onto.Roteirista('Roteirista02')
roteirista.nome.append('Ted Elliott')

roteirista = onto.Roteirista('Roteirista03')
roteirista.nome.append('Jonathan Aibel')

roteirista = onto.Roteirista('Roteirista04')
roteirista.nome.append('Art Marcum')

roteirista = onto.Roteirista('Roteirista05')
roteirista.nome.append('Matt Holloway')

roteirista = onto.Roteirista('Roteirista06')
roteirista.nome.append('Christopher Markus')
    
# Adiciona Gêneros
onto.Acao('FilmeDeAcao')
onto.Comedia('FilmeDeComedia')
onto.FiccaoCientifica('FilmeDeFiccao')
onto.Musical('FilmeMusical')
onto.Suspense('FilmeDeSuspense')
onto.Terror('FilmeDeTerror')

# Adiciona Eventos
evento = onto.Evento('Evento01')
evento.nome.append('Oscar 1973')

evento = onto.Evento('Evento02')
evento.nome.append('Globo de Ouro 1973')

evento = onto.Evento('Evento03')
evento.nome.append('Oscar 1998')

evento = onto.Evento('Evento04')
evento.nome.append('Globo de Ouro 1998')

evento = onto.Evento('Evento05')
evento.nome.append('Oscar 2000')

evento = onto.Evento('Evento06')
evento.nome.append('BAFTA 2000')

evento = onto.Evento('Evento07')
evento.nome.append('Oscar 2002')

evento = onto.Evento('Evento08')
evento.nome.append('BAFTA 2002')

evento = onto.Evento('Evento09')
evento.nome.append('Oscar 2020')

evento = onto.Evento('Evento10')
evento.nome.append('Globo de Ouro 2020')


# Adiciona Prêmios
premio = onto.Premio('Premio01')
premio.nome.append('Melhor Filme')

premio = onto.Premio('Premio02')
premio.nome.append('Melhor Ator')

premio = onto.Premio('Premio03')
premio.nome.append('Melhor Roteiro Adaptado')

premio = onto.Premio('Premio04')
premio.nome.append('Melhor Diretor')

premio = onto.Premio('Premio05')
premio.nome.append('Melhor Fotografia')

premio = onto.Premio('Premio05')
premio.nome.append('Melhor Edição')

premio = onto.Premio('Premio06')
premio.nome.append('Melhor Efeitos Visuais')

premio = onto.Premio('Premio07')
premio.nome.append('Melhor Trilha Sonora')

# Defina a função para associar o gênero a cada filme
def filme_possui_genero():
    for item in generos_filmes:
        # Recupera o filme e o gênero
        filme = item["filme"]
        genero = item["genero"]

        # Busca os indivíduos na ontologia
        filme = onto.Filme(filme)
        genero = onto.Genero(genero)

        # Adiciona o gênero ao filme
        filme.possuiGenero.append(genero)

# Chama a função
filme_possui_genero()

# Defina a função para associar a preferência do usuário por gênero de filme
def usuario_temPreferencia_genero():
    #genero = ['FilmeDeSuspense', 'FilmeDeFiccao', 'FilmeDeComedia', 'FilmeDeAcao', 'FilmeMusical', 'FilmeDeTerror']
    for usuario in onto.Usuario.instances():
        genero = random.choice(onto.Genero.instances())
        usuario.temPreferencia.append(genero)
        
# Chama a função
usuario_temPreferencia_genero()

for usuario in onto.Usuario.instances():
    # Obtem o nome do filme e do gênero
    nome_usuario = usuario.name  # Obtém o nome do filme
    generos = usuario.temPreferencia  # Obtém os gêneros associados

    # Imprime os resultados
    for genero in generos:
        print(f"Filme: {nome_usuario}, Gênero: {genero.name}")

#print(dir(onto))
#print(list(onto.properties()))


# Salvar as alterações no RDF com identificadores únicos
#onto.save(file="C:\\Users\\phell\\Dropbox\\projetos\\webSemantica\\filmes_atualizado_com_ids.rdf")