number=[1,2,3,4,5,6,7,8,9,10]
number_par=[num for num in number if num %2==0]
number_inpar=[num for num in number if num%2 == 1]
print(number_par)
print(number_inpar)