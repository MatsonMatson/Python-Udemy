import emoji

# Uma das maneira de formata os codigos
a = 'Aa'
b = 'Bb'
c = 'Cc'
string = 'a={0}, b={1}, c={2:.2f}'
formato = string.format(a, b, c)

print(formato)

# Outra forma e melhor(minha opnião)
# é utilizando o f como por exempo
nome = 'matso'
print(f'olá {nome}, tudo bem!?')
#método mt mais facil...

print(emoji.emojize(':fox:'))

