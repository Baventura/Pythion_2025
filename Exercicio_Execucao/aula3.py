# Estrutura de decisao

# if = se
# else = senao
# elife = senao se
# maior que >
# manor que <
# maior ou igual >=
# menor ou igual <=
# igualdade ==
# diferente != ou <>
# and = e
# or =ou

import os
os.system("cls")

idade = int(input("Digite a idade: "))

if idade <= 16:
    print("Voto não obrigatorio")
else: 
    if idade <=17 or idade >= 65:
        print("Nâo é obrigatorio")
    else:
        print("Obrigatorio")


