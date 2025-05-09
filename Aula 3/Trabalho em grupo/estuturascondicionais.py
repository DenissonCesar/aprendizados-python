alunos = ["Denisson", "Arthur", "Jonathan", "Tiago", "Luis Otávio", "Gabriel"]

#Estruturas condicional simples

idade = 17
if idade >= 18:
    print("Você pode dirigir")


#Estrutura condicional composta

if idade < 18:
    print("Você não pode dirigir")
else:
    print("Você pode dirigir")

#Estrutura condiconal múltipla

peso = 75
altura = 1.80
resultadoimc = peso / (altura * altura)

if resultadoimc < 18.5: 
    print("Baixo peso")
elif resultadoimc >= 18.5 and resultadoimc < 24.9:
    print("Normal")
elif resultadoimc >= 25 and resultadoimc < 29.9:
    print("Sobrepeso")
elif resultadoimc >= 30 and resultadoimc < 34.9:
    print("Obesidade nível 1")
elif resultadoimc >= 35 and resultadoimc < 39.9:
    print("Obesidade nível 2")
else:
    print("Obesidade grau 3 (mórbida)")

#Estrutura condicional ternário

mensagem = "Pode dirigir" if idade >= 18 else "Menor não pode dirigir"
print(mensagem)