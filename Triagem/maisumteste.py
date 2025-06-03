while True:
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        print("Acesso à festa concedido")
    else:
        print("ENTRADA PROIBIDA")
    
    while True:
        continuar = input("Deseja verificar mais alguma idade [S OU N]: ").upper()
        if continuar in ['S', 'N']:
            break
        else:
            print("Por favor, digite 'S' ou 'N', ou Digite novamente sua idade: ")
    
    if continuar == "N":
        break


print("Fim da verificação")