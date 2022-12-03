#1) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def Factorial(number):
    if number < 0:
        print("Sorry, factorial does not exist for negative numbers")
    if number == 1 or 0: 
        return 1
    if number > 1:
        return Factorial(number - 1) * number

number = int(input("Enter a number: "))
numbers = [Factorial(x) for x in range(1, number + 1)]
print (numbers)
