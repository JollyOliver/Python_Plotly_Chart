# -*- coding: utf-8 -*-
import plotly.express as px
import numpy as np
import pandas as pd
a = 3 #número RU 1
b = 3 #número RU 2
c = 3 #número RU 3
contador = 0
x = [] #variável em lista para receber os números definidos pelo usuário
y = [] #variável em lista para receber os resultados da equação
print('=' * 70)
while True:
  contador = contador + 1
  try:
    x.append(int(input('Defina X [{} de 10]: ' .format(contador)))) #pede os números ao usuário e os coloca na lista um após o outro
  except ValueError:
    x.remove #remove o último input recebido para evitar erros nas equações em caso de value error
    contador = contador - 1
    print('Apenas Use Números Inteiros [Ex. 10, -8, 20, 7]')
    continue #repete o input até receber um valor válido
  if contador == 10:
    print('=' * 70)
    print('Os 10 Valores de Y São Definidos a Partir da Seguinte Equação: y = 3 * x + 3 * x - 3')
    print('Valores de X: ' , x)
    break
#realiza as equações para os valores de y usando as variáveis a-b-c e os números da lista x do 1 ao 10 (posições 0 a 9)
y.append((a * x[0]) + (b * x[0]) - c)
y.append((a * x[1]) + (b * x[1]) - c)
y.append((a * x[2]) + (b * x[2]) - c)
y.append((a * x[3]) + (b * x[3]) - c)
y.append((a * x[4]) + (b * x[4]) - c)
y.append((a * x[5]) + (b * x[5]) - c)
y.append((a * x[6]) + (b * x[6]) - c)
y.append((a * x[7]) + (b * x[7]) - c)
y.append((a * x[8]) + (b * x[8]) - c)
y.append((a * x[9]) + (b * x[9]) - c)
print('Valores de Y: ' , y)
print('=' * 70)
fig = px.line(x = x, y = y,
              labels = {"x": "X AXIS", "y": "Y AXIS"}) #define como X e Y serão legendados no gráfico
fig.add_scatter(x = x, y = y,
                mode = 'markers',
                hoverinfo = 'skip',
                marker_color = '#3CB371',
                name = 'Par de X e Y',
                marker_size = 15) #configura as definições visuais dos marcadores
fig.update_layout(title = 'Plano Cartesiano de Pontos X e Y',
                  plot_bgcolor ='#8FBC8F',
                  showlegend = True,
                  width = 1400,
                  height = 700) #configura as definições visuais do gráfico
fig.show() #exibe o gráfico formado
