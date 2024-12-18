from owlready2 import *
import unicodedata
import random
#from owlready2 import sync_reasoner_pellet

onto = get_ontology("filmesV1.rdf").load()

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

filmes_e_atores = [
    {"filme": "O_Poderoso_Chefao", "atores": ["Marlon_Brando", "Al_Pacino"]},
    {"filme": "A_Origem", "atores": ["Leonardo_DiCaprio", "Joseph_Gordon-Levitt", "Ellen_Page"]},
    {"filme": "Titanic", "atores": ["Leonardo_DiCaprio", "Kate_Winslet"]},
    {"filme": "Forrest_Gump", "atores": ["Tom_Hanks", "Robin_Wright"]},
    {"filme": "Matrix", "atores": ["Keanu_Reeves", "Laurence_Fishburne", "Carrie-Anne_Moss"]},
    {"filme": "O_Senhor_dos_Aneis:_A_Sociedade_do_Anel", "atores": ["Elijah_Wood", "Ian_McKellen", "Viggo_Mortensen"]},
    {"filme": "Vingadores:_Ultimato", "atores": ["Robert_Downey_Jr.", "Chris_Evans", "Scarlett_Johansson"]},
    {"filme": "Pantera_Negra", "atores": ["Chadwick_Boseman", "Michael_B._Jordan"]},
    {"filme": "Homem-Aranha:_Sem_Volta_para_Casa", "atores": ["Tom_Holland", "Benedict_Cumberbatch", "Zendaya"]},
    {"filme": "A_Bela_e_a_Fera", "atores": ["Emma_Watson", "Dan_Stevens"]},
    {"filme": "Gladiador", "atores": ["Russell_Crowe", "Joaquin_Phoenix", "Connie_Nielsen"]},
    {"filme": "Coringa", "atores": ["Joaquin_Phoenix"]},
    {"filme": "Duna", "atores": ["Timothee_Chalamet", "Oscar_Isaac"]},
    {"filme": "Star_Wars:_Uma_Nova_Esperanca", "atores": ["Mark_Hamill", "Harrison_Ford", "Carrie_Fisher"]},
    {"filme": "Interestelar", "atores": ["Matthew_McConaughey", "Anne_Hathaway", "Jessica_Chastain"]},
    {"filme": "Toy_Story", "atores": ["Tim_Allen", "Tom_Hanks"]},
    {"filme": "Harry_Potter_e_a_Pedra_Filosofal", "atores": ["Daniel_Radcliffe", "Rupert_Grint", "Emma_Watson"]},
    {"filme": "A_Lista_de_Schindler", "atores": ["Liam_Neeson", "Ben_Kingsley", "Ralph_Fiennes"]},
    {"filme": "Pulp_Fiction:_Tempo_de_Violencia", "atores": ["John_Travolta", "Uma_Thurman", "Samuel_L._Jackson"]},
    {"filme": "O_Rei_Leao", "atores": ["Matthew_Broderick", "James_Earl_Jones"]},
    {"filme": "Procurando_Nemo", "atores": ["Albert_Brooks", "Ellen_DeGeneres"]},
    {"filme": "Os_Incriveis", "atores": ["Craig_T._Nelson", "Holly_Hunter"]},
    {"filme": "Frozen:_Uma_Aventura_Congelante", "atores": ["Kristen_Bell", "Idina_Menzel"]},
    {"filme": "Encanto", "atores": ["Stephanie_Beatriz", "Maria_Cecilia_Botero"]},
    {"filme": "Moana:_Um_Mar_de_Aventuras", "atores": ["Auli'i_Cravalho", "Dwayne_Johnson"]},
    {"filme": "Carros", "atores": ["Owen_Wilson", "Larry_the_Cable_Guy"]},
    {"filme": "Divertida_Mente", "atores": ["Amy_Poehler", "Phyllis_Smith"]},
    {"filme": "Shrek", "atores": ["Mike_Myers", "Eddie_Murphy"]},
    {"filme": "Kung_Fu_Panda", "atores": ["Jack_Black", "Dustin_Hoffman"]},
    {"filme": "Homem_de_Ferro", "atores": ["Robert_Downey_Jr.", "Gwyneth_Paltrow"]},
    {"filme": "Capitao_America:_O_Primeiro_Vingador", "atores": ["Chris_Evans", "Hayley_Atwell"]},
    {"filme": "Guardioes_da_Galaxia", "atores": ["Chris_Pratt", "Zoe_Saldana", "Dave_Bautista"]},
    {"filme": "Thor:_Ragnarok", "atores": ["Chris_Hemsworth", "Tom_Hiddleston", "Cate_Blanchett"]},
    {"filme": "Viuva_Negra", "atores": ["Scarlett_Johansson", "Florence_Pugh"]},
    {"filme": "Avatar", "atores": ["Sam_Worthington", "Sigourney_Weaver"]},
    {"filme": "Top_Gun:_Maverick", "atores": ["Tom_Cruise", "Miles_Teller"]},
    {"filme": "Cisne_Negro", "atores": ["Natalie_Portman", "Mila_Kunis"]},
    {"filme": "A_Teoria_de_Tudo", "atores": ["Eddie_Redmayne", "Felicity_Jones"]},
    {"filme": "Bohemian_Rhapsody", "atores": ["Rami_Malek", "Lucy_Boynton"]},
    {"filme": "O_Exorcista", "atores": ["Linda_Blair", "Max_von_Sydow"]},
    {"filme": "Psicose", "atores": ["Anthony_Perkins", "Janet_Leigh"]},
    {"filme": "O_Iluminado", "atores": ["Jack_Nicholson", "Shelley_Duvall"]}
]

