#Instruções para entrega

# 1️⃣ Desafio Classificador de nível de Herói

#**O Que deve ser utilizado**

#- Variáveis
#- Operadores
#- Laços de repetição
#- Estruturas de decisões

## Objetivo

#Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, 
# depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

#Se XP for menor do que 1.000 = Ferro
#Se XP for entre 1.001 e 2.000 = Bronze
#Se XP for entre 2.001 e 5.000 = Prata
#Se XP for entre 5.001 e 7.000 = Ouro
#Se XP for entre 7.001 e 8.000 = Platina
#Se XP for entre 8.001 e 9.000 = Ascendente
#Se XP for entre 9.001 e 10.000= Imortal
#Se XP for maior ou igual a 10.001 = Radiante

## Saída

#Ao final deve se exibir uma mensagem:
#"O Herói de nome **{nome}** está no nível de **{nivel}**"

nome = str(input("Digite o nome do Herói: "))
ex = int(input("Digite seu nével de XP:(0 a <10000) "))

classe =''

if ex <= 1000:
    classe = 'Ferro'
elif 1001 < ex <= 2000:
    classe = 'Bronze'
elif 2001 < ex <= 5000:
    classe = 'Prata'
elif 5001 < ex <= 7000:
    classe = 'Ouro'
elif 7001 < ex <= 8000:
    classe = 'Platina'
elif 8001 < ex <= 9000:
    classe = 'Ascendente'
elif 9001 < ex <= 10000:
    classe = 'Imortal'
elif ex >= 10001:
    classe = 'Radiante'

print(f'O Herói/Heroína {nome} está no nível {classe}')
