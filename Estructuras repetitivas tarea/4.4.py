def contabilizarfocosMAQC():
    focosverdes = 0
    focosblancos = 0
    focosrojos = 0
    n = int (input ('Ingrese el valor de n: '))
    for i in range (1, n + 1):
        print ('PROCESO ' +  (i))
        print ('Seleccione el valor de color.')
        print ("1.- verde")
        print ("2.- blanco")
        print ("3.- rojo")
        color = 0
        while color<1 or color>3:
            color = int (input (': '))
        if color==1:
            focosverdes=focosverdes+1
        if color==2:
            focosblancos=focosblancos+1
        if color==3:
            focosrojos=focosrojos+1
        print ()
    print ('Valor de focos verdes: ' +  (focosverdes))
    print ('Valor de focos blancos: ' +  (focosblancos))
    print ('Valor de focos rojos: ' +  (focosrojos))
contabilizarfocosMAQC()