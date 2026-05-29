# Construir um programa em Python que gera um cartão digital de desenvolvedor no terminal.
# usando: variáveis, input(), conversão de tipos, operadores aritméticos, condicionais (if/elif/else) e f-strings.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: (apenas números) "))
linguagem_favorita = input("Digite sua linguagem de programação favorita: ")
anos_estudados = int(input("Digite quantos anos você tem estudado programação: (apenas números) "))

if anos_estudados == 0:
    nivel_xp = 10 
else:
    nivel_xp = anos_estudados * 100


print("\n" + "=" * 42)
print("======= CARTÃO DIGITAL DE DESENVOLVEDOR =======")
print("=" * 42)
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Linguagem Favorita: {linguagem_favorita}")
print(f"Anos Estudados: {anos_estudados}")
print(f"Nível de XP: {nivel_xp}")
print("=" * 42)

