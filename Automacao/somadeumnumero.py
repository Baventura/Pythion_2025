soma = 0
while True:
    numero = float(input("Digite um numero para somar ou 0 para sair: ")) # 
    if numero == 0: # if significa se
        break
    soma += numero # += significa soma = soma + numero
    print(soma)
print(f"A soma de todos os numeros digitados é {soma}") 