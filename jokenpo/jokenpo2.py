def Jokenpo(jogada1, jogada2):
   if jogada1==jogada2:
       return "Empate"
   if jogada1=="Pedra" or jogada2=="Pedra":
       if jogada1=="Tesoura" or jogada2=="Tesoura":
           return "Pedra"
       else:
           return "Papel"
   else:
       return "Tesoura"
