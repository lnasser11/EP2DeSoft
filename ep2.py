#Projeto de Design de Software EP2 Felipe Maia e Lucca Nasser
#Criar um jogo de adivinhação de países

import random as rd
from math import *
from funcoes import *
import json

#Importando os dicionário com os países
with open('dados.json', 'r') as pre_norm:
  dados_pn = pre_norm.read()

dic_dados = json.loads(dados_pn)
dados = normaliza(dic_dados)

EARTH_RADIUS = 6371

print('=====================================\n|                                   |\n|    Bem vindo ao Insper Países!    |\n|                                   |\n======== Design de Software =========')
print(' ')
print('Comandos:\n   dica       - entra no mercado de dicas\n   desisto    - desiste da rodada\n   inventario - exibe sua pontuação')

print('Chute um país até acertar para vencer!\nEscreva em letras minúsculas e sem acento!')

pais_sorteado = sorteia_pais(dados)

print(' ')
print(' ')
print(' ')

facil = cor(36, 255, 160, '20')
medio = cor(255, 248, 36, '10')
dificil = cor(255, 69, 36, '5')

facil_str = cor(36, 255, 160,'Fácil')
medio_str = cor(255, 248, 36, 'Médio')
dificil_str = cor(255, 69, 36, 'Difícil')

escolha_dificuldade = cor(37, 203, 245, '1|2|3')
#Define a dificuldade do jogo
dif = int(input(f'Escolha sua dificuldade:\n   1. {facil_str} --> {facil} tentativas\n   2. {medio_str} --> {medio} tentativas\n   3. {dificil_str} --> {dificil} tentativas\n    Dificuldade escolhida [ {escolha_dificuldade}]: '))
if dif == 1:
  tentativas = 20
elif dif == 2:
  tentativas = 10
elif dif == 3:
  tentativas = 5


print(' ')
print(' ')
print(' ')

print('Um país foi sorteado! Boa sorte!')

print(' ')
print(' ')
print(' ')


i = 0
c = 0 # Index das letras da capital para a dica 2 
d = 0 # index das distancias



header = '========================================'
cdica1 = cor(66, 135, 245,'4')
cdica2 = cor(66, 135, 245,'3')
cdica3 = cor(66, 135, 245,'6')
cdica4 = cor(66, 135, 245,'5')
cdica5 = cor(66, 135, 245,'7')
cdica6 = cor(66, 135, 245,'0')

dic_dicas = {
  1: f'1. Cor da bandeira  - custa {cdica1} tentativas.',
  2: f'2. Letra da capital - custa {cdica2} tentativas.',
  3: f'3. Área             - custa {cdica3} tentativas.',
  4: f'4. População        - custa {cdica4} tentativas.',
  5: f'5. Continente       - custa {cdica5} tentativas.',
  6: f'6. Sair do mercado.'
}

custo_dicas = {
        1: 4, 
        2: 3,
        3: 6,
        4: 5,
        5: 7,
        6: 0
              }


# Dados do País sorteado em variáveis
area = (dados[pais_sorteado])['area']
populacao = (dados[pais_sorteado])['populacao']
capital = (dados[pais_sorteado])['capital']
latitude = ((dados[pais_sorteado])['geo'])['latitude']
longitude = ((dados[pais_sorteado])['geo'])['longitude']
bandeira = (dados[pais_sorteado])['bandeira']
continente = (dados[pais_sorteado])['continente']

# Listas Auxiliares
lista_distancias = []
lista_chutes = []
lista_tentativas = []
capital_str = ''

if tentativas > 10:
  print(f'Tentativas restantes:', f'\033[0;32m {tentativas}\033[0;0m')
elif tentativas <= 10 and tentativas > 5:
  print(f'Tentativas restantes:', f'\033[0;33m {tentativas}\033[0;0m')
elif tentativas <= 5:
  print(f'Tentativas restantes:', f'\033[0;31m {tentativas}\033[0;0m')

while tentativas > 0:
  jogada = input('Qual a sua jogada? ')
  i += 1

  if jogada != pais_sorteado and jogada != "dica" and jogada != "inventario" and jogada != "desisto" and jogada in dados and jogada not in lista_tentativas:
    print('Errado!') 
    tentativas -= 1

  if jogada in lista_tentativas and jogada in dados:
    print(f'Você já chutou {jogada}! Tente com outro país!')

  lista_tentativas.append(jogada)
  
  if jogada not in dados and jogada != (1,2,3,4,5,6) and jogada != 'dica' and jogada != 'inventario':
    print('País desconhecido.')

  if jogada in dados:
    distancia = haversine(EARTH_RADIUS, ((dados[jogada])['geo'])['latitude'], ((dados[jogada])['geo'])['longitude'], latitude, longitude)
    if distancia not in lista_distancias:
      lista_distancias.append(distancia)
    if jogada not in lista_chutes:
      lista_chutes.append(jogada)
    print('Distâncias: ')
    for i in lista_distancias:
      print(f'    \033[0;35m{i:.2f} KM --> {lista_chutes[lista_distancias.index(i)]}\033[0;0m')


  if jogada == 'dica':
    print(header)
    for index, dica in dic_dicas.items():
      if tentativas > custo_dicas[index]:
        print(dic_dicas[index])
    print(header)

    dica = int(input(f'Escolha sua opção [1|2|3|4|5|6]: '))

    if dica == 1: #dica 1
      print(f'A cor predominante da bandeira é: {cor_predominante(bandeira)}')
      tentativas -= 4
      del dic_dicas[1]

    elif dica == 2: #dica 2
      print(f'A próxima letra da Capital é:', f'\033[0,33m {capital[c]}\033[0,0m')
      capital_str += capital[c]
      print(f'Letras obtidas por enquanto: {capital_str}')
      tentativas -= 3
      c+=1
      if len(capital)-1 == c:
        del dic_dicas[2]

    elif dica == 3: #dica 3
      print(f'A área do país é: {area}')
      del dic_dicas[3]
      tentativas -= 6

    elif dica == 4: #dica 4
      print(f'{populacao} pessoas.')
      tentativas -= 5
      del dic_dicas[4]

    elif dica == 5: #dica 5
      print(f'Está no continente: {continente}')
      tentativas -= 7
      del dic_dicas[4]

    elif dica == 6: #dica 6
      print('\n\nVoltando ao jogo!\n\n')
      
  if jogada == "inventario":
    print(tentativas)
  

  
  if tentativas > 10:
    print(f'Tentativas restantes:', f'\033[0;32m {tentativas}\033[0;0m')
  elif tentativas <= 10 and tentativas > 5:
    print(f'Tentativas restantes:', f'\033[0;33m {tentativas}\033[0;0m')
  elif tentativas <= 5:
    print(f'Tentativas restantes:', f'\033[0;31m {tentativas}\033[0;0m')

  if jogada == pais_sorteado:
    print(f'Parabéns! Você adivinhou o país "{pais_sorteado}" que eu escolhi em {i} tentativas!')
    print('Finalizando jogo...')
    tentativas = 0

  
  if jogada == 'desisto':
    print('Finalizando jogo...')
    tentativas = 0

print('')
print('')
print('')

print('Fim de jogo! \n')
print(f'O país sortedo era {pais_sorteado}!')
print(bandeira)