#  if /   elif    / else 
#  se / se nao se / se nao

entrada = input('Você quer "entrar" ou "sair" do sistema?: ')

print('-' * 15)

if entrada == 'entrar':
    print('Você Entrou no Sistema')
elif entrada == 'sair':
    print('Você Saiu do Sistema')
else:
    print('Você não digitou se quer "entrar" ou "sair" do sistema...')
#fora do bloco do if/else
#pode até estar fora de um bloco de reptição como for ou while
print('-' * 15)



