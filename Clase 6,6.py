print('la Sumatoria de (1/a)**i')
a= int(input('donde a es: '))
i= int(input('y donde i es: '))
r=0
x=1
while x<=i:
    r+= (1/a)**x
    x+=1
print(f'Es mas o menos {r}')