#4)Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

def SumEven(array):
    sum = 0
    for n in array:
        if n % 2 == 0:
            sum += n
    return sum

number = int(input('Enter a number: '))
print(SumEven(range(number + 1)))