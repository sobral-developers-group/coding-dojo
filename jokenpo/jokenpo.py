def Jokenpo(jogada1, jogada2):
    if jogada1==jogada2:
        return "Empate"
    if jogada1=="Papel":
        if jogada2=="Pedra":
            return "Papel"
        else:
            return "Tesoura"
    elif jogada1=='Tesoura':
        if jogada2=='Papel':
            return'Tesoura'
        else:
            return 'Pedra'
    elif jogada1=='Pedra':
        if jogada2=='Tesoura':
            return 'Pedra'
        else:
            return 'Papel'

