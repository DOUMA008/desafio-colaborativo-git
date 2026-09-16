while True:
    print("====Calculadora====")
    print("1. Suma")
    print("2. subtração") 
    print("3. divisão")
    print("4. multiplicação")
    print("5. sair")
    print("====================") 
    
    opcao = input("Escolha uma opção: ")
    if opcao == "5":
        print("Saindo da calculadora...")
        break
    
    if opcao == "1":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print("O resultado da soma é:", resultado)