def totalcajaregistradora():
    billetes_de_100 = int (input ('Ingrese el valor de billetes de 100: '))
    billetes_de_1000 = int (input ('Ingrese el valor de billetes de 1000: '))
    billetes_de_20 = int (input ('Ingrese el valor de billetes de 20: '))
    billetes_de_200 = int (input ('Ingrese el valor de billetes de 200: '))
    billetes_de_50 = int (input ('Ingrese el valor de billetes de 50: '))
    billetes_de_500 = int (input ('Ingrese el valor de billetes de 500: '))
    monedas_de_1 = int (input ('Ingrese el valor de monedas de 1: '))
    monedas_de_10 = int (input ('Ingrese el valor de monedas de 10: '))
    monedas_de_2 = int (input ('Ingrese el valor de monedas de 2: '))
    monedas_de_20 = int (input ('Ingrese el valor de monedas de 20: '))
    monedas_de_5 = int (input ('Ingrese el valor de monedas de 5: '))
    total=billetes_de_1000*1000+billetes_de_500*500+billetes_de_200*200+billetes_de_100*100+billetes_de_50*50+billetes_de_20*20+monedas_de_20*20+monedas_de_10*10+monedas_de_5*5+monedas_de_2*2+monedas_de_1
    print ('Valor de total: ' + repr (total))
totalcajaregistradora()