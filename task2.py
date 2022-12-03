#2) Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
#Пример:
#Для n = 15: Ответ: 3
#Для n = 35: Ответ: 5

number = int(input('Enter a number: '))
for i in range(2, number + 1): 
    if number % i == 0: 
        print(f'The smallest natural divisor for {number} is {i}')
        break


