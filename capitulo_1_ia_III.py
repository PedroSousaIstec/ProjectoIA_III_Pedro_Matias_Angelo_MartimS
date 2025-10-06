mapa_robo =[

    [0,0,0],
    [0,1,0],
    [0,0,0]
]
posicao_robo = [1,1] #posição inicial
# 0 = sujo
# 1 = limpo
def mover_robo():
    for i in range(len(mapa_robo)):
        for j in range(len(mapa_robo[i])):
          if mapa_robo[i][j] == 0:
            mapa_robo[i][j] = 1
            
            
mover_robo()
posicao_robo
for linha in mapa_robo:
    print(linha)
