import random as rd
from math import *

def cor(r, g, b, texto):
    return f"\033[38;2;{r};{g};{b}m{texto}\033[38;2;255;255;255m"

def haversine(raio, lat1, lon1, lat2, lon2):
  lat1 = radians(lat1)
  lon1 = radians(lon1)
  lat2 = radians(lat2)
  lon2 = radians(lon2)
  senlat = sin((lat2 - lat1)/2)
  coslat1 = cos(lat1)
  coslat2 = cos(lat2)
  mcoslat = coslat1*coslat2
  senlon = sin((lon2 - lon1)/2)
  cont_r = (senlat**2) + (mcoslat*(senlon**2))
  raiz = sqrt(cont_r)
  asin_r = asin(raiz)
  d = 2 * raio * asin_r
  return d

def normaliza(dic):
    d = {}
    for i in dic:
        for pais in dic[i]:
            d[pais] = dic[i][pais]
            d[pais]['continente'] = i
    return d

def sorteia_pais(dict):
    pais = rd.choice(list(dict))
    return pais

def cor_predominante(dic):
    i = 0
    corp = ''
    for cor in dic.items():
        if dic[cor] > i:
            i = dic[cor]
            corp = cor
    return corp




