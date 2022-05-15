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

pais_sorteado = sorteia_pais(dados)

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
lista_dist_colorido = []
lista_tentativas = []
lista_dicas = [1,2,3,4,5,6]
capital_str = ''
inventario = {}
dic_distancia = {} #dicionario de distancias
jogar_novamente = True

indice_jogada = 1
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

facil = cor(36, 255, 160, '20')
medio = cor(255, 248, 36, '10')
dificil = cor(255, 69, 36, '5')

facil_str = cor(36, 255, 160,'Fácil')
medio_str = cor(255, 248, 36, 'Médio')
dificil_str = cor(255, 69, 36, 'Difícil')

um = cor(36, 255, 160,'1')
dois = cor(255, 248, 36, '2')
tres = cor(255, 69, 36, '3')

escolha_dificuldade = f'[{um}|{dois}|{tres}]'

tentativas = 0

print('=====================================\n|                                   |\n|    Bem vindo ao Insper Países!    |\n|                                   |\n======== Design de Software =========')
print(' ')
print('Comandos:\n   dica       - entra no mercado de dicas\n   desisto    - desiste da rodada\n   inventario - exibe sua pontuação')
print('Chute um país até acertar para vencer!\nEscreva em letras minúsculas e sem acento!')
print(' ')
print(' ')
print(' ')

