fibonacci_list = [1,1]
sum_even_numbers = 0
even_numbers_list = []

while fibonacci_list[-1] + fibonacci_list[-2] <= 10000000:
    if fibonacci_list[-1]%2 == 0:
        sum_even_numbers += fibonacci_list[-1]
        even_numbers_list.append(fibonacci_list[-1])
    fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])


print(f'Последовательность Фибоначчи: {fibonacci_list}\n')
print(f'Количество элементов в последовательности: {len(fibonacci_list)}\n')    
print(f'Cумму всех четных элементов: {sum_even_numbers}\n')
print(f'Все четные элементы: {even_numbers_list}\n')
print(f'Предпоследнее число последовательности: {fibonacci_list[-2]}\n')