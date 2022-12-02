# nome = input('Qual o seu nome?: ')
# print(f'O seu nome é {nome}')
# o input sozinhofunviona como str, basicamente não precisa ter um str(input()) qd o input ta sozinho

num1 = input('Digite um número: ')
num2 = input('Digite ouro número: ')
#para numero no input, precisa converter em outra variavel
#ou manda um int(input()) mais facil...
int_num1 = int(num1)
int_num2 = int(num2)

print(f'A soma dos dois números é {num1 + num2}')
# da pra obter o resultado dessa forma q esta nas chaves
#eu prefiro uma variavel q receba o resultado, mas ok.


