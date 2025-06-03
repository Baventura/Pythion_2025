#criando uma calculadora

def calculadora():
    print ("========== CALCULADORA SIMPLES ======")
    print("operacoes Disponiveis:")
    print("1 - Soma (+)")
    print("2 -Subtracao (-)")

    operacao = input ("Escolha a operacao (1 ou 2):")

    if operacao == "1" :
        num1 = float (input("Digite o primeiro numero: "))
        num2 = float (input("Digite o segundo numero: "))
        resultado = num1 + num2
        print(f"Resultado da soma: {resultado} ")

    elif operacao == '2':
        num1 = float (input ('Digite o primeiro numero: '))
        num2 = float (input ('Digite o segundo numero: '))
        resultado =num1 -num2
        print(f'Resultado da subtracao: {resultado}')
        
    else:
        print (f'Operacão invalida. tente novamente')
    calculadora()


