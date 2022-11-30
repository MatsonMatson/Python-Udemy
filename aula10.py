import emoji
"""
PRECEDÊNCIA DOS OPERADORES
1. (n1 + n2) parenteses são executados de dentro pra fora 
2. **
3. * -> / -> // -> %
4. + | -
"""
print('-' * 10)

conta1 = 1 + 1 ** 5 + 5 # 7
print(conta1)

print('-' * 10)

conta2 = (1 + 1) ** 5 + 5 # 37
print(conta2)

print('-' * 10)

print(emoji.emojize(':fox:'))
