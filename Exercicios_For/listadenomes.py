

# Lista de clientes com informações: nome, email, telefone e data de nascimento


clientes = [
    {
        "nome": "João Silva", "email": "joao.silva@email.com", "telefone": "(11) 91234-5678", "data_nascimento": "1990-05-15"
    },
    {   "nome": "Maria Oliveira", "email": "maria.oliveira@email.com", "telefone": "(21) 99876-5432","data_nascimento": "1985-08-22"
    },
    {   "nome": "Carlos Pereira", "email": "carlos.pereira@email.com", "telefone": "(31) 98765-4321", "data_nascimento": "1978-12-10"
    },
    {   "nome": "Ana Santos", "email": "ana.santos@email.com", "telefone": "(41) 91234-9876", "data_nascimento": "1992-03-05"
    },
    {   "nome": "Pedro Lima", "email": "pedro.lima@email.com", "telefone": "(51) 99876-1234", "data_nascimento": "1988-07-19"
    },
    {   "nome": "Luana Costa", "email": "luana.costa@email.com", "telefone": "(61) 91234-5678", "data_nascimento": "1995-11-30"
    },
    {   "nome": "Felipe Almeida", "email": "felipe.almeida@email.com", "telefone": "(71) 98765-4321", "data_nascimento": "1982-04-25"
    },
    {   "nome": "Sofia Martins", "email": "sofia.martins@email.com", "telefone": "(81) 99876-5432", "data_nascimento": "1993-09-14"
    },
    {   "nome": "Rafael Gomes", "email": "rafael.gomes@email.com", "telefone": "(91) 91234-6789", "data_nascimento": "1987-02-08"
    },
    {   "nome": "Camila Rocha", "email": "camila.rocha@email.com", "telefone": "(99) 98765-4321", "data_nascimento": "1991-06-21"
    }
]

# Exemplo de como acessar os dados
for cliente in clientes:
    print(f"Nome: {cliente['nome']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}, Data de Nascimento: {cliente['data_nascimento']}")