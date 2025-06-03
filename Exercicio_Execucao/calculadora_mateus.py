

a = float(input("Digite um numero: "))
operador = input("Digite um operador: ")
b = float(input("Digite um numero: "))
if  operador == "+":
    resultado = a + b
    print(resultado)
elif operador == '-':
    resultado = a + b
    print(resultado)
elif operador == '*':
    resultado = a * b
    print(resultado)
elif operador == '/':
    if a and b != 0:
        resultado = a/ b
        print (resultado)
    else:
        print("Divisão invalida")
else:
    print("Operador invalido")