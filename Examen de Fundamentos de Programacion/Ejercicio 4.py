def definirsigno_correspondiente():
    #datos de entrada
    
    operacion=int(input("ingrsa 1 es suma, 2 es resta, 3 si es multiplicacion, 4 si es divicion, 5 si es potencia:"))
    dato1=int(input("ingresa el primer valor"))
    dato2=int(input("ingresar el segundo valor"))
    #proceso
    if operacion<2 and operacion>0:
        R=dato1+dato2   
    else:
        operacion<3 and operacion>1
        R=dato1-dato2
    if operacion>2 and operacion<4 :
        R=dato1*dato2
    elif operacion <5 and operacion>3:
        R=dato1/dato2
    if operacion>4 and operacion<6:
        R=dato1**dato2
    print("el resultado  es:", R)
definirsigno_correspondiente()