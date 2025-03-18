palabra_1=input('ingresa la primera palabra:')
palabra_2=input('ingresa la segunda palabra:')
if sorted(palabra_1.lower()) == sorted(palabra_2.lower()):
    print('son anagramas')
else:
    print('no son anagramas')