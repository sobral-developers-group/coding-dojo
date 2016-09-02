def converte_Romanos (x):
    if x>=1 and x<5:
        return "I"+converte_Romanos(x-1)
    elif x>=5 and x<9:
        return "V" + converte_Romanos(x%5)
    elif x>=10 and x<50:
        return "X"+converte_Romanos(x-10)
    elif x>=50 and x<90:
        return "L"+converte_Romanos(x%50)
    elif x>=100 and x<500:
        return "C"+converte_Romanos(x-100)
    elif x>=500 and x<900:
        return "D"+converte_Romanos(x-500)
    elif x>=1000 and x<5000:
        return "M"+converte_Romanos(x-1000)
    else:
        return ""
