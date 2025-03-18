num=int(input('ingresa el numero:'))
for i in range(2,num):
    if num%i==0:
        print('no es primo')
        break
else:
    print('es primo')