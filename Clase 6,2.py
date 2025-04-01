Numb_Notes = int(input('Ingresar numero de notas: '))
X = 0
R = 0
while X < Numb_Notes:
    N=float(input(f'Nota Numb {X+1}'))
    if N < 0 or N > 5:
        print('Nota no valida, ingrese un valor Valido')
        continue
    else:
        R += N
        X += 1
print(f'Su nota Final es {R/Numb_Notes}')
