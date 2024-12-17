# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):
        # VERIFICANDO SE HOUVE CAMPEÃO NAS LINHAS
        for i in range(0, 3):
            if self.matriz[i][0] == self.matriz[i][1]:
                if self.matriz[i][1] == self.matriz[i][2]:
                    return self.matriz[i][2]
                
        # VERIFICANDO SE HOUVE CAMPEÃO NAS COLUNAS
        for j in range(0, 3):
            if self.matriz[0][j] == self.matriz[1][j]:
                if self.matriz[1][j] == self.matriz[2][j]:
                    return self.matriz[2][j]
            
        # VERIFICANDO SE HOUVE CAMPEÃO NA DIAGONAL PRINCIPAL
        if self.matriz[0][0] == self.matriz[1][1]:
            if self.matriz[1][1] == self.matriz[2][2]:
                return self.matriz[2][2]
            
        # VERIFICANDO SE HOUVE CAMPEÃO NA DIAGONAL SECUNDÁRIA
        if self.matriz[2][0] == self.matriz[1][1]:
            if self.matriz[1][1] == self.matriz[0][2]:
                return self.matriz[0][2]

        return Tabuleiro.DESCONHECIDO