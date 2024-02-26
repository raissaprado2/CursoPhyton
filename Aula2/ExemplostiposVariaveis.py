#Números Inteiros e de Ponto Flutuante :

# Números inteiros

idade = 25
quantidade_produtos = 100

# Números de ponto flutuante
preco_unitario = 29.99
pi = 3.14159

#Strings (Cadeias de Caracteres) :

# Strings simples
nome = "Alice"
mensagem = 'Olá, seja bem-vindo!'

# Concatenação de strings
nome_completo = nome + " Wonderland"

# Formatação de strings
mensagem_formatada = f"Olá, {nome}! Você tem {idade} anos."
print(mensagem_formatada)


#Listas e Tuplas:

# Listas (mutáveis)
frutas = ["maçã", "banana", "uva"]
numeros = [1, 2, 3, 4, 5]

# Adicionando elementos a uma lista
frutas.append("laranja")

# Tuplas (imutáveis)
coordenadas = (4, 5)
cores_rgb = (255, 0, 0)
cores_rgb.append(155)
print(frutas[0])
print(cores_rgb)

#Dicionários:

# Dicionário chave-valor
pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "profissao": "engenheiro"
}

# Acessando valores
print(pessoa["nome"])
print(pessoa.get("idade"))

# Adicionando novo par chave-valor
pessoa["cidade"] = "São Paulo"

#Booleans:

# Variáveis booleanas
tem_cafe = True
tem_cha = False

# Expressões booleanas
tem_bebida_quente = tem_cafe or tem_cha
tem_as_dois = tem_cafe and tem_cha
print(tem_bebida_quente)
print(tem_as_dois)

