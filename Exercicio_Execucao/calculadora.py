
# Calculadora simples usando if, elif e else

# Solicitando ao usuário os números e o operador
numero1 = float(input("Digite o primeiro número: "))
operador = input("Digite o operador (+, -, *, /): ")
numero2 = float(input("Digite o segundo número: "))

# Verificando o operador e realizando a operação
if operador == '+':
    resultado = numero1 + numero2
    print(f"Resultado: {numero1} + {numero2} = {resultado}")
elif operador == '-':
    resultado = numero1 - numero2
    print(f"Resultado: {numero1} - {numero2} = {resultado}")
elif operador == '*':
    resultado = numero1 * numero2
    print(f"Resultado: {numero1} * {numero2} = {resultado}")
elif operador == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"Resultado: {numero1} / {numero2} = {resultado}")
    else:
        print("Erro: divisão por zero não é permitida.")
else:
    print("Operador inválido! Use apenas +, -, * ou /.")










