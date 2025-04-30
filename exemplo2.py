print("Bem-vindo a introdução ao Python!")
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

#Cálculo da Média
media = (a + b) / 2

#Estruturas Condicionais
if media > 7:
    print(f"Sua média foi de {media}, PARABÉNS!")
elif media <= 7 and media > 4:
    print(f"Sua média foi de {media}, você está na FINAL!")
else:
    print("Sua média foi de {media}, você está de RECUPERAÇÃO!")