while jogar_novamente:

  #Define a dificuldade do jogo
  dif = input(f'Escolha sua dificuldade:\n   1. {facil_str} --> {facil} tentativas\n   2. {medio_str} --> {medio} tentativas\n   3. {dificil_str} --> {dificil} tentativas\n    Dificuldade escolhida {escolha_dificuldade}: ')
  if dif == '1':
    tentativas += 20
  elif dif == '2':
    tentativas += 10
  elif dif == '3':
    tentativas += 5

  if dif != '1' or dif != '2' or dif != '3':
    while dif != '1' and dif != '2' and dif != '3':
      dif = input(f'Escolha uma opção válida. {escolha_dificuldade}: ')
      if dif == '1':
        tentativas += 20
      elif dif == '2':
        tentativas += 10
      elif dif == '3':
        tentativas += 5



  print(' ')
  print(' ')
  print(' ')

  print('Um país foi sorteado! Boa sorte!')

  print(' ')
  print(' ')
  print(' ')


  if tentativas > 10:
    print(f'Tentativas restantes:', f'\033[0;32m {tentativas}\033[0;0m')
  elif tentativas <= 10 and tentativas > 5:
    print(f'Tentativas restantes:', f'\033[0;33m {tentativas}\033[0;0m')
  elif tentativas <= 5:
    print(f'Tentativas restantes:', f'\033[0;31m {tentativas}\033[0;0m')

  while tentativas > 0:
    jogada = input('Qual a sua jogada? ')


    if jogada != pais_sorteado and jogada != "dica" and jogada != "inventario" and jogada != "desisto" and jogada in dados and jogada not in lista_tentativas:
      print('Errado!') 
      tentativas -= 1
      indice_jogada += 1

    if jogada in lista_tentativas and jogada in dados:
      print(f'Você já chutou {jogada}! Tente com outro país!')

    lista_tentativas.append(jogada)
    
    if jogada not in dados and jogada != (1,2,3,4,5,6) and jogada != 'dica' and jogada != 'inventario' and jogada != 'desisto':
      print('País desconhecido.')

    if jogada == 'dica':
      print(header)
      for index, dica in dic_dicas.items():
        if tentativas > custo_dicas[index]:
          print(dic_dicas[index])
      print(header)

      dica = int(input(f'Escolha sua opção: '))

      if dica >= 7 or dica not in lista_dicas: 
        print('Por favor, escolha uma dica que esteja no mercado.')

      elif dica == 1 and dica in lista_dicas: #dica 1
        cor_pais = cor_predominante(bandeira)
        print(f'A cor predominante da bandeira é: {cor_pais}')
        tentativas -= 4
        inventario['Cor da bandeira: '] = cor_pais
        del dic_dicas[1]
        del lista_dicas[0]

      elif dica == 2 and dica in  lista_dicas: #dica 2
        if tentativas < 3:  
          print('Você não pode comprar essa dica.')
        else:
          print(f'A próxima letra da Capital é:', f'\033[0,33m {capital[c]}\033[0,0m')
          capital_str += capital[c]
          print(f'Letras obtidas por enquanto: {capital_str}')
          tentativas -= 3
          c+=1
          inventario['Letras da capital: '] = capital_str
          if len(capital)-1 == c:
            del dic_dicas[2]
            del lista_dicas[1]

      elif dica == 3 and dica in  lista_dicas: #dica 3
        print(f'A área do país é: {area}')
        del dic_dicas[3]
        del lista_dicas[2]
        inventario['Área do país: '] = area
        tentativas -= 6

      elif dica == 4 and dica in  lista_dicas: #dica 4
        print(f'{populacao} pessoas.')
        tentativas -= 5
        inventario['População'] = populacao
        del dic_dicas[4]
        del lista_dicas[3]

      elif dica == 5 and dica in  lista_dicas: #dica 5
        print(f'Está no continente: {continente}')
        tentativas -= 7
        inventario['Continente'] = continente
        del dic_dicas[5]
        del lista_dicas[4]

      elif dica == 6: #dica 6
        print('\n\nVoltando ao jogo!\n\n')
      

        
    if jogada == "inventario":
      if inventario == {}:
        print('Seu inventário está vazio.')
      for i in inventario.keys():
        print(f'{i} --> {inventario[i]}')
    
    if jogada in dados:
      distancia = haversine(EARTH_RADIUS, ((dados[jogada])['geo'])['latitude'], ((dados[jogada])['geo'])['longitude'], latitude, longitude)
      dic_distancia[distancia] = jogada
      for i in dic_distancia.keys():
        if i not in lista_distancias:
          lista_distancias.append(i)
      lista_distancias.sort()
      print('Distâncias: ')
      for dista in lista_distancias:
        if dista >= 10000:
          print(cor(166, 43, 237,f'    {dista:.2f} KM --> {dic_distancia[dista]}'))
        elif dista < 10000 and dista >= 5000:
          print(cor(237, 211, 43,f'    {dista:.2f} KM --> {dic_distancia[dista]}'))
        elif dista < 5000 and dista >= 1000:
          print(cor(92, 237, 43,f'    {dista:.2f} KM --> {dic_distancia[dista]}'))
        elif dista < 1000:
          print(cor(41, 240, 193,f'    {dista:.2f} KM --> {dic_distancia[dista]}'))

    
    if tentativas > 10:
      print(f'Tentativas restantes:', f'\033[0;32m {tentativas}\033[0;0m')
    elif tentativas <= 10 and tentativas > 5:
      print(f'Tentativas restantes:', f'\033[0;33m {tentativas}\033[0;0m')
    elif tentativas <= 5:
      print(f'Tentativas restantes:', f'\033[0;31m {tentativas}\033[0;0m')

    if jogada == pais_sorteado:
      print(f'Parabéns! Você adivinhou o país "{pais_sorteado}" em {indice_jogada} tentativas!')
      print('Finalizando jogo...')
      jogar_novamente = False
      tentativas = 0

    
    if jogada == 'desisto':
      desistir = input('Deseja mesmo desistir? [s|n]: ')
      if desistir == 's':
        print('Que feio... Lembre-se de nunca desistir se quiser atingir seus sonhos!\nFinalizando jogo...')
        jogar_novamente = False
        tentativas = 0
      elif desistir == 'n':
        print('Voltando ao jogo...')
    
  

  print('')
  print('Fim de jogo! \n')
  print(f'O país sortedo era {pais_sorteado}!')
  print('')

  pais_sorteado = sorteia_pais(dados)

  jogar_novamente = input('Deseja jogar novamente? [s|n] ')
  if jogar_novamente == 'n':
    jogar_novamente = False
    print('Até a próxima!')
  elif jogar_novamente == 's':
    lista_distancias = []
    lista_dist_colorido = []
    lista_tentativas = []
    lista_dicas = [1,2,3,4,5,6]
    capital_str = ''
    inventario = {}
    dic_distancia = {}
    indice_jogada = 1
    c = 0 
    d = 0
    area = (dados[pais_sorteado])['area']
    populacao = (dados[pais_sorteado])['populacao']
    capital = (dados[pais_sorteado])['capital']
    latitude = ((dados[pais_sorteado])['geo'])['latitude']
    longitude = ((dados[pais_sorteado])['geo'])['longitude']
    bandeira = (dados[pais_sorteado])['bandeira']
    continente = (dados[pais_sorteado])['continente']

  if jogar_novamente != 'n' or jogar_novamente != 's':
    while jogar_novamente != 'n' or jogar_novamente != 's':
      jogar_novamente = input('Escolha uma opção válida [s|n] ')
      if jogar_novamente == 'n':
        jogar_novamente = False
        print('Até a próxima!')
        break
      elif jogar_novamente == 's':
        lista_distancias = []
        lista_dist_colorido = []
        lista_tentativas = []
        lista_dicas = [1,2,3,4,5,6]
        capital_str = ''
        inventario = {}
        dic_distancia = {}
        indice_jogada = 1
        c = 0 
        d = 0
        area = (dados[pais_sorteado])['area']
        populacao = (dados[pais_sorteado])['populacao']
        capital = (dados[pais_sorteado])['capital']
        latitude = ((dados[pais_sorteado])['geo'])['latitude']
        longitude = ((dados[pais_sorteado])['geo'])['longitude']
        bandeira = (dados[pais_sorteado])['bandeira']
        continente = (dados[pais_sorteado])['continente']