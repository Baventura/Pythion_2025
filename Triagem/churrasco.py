# calculadora de churrasco bevenuto

def churrasco (pessoas, horas): #def significa definicao de uma fincao
    carne_hora = 0.350
    total_carne = pessoas * horas * carne_hora
    return f"Vai precisar de {total_carne} kg de fraldinha!"
print(churrasco(100,10))

