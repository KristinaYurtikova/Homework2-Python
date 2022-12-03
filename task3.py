#3) Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
#Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
#Ввод: 4
#[-4, -3, -2, -1, 0, 1, 2, 3,4]

def MultiplyElementsOnDefinedIndices(array,indices):
    result = 1
    for x in indices:
        result *= array[x]
    return result

number = int(input('Enter a number: '))
range = [n for n in range(-number, number + 1)]
print(range)
number = map(int,input('Put through a space indices on which to multiply elements: ').split())
print(MultiplyElementsOnDefinedIndices(range,number))