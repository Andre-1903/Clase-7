N= int(input('impar final: '))
R=0
I=1 
while ((2*I)-1) <= N:
        R+=((2*I)-1)
        I+=1
print(f'EL resultado de la suma de los numeros impares hasta {N} es igual a {R}')
