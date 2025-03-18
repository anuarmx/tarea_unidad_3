a=0
b=1
num= int(input('ingresa el limite de la serie:'))
for _ in range(num):
    c= a + b
    a=b
    b= c
    print(c)