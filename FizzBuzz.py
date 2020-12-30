#Задача FizzBuzz
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print ('FizzBuzz')
    elif i%3 == 0:
        print ('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)


#Сумма чисел из диапазона от 1000 до 20000 включительно, 
#которые делятся и на 3 и на 5.
sum = 0
for i in range(1000, 20001):
    if i%3==0 and i%5==0:
        sum+=i
print(sum)
