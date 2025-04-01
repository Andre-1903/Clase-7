while 1==1:
    fact = int(input('ingresar un numero entre 0 y 20: '))
    if fact>20 or fact<0:
        print('numero no valido')
        continue
    else:
        fl=1
        X=1
        while X<=fact:
            fl *=X
            X +=1
    print(fl)