def imc(altura, peso):
    #altura = input("Digite a sua altura: ")
    #peso = input("Digite o seu peso: ")

    resultado = peso / (altura * altura)
    print(resultado)
    if resultado < 18.5:
        print("Abaixo do peso")
    elif resultado > 18.5 and resultado < 24.9:
        print("Peso normal")
    elif resultado > 25 and resultado < 29.9:
        print("Sobrepeso")
    elif resultado > 30 and resultado < 34.9:
        print("Obesidade Grau I")
    elif resultado > 35 and resultado < 39.9:
        print("Obesidade Grau II")
    else:
        print("Obesidade III (mórbida)")

denisson = imc(1.80, 200)