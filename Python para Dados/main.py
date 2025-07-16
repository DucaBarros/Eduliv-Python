import pandas as pd

# Criando uma lista de dicionários (pessoas)
users_list = [
    {
        "nome": "Paulo",
        "idade": 50,
        "sexo": "Masculino",
        "endereco": "Sidney Chaves",
        "nacionalidade": "Brasileiro"
        },
    {
        "nome": "Fran",
        "idade": 25,
        "sexo": "Feminino",
        "endereco": "Vila Velha",
        "nacionalidade": "Brasileira"
        },
    {
        "nome": "João",
        "idade": 30,
        "sexo": "Masulino",
        "endereco": "Vitória",
        "nacionalidade": "Brasileira"
        }
]

print(users_list)

# df_ is a convention for dataframe
df_users = pd.DataFrame(users_list)
print('DATA_FRAME', df_users)
