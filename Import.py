'''1. Write a python program which will check is your number equal the random 
number of computer (1-10)if yes print True otherwise False.'''
# import random
# x = int(input('x = '))
# y = random.randint(1,10)
# print('y =',y)
# c = x == y
# print(c)

'''2. Write a python program which will check is your number great or equal 
the random number of computer (10-100)if yes print True otherwise False.'''
# import random
# x = int(input('x = '))
# y = random.randint(10,100)
# print('y =',y)
# c = x >= y
# print(c)

'''3. Write a python program which will show your birthday using calendar.'''
# import calendar
# x = int(input('year = '))
# y = int(input('month = '))
# print(calendar.month(x,y))

'''4. Write a python program where we use sqrt (definition discriminant)
D = b^2 - 4ac, x = (-b +- sqrt(D))/2a, 6x^2 + 10x - 1 = 0'''
# import math
# a = 6
# b = 10
# c = -1
# D = math.pow(b,2) - 4 * a * c
# x1 = (-b + math.sqrt(D))/(2 * a)
# x2 = (-b - math.sqrt(D))/(2 * a)
# print('D =',D,'\nX1 =',x1,'\nX2 =',x2)

'''5. Write a python program where we use pi (calculate the area of circle) 
you have one input (radius circle).'''
# from math import *
# r = float(input('r = '))
# s = pi*pow(r,2)
# print('pi =',pi,'\ns =',s)


'''6.You have one input and one random(1-100),count how many 6 are in number and than divide the numbers,
than ceil the answer and print factorial 
EXAMPLE
our number is 645686
random number is 8
666/8 = 83.25 = 84
84! = ...'''
# from math import *
# import random
# x = input(' x = ')
# y = x.count('6')
# z = y * '6'
# a = random.randint(1,100)
# b = int(z) / a
# c = ceil(b)
# print('','number is',z,'\n','random number is',a,'\n','z/a =',c,'\n','factorial =',factorial(c))
