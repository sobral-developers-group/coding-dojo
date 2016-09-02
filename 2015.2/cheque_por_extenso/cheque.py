def cheque_extenso(valor):

    unidades = {    1.00:"um",
                    2.00:"dois",
                    3.00:"três",
                    4.00:"quatro",
                    5.00:"cinco",
                    6.00:"seis",
                    7.00:"sete",
                    8.00:"oito",
                    9.00:"nove",
                    11.00:"onze",
                    12.00:"doze",
                    13.00:"treze",
                    14.00:"quatorze",
                    15.00:"quinze",
                    16.00:"dezesseis",
                    17.00:"dezessete",
                    18.00:"dezoito",
                    19.00:"dezenove"
                }

    dezenas = {
                    10.00:"dez",
                    20.00:"vinte",
                    30.00:"trinta",
                    40.00:"quarenta",
                    50.00:"cinquenta",
                    60.00:"sessenta",
                    70.00:"setenta",
                    80.00:"oitenta",
                    90.00:"noventa",
                    100.00: "cem"
                    }

    centenas = {
                    200.00: "duzentos",
                    300.00: "trezentos",
                    500.00: "quinhentos"
                  }

    conc="reais"

    if (valor == 1.00):
        conc = "real"
    if (valor in unidades):
        return unidades[valor] + " " + conc
    elif(valor in dezenas):
        return dezenas[valor] + " " + conc
    elif (valor in centenas):
        return centenas[valor]+ " " + conc
    elif (valor==400 or (valor>=600 and valor<=900)):
        return unidades[valor/100] +"centos"+" "+conc
    elif(valor<=99):
        valor_mod_10 = valor%10
        return dezenas[(valor) - valor_mod_10]+" e "+unidades[valor_mod_10]+" "+conc
    else:
        parte_centenaria = int(valor/100)*100
        if(parte_centenaria==100):
            return cheque_extenso(parte_centenaria).replace("cem reais","cento ")+\
            "e "+cheque_extenso(valor-parte_centenaria).replace("real","reais")
        else:
            return cheque_extenso(parte_centenaria).replace("reais","")+\
            "e "+cheque_extenso(valor-parte_centenaria).replace("real","reais")