filmes_e_diretores = [
    {"filme": "O_Poderoso_Chefao", "diretores": ["Francis_Ford_Coppola"]},
    {"filme": "A_Origem", "diretores": ["Christopher_Nolan"]},
    {"filme": "Titanic", "diretores": ["James_Cameron"]},
    {"filme": "Forrest_Gump", "diretores": ["Robert_Zemeckis"]},
    {"filme": "Matrix", "diretores": ["Lana_Wachowski", "Lilly_Wachowski"]},
    {"filme": "O_Senhor_dos_Aneis:_A_Sociedade_do_Anel", "diretores": ["Peter_Jackson"]},
    {"filme": "Vingadores:_Ultimato", "diretores": ["Anthony_Russo", "Joe_Russo"]},
    {"filme": "Pantera_Negra", "diretores": ["Ryan_Coogler"]},
    {"filme": "Homem-Aranha:_Sem_Volta_para_Casa", "diretores": ["Jon_Watts"]},
    {"filme": "A_Bela_e_a_Fera", "diretores": ["Bill_Condon"]},
    {"filme": "Gladiador", "diretores": ["Ridley_Scott"]},
    {"filme": "Coringa", "diretores": ["Todd_Phillips"]},
    {"filme": "Duna", "diretores": ["Denis_Villeneuve"]},
    {"filme": "Star_Wars:_Uma_Nova_Esperanca", "diretores": ["George_Lucas"]},
    {"filme": "Toy_Story", "diretores": ["John_Lasseter"]},
    {"filme": "Harry_Potter_e_a_Pedra_Filosofal", "diretores": ["Chris_Columbus"]},
    {"filme": "A_Lista_de_Schindler", "diretores": ["Steven_Spielberg"]},
    {"filme": "Pulp_Fiction:_Tempo_de_Violencia", "diretores": ["Quentin_Tarantino"]},
    {"filme": "O_Rei_Leao", "diretores": ["Roger_Allers", "Rob_Minkoff"]},
    {"filme": "Procurando_Nemo", "diretores": ["Andrew_Stanton"]},
    {"filme": "Os_Incriveis", "diretores": ["Brad_Bird"]},
    {"filme": "Frozen:_Uma_Aventura_Congelante", "diretores": ["Chris_Buck", "Jennifer_Lee"]},
    {"filme": "Encanto", "diretores": ["Jared_Bush", "Byron_Howard", "Charise_Castro_Smith"]},
    {"filme": "Moana:_Um_Mar_de_Aventuras", "diretores": ["Ron_Clements", "John_Musker"]},
    {"filme": "Carros", "diretores": ["John_Lasseter", "Joe_Ranft"]},
    {"filme": "Divertida_Mente", "diretores": ["Pete_Docter", "Ronnie_del_Carmen"]},
    {"filme": "Shrek", "diretores": ["Andrew_Adamson", "Vicky_Jenson"]},
    {"filme": "Kung_Fu_Panda", "diretores": ["Mark_Osborne", "John_Stevenson"]},
    {"filme": "Homem_de_Ferro", "diretores": ["Jon_Favreau"]},
    {"filme": "Capitao_America:_O_Primeiro_Vingador", "diretores": ["Joe_Johnston"]},
    {"filme": "Guardioes_da_Galaxia", "diretores": ["James_Gunn"]},
    {"filme": "Thor:_Ragnarok", "diretores": ["Taika_Waititi"]},
    {"filme": "Viuva_Negra", "diretores": ["Cate_Shortland"]},
    {"filme": "Top_Gun:_Maverick", "diretores": ["Joseph_Kosinski"]},
    {"filme": "Cisne_Negro", "diretores": ["Darren_Aronofsky"]},
    {"filme": "A_Teoria_de_Tudo", "diretores": ["James_Marsh"]},
    {"filme": "Bohemian_Rhapsody", "diretores": ["Bryan_Singer"]},
    {"filme": "O_Exorcista", "diretores": ["William_Friedkin"]},
    {"filme": "Psicose", "diretores": ["Alfred_Hitchcock"]},
    {"filme": "O_Iluminado", "diretores": ["Stanley_Kubrick"]}
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
    {"nome": "Tom Cruise"},
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
roteirista = onto.Roteirista('Roteirista01')
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
premio.nome.append('Melhor Roteiro')

premio = onto.Premio('Premio04')
premio.nome.append('Melhor Diretor')

premio = onto.Premio('Premio05')
premio.nome.append('Melhor Fotografia')

premio = onto.Premio('Premio06')
premio.nome.append('Melhor Edição')

premio = onto.Premio('Premio07')
premio.nome.append('Melhor Efeitos Visuais')

premio = onto.Premio('Premio08')
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

def filme_atuadoPor_ator():
    for item in filmes_e_atores:
        filme = item["filme"]
        atores = item["atores"]
        filme = onto.Filme(filme)

        for ator in atores:
            # Busca os indivíduos na ontologia
            ator = onto.Ator(ator)

            # Adiciona o ator ao filme
            filme.atuadoPor.append(ator)

filme_atuadoPor_ator()

def filme_dirigidoPor_diretor():
    for item in filmes_e_diretores:
        filme = item["filme"]
        diretores = item["diretores"]
        filme = onto.Filme(filme)

        for diretor in diretores:
            # Busca os indivíduos na ontologia
            diretor = onto.Diretor(diretor)

            # Adiciona o ator ao filme
            filme.dirigidoPor.append(diretor)

filme_dirigidoPor_diretor()

# Adiciona propriedade entre filme e prêmio
onto.search_one(iri="*O_Poderoso_Chefao").conquistaPremio.append(onto.search_one(iri="*Premio01")) # melhor filme
onto.search_one(iri="*O_Poderoso_Chefao").conquistaPremio.append(onto.search_one(iri="*Premio02"))  # melhor ator
onto.search_one(iri="*O_Poderoso_Chefao").conquistaPremio.append(onto.search_one(iri="*Premio03"))  # melhor roteiro

onto.search_one(iri="*Titanic").conquistaPremio.append(onto.search_one(iri="*Premio01"))  # melhor filme
onto.search_one(iri="*Titanic").conquistaPremio.append(onto.search_one(iri="*Premio04"))  # melhor diretor
onto.search_one(iri="*Titanic").conquistaPremio.append(onto.search_one(iri="*Premio08"))  # melhor trilha sonora

onto.search_one(iri="*Matrix").conquistaPremio.append(onto.search_one(iri="*Premio06"))  # melhor edição
onto.search_one(iri="*Matrix").conquistaPremio.append(onto.search_one(iri="*Premio07"))  # melhor efeitos visuais

onto.search_one(iri="*O_Senhor_dos_Aneis:_A_Sociedade_do_Anel").conquistaPremio.append(onto.search_one(iri="*Premio07"))  # melhor efeitos visuais
onto.search_one(iri="*O_Senhor_dos_Aneis:_A_Sociedade_do_Anel").conquistaPremio.append(onto.search_one(iri="*Premio05"))  # melhor fotografia

onto.search_one(iri="*Coringa").conquistaPremio.append(onto.search_one(iri="*Premio02"))  # melhor ator
onto.search_one(iri="*Coringa").conquistaPremio.append(onto.search_one(iri="*Premio08"))  # melhor trilha sonora


# Adiciona propriedade entre prêmio e evento
onto.search_one(iri="*Premio01").dadoEm.append(onto.search_one(iri="*Evento01"))  # Oscar 1973
onto.search_one(iri="*Premio02").dadoEm.append(onto.search_one(iri="*Evento01"))
onto.search_one(iri="*Premio03").dadoEm.append(onto.search_one(iri="*Evento01"))
onto.search_one(iri="*Premio04").dadoEm.append(onto.search_one(iri="*Evento01"))
onto.search_one(iri="*Premio05").dadoEm.append(onto.search_one(iri="*Evento01"))
onto.search_one(iri="*Premio06").dadoEm.append(onto.search_one(iri="*Evento01"))
onto.search_one(iri="*Premio07").dadoEm.append(onto.search_one(iri="*Evento01"))
onto.search_one(iri="*Premio08").dadoEm.append(onto.search_one(iri="*Evento01"))

onto.search_one(iri="*Premio01").dadoEm.append(onto.search_one(iri="*Evento02"))  # Globo de Ouro 1973
onto.search_one(iri="*Premio02").dadoEm.append(onto.search_one(iri="*Evento02"))
onto.search_one(iri="*Premio03").dadoEm.append(onto.search_one(iri="*Evento02"))
onto.search_one(iri="*Premio04").dadoEm.append(onto.search_one(iri="*Evento02"))
onto.search_one(iri="*Premio05").dadoEm.append(onto.search_one(iri="*Evento02"))
onto.search_one(iri="*Premio06").dadoEm.append(onto.search_one(iri="*Evento02"))
onto.search_one(iri="*Premio07").dadoEm.append(onto.search_one(iri="*Evento02"))
onto.search_one(iri="*Premio08").dadoEm.append(onto.search_one(iri="*Evento02"))

onto.search_one(iri="*Premio01").dadoEm.append(onto.search_one(iri="*Evento03"))  # Oscar 1998
onto.search_one(iri="*Premio02").dadoEm.append(onto.search_one(iri="*Evento03"))
onto.search_one(iri="*Premio03").dadoEm.append(onto.search_one(iri="*Evento03"))
onto.search_one(iri="*Premio04").dadoEm.append(onto.search_one(iri="*Evento03"))
onto.search_one(iri="*Premio05").dadoEm.append(onto.search_one(iri="*Evento03"))
onto.search_one(iri="*Premio06").dadoEm.append(onto.search_one(iri="*Evento03"))
onto.search_one(iri="*Premio07").dadoEm.append(onto.search_one(iri="*Evento03"))
onto.search_one(iri="*Premio08").dadoEm.append(onto.search_one(iri="*Evento03"))

onto.search_one(iri="*Premio01").dadoEm.append(onto.search_one(iri="*Evento04"))  # Globo de Ouro 1998
onto.search_one(iri="*Premio02").dadoEm.append(onto.search_one(iri="*Evento04"))
onto.search_one(iri="*Premio03").dadoEm.append(onto.search_one(iri="*Evento04"))
onto.search_one(iri="*Premio04").dadoEm.append(onto.search_one(iri="*Evento04"))
onto.search_one(iri="*Premio05").dadoEm.append(onto.search_one(iri="*Evento04"))
onto.search_one(iri="*Premio06").dadoEm.append(onto.search_one(iri="*Evento04"))
onto.search_one(iri="*Premio07").dadoEm.append(onto.search_one(iri="*Evento04"))
onto.search_one(iri="*Premio08").dadoEm.append(onto.search_one(iri="*Evento04"))


# Adiciona propriedade entre produtor e filme
onto.search_one(iri="*Produtor01").produzFilme.append(onto.search_one(iri="*A_Origem"))  
onto.search_one(iri="*Produtor02").produzFilme.append(onto.search_one(iri="*Titanic"))
onto.search_one(iri="*Produtor03").produzFilme.append(onto.search_one(iri="*Forrest_Gump"))
onto.search_one(iri="*Produtor04").produzFilme.append(onto.search_one(iri="*Forrest_Gump"))
onto.search_one(iri="*Produtor05").produzFilme.append(onto.search_one(iri="*Matrix"))


# Adiciona propriedade entre roteirista e filme
onto.search_one(iri="*Roteirista01").criaRoteiro.append(onto.search_one(iri="*Divertida_Mente"))  
onto.search_one(iri="*Roteirista02").criaRoteiro.append(onto.search_one(iri="*Shrek"))
onto.search_one(iri="*Roteirista03").criaRoteiro.append(onto.search_one(iri="*Kung_Fu_Panda"))
onto.search_one(iri="*Roteirista04").criaRoteiro.append(onto.search_one(iri="*Homem_de_Ferro"))
onto.search_one(iri="*Roteirista05").criaRoteiro.append(onto.search_one(iri="*Homem_de_Ferro"))
onto.search_one(iri="*Roteirista06").criaRoteiro.append(onto.search_one(iri="*Capitao_America:_O_Primeiro_Vingador"))

# Busca uma instância de uma classe pelo nome (iri parcial).
def buscar_instancia(classe, nome):       
    return onto.search_one(iri=f"*{nome}")

#Cria uma avaliação apenas se o mesmo usuário não avaliou o mesmo filme antes.
def criar_avaliacao(nome_avaliacao, nome_usuario, nome_filme, nota):

    # Busca as instâncias do usuário e do filme
    usuario = buscar_instancia(onto.Usuario, nome_usuario)
    filme = buscar_instancia(onto.Filme, nome_filme)

    if not usuario:
        print(f"Erro: Usuário '{nome_usuario}' não encontrado.")
        return
    if not filme:
        print(f"Erro: Filme '{nome_filme}' não encontrado.")
        return

    # Verifica se já existe uma avaliação feita pelo usuário para o mesmo filme
    avaliacao_existente = onto.search(type=onto.Avaliacao, avaliadoPor=usuario, pertenceAoFilme=filme)
    
    if avaliacao_existente:
        print(f"Erro: {usuario.name} já avaliou o filme {filme.name}. Avaliação não permitida.")
    else:
        # Cria uma nova avaliação
        nova_avaliacao = onto.Avaliacao(nome_avaliacao)
        nova_avaliacao.nota.append(nota)
        nova_avaliacao.avaliadoPor.append(usuario)
        nova_avaliacao.pertenceAoFilme.append(filme)

        
# Iterar sobre todas as instâncias de Usuario e Filme
usuarios = [u.name for u in onto.Usuario.instances()]  
filmes = [f.name for f in onto.Filme.instances()]     

# Notas e suas probabilidades
notas = [1, 2, 3, 4, 5]
probabilidades = [0.1, 0.2, 0.3, 0.2, 0.2]

# Ponto de corte para dividir os filmes
ponto_corte = 21

# Criar avaliações alternando entre os intervalos de filmes para cada usuário
avaliacao_id = 1  # Contador para os nomes das avaliações
for i, usuario in enumerate(usuarios):
    # Se o índice do usuário for par, ele avalia os primeiros 21 filmes, se for ímpar, avalia do 21 em diante
    if i % 2 == 0:
        filmes_para_avaliar = filmes[:ponto_corte]  # 21 primeiros filmes
    else:
        filmes_para_avaliar = filmes[ponto_corte:]  # Filmes do 22º em diante

    # Iteração sobre os filmes a serem avaliados
    for filme in filmes_para_avaliar:
        nota = random.choices(notas, probabilidades, k=1)[0]  # Gera uma nota de 1 a 5
        criar_avaliacao(f"Aval{avaliacao_id}", usuario, filme, nota)  # Chama a função para criar a avaliação
        avaliacao_id += 1  # Incrementa o ID da avaliação


#print([filme.name for filme in onto.Filme.instances()])
# print()
# print([ator.name for ator in onto.Ator.instances()])


#for diretores in onto.Diretor.instances():
#    print(diretores)

#print(dir(onto))
#print(list(onto.properties()))

# Salvar as alterações no RDF com identificadores únicos
onto.save(file="filmes_atualizado_com_ids.rdf")