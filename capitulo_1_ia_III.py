mapa_robo ={

    [0,0,0],
    [0,1,0],
    [0,0,0]
}
posicao_robo = [1,1] # linha, coluna
# 0 = sujo
# 1 = limpo
def mover_robo(direcao):
    for i in range(len(mapa_robo)):
        for j in range(len(mapa_robo[i])):
            if mapa_robo[i][j] == 0:
                if direcao == mapa_robo[i-1][j] and i > 0:
                    posicao_robo[0] -= 1
                    mapa_robo[i][j] = 1
                elif direcao == mapa_robo[i+1][j] and i < len(mapa_robo)-1:
                    posicao_robo[0] += 1
                    mapa_robo[i][j] = 1
                elif direcao == mapa_robo[i][j-1] and j > 0:
                    posicao_robo[1] -= 1
                    mapa_robo[i][j] = 1
                elif direcao == mapa_robo[i][j+1] and j > len(mapa_robo[i])-1:
                    posicao_robo[1] -= 1
                    mapa_robo[i][j] = 1
                else:
                    print("Movimento inválido")
    return posicao_robo

print(mover_robo(0))
print(posicao_robo)
print(mapa_robo)
