nome = str(input('Digite seu Nome: '))
sobrenome = str(input('Seu Sobrenome: '))
idade = int(input('Digite sua Idade: '))
nasc = 2022 - idade
altura = float(input('Sua Altura em metros: '))

print(nome)
print(sobrenome)
print(idade)
if idade >= 18:
    print(f'É maior de idade e tem {idade} anos')
else:
    print(f'É menor de idade e tem {idade} anos')
print(nasc)
print(altura)
