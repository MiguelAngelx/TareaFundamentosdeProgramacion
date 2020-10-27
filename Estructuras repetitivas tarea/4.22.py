def calcularsaldoclienteMAQC():
    ganacia_por_intereses = 0
    n = int (input ('Ingrese el valor de n: '))
    for i in range (1, n + 1):
        print ('PROCESO ' + repr (i))
        compras_realizadas = float (input ('Ingrese el valor de compras realizadas: '))
        pago_del_corte_anterior = float (input ('Ingrese el valor de pago del corte anterior: '))
        saldo_anterior = float (input ('Ingrese el valor de saldo anterior: '))
        if saldo_anterior*0.15>pago_del_corte_anterior:
            intereses=saldo_anterior*0.12
            multa=200
        else:
            intereses=0
            multa=0
        saldo_actual=saldo_anterior+compras_realizadas-pago_del_corte_anterior+intereses+multa
        pago_minimo=saldo_actual*0.15
        pago_para_no_generar_intereses=saldo_actual*0.85
        ganacia_por_intereses=ganacia_por_intereses+intereses
        print ('Valor de intereses: ' + repr (intereses))
        print ('Valor de multa: ' + repr (multa))
        print ('Valor de pago minimo: ' + repr (pago_minimo))
        print ('Valor de pago para no generar intereses: ' + repr (pago_para_no_generar_intereses))
        print ('Valor de saldo actual: ' + repr (saldo_actual))
    print ('Valor de ganacia por intereses: ' + repr (ganacia_por_intereses))
calcularsaldoclienteMAQC()