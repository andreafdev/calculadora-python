def soma(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


while True:
    num1 = int(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    num2 = int(input("Digite o segundo número: "))

    if operacao == '+':
        print(f"Resultado da soma é: {soma(num1, num2)}")

    elif operacao == '-':
        print(f"Resultado da subtração é: {sub(num1, num2)}")

    elif operacao == '*':
        print(f"Resultado da multiplicação é: {mult(num1, num2)}")

    elif operacao == '/':
        if num2 != 0:  # Adicionei esta verificação para evitar divisão por zero
            print(f"Resultado da divisão é: {div(num1, num2)}")
        else:
            print("Erro: Divisão por zero não é permitida.")

    else:
        print("Operação inválida.")
