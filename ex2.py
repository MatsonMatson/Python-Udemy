import emoji
from time import sleep
nome = str(input('Digite seu Nome: '))
peso = float(input('Digite seu Peso: '))
altura = float(input('Digite sua Altura: '))
imc = peso / (altura * altura)

print('-' * 15)

print(f'Olá {nome}, Tudo Bem!?')
sleep(1)
print('irei calcular seu imc, pra isso pegarei suas informações...')
sleep(1)
print(f'Seu peso é {peso}')
sleep(1)
print(f'Sua Altura é {altura}')
sleep(1)
print('Com seus dados posso calcular seu IMC, que é...')
sleep(1)
print(f'Seu IMC é de {imc}')

print('-' * 15)
print(emoji.emojize(':fox:'))

