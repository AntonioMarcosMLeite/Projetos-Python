import random

print('Gerador de senha')

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%"&*().,?'

qtd_senhas = int(input('Informe a quantidade de senhas a ser gerada: '))
qtd_caracteres = int(input('Informe a quantidade de caracteres da senha: '))


for senha in range(qtd_senhas):
    senha = ''
    for num in range(qtd_caracteres):
        senha += random.choice(caracteres)
    print(senha)