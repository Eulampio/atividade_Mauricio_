while True:
    print(" Digite 1 para ADIÇÃa")
    print(" Digite 2 para SUBTRAÇÃO")
    print(" Digite 3 para DIVISÃO")
    print(" Digite 4 para MULTIPLICAÇÃO")

    x=float(input(" Digite a opção:  "))
    if x<=0 or x>=5:
        print("opção invalida")
    
    elif x==1 or x==1:
        import Soma
    elif x==2:
       import Subtração
    elif x==3:
       import Divisão
    elif x==4:
       import Multiplicacao
    elif x==0:
        print('calculadora encerrada')
        break
