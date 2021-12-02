'''1. Write code to print pypypypython'''
# print('py' * 4 + 'thon')

'''2. Write code to print 7p7p7p79'''
# print('7p' * 3 + '79')

'''3. Write code to print 9999999'''
# print('9' * 7)

'''4. Write a Python program that checks how much money you have on your card. 
At first, your balance is 0, and you have 3 inputs and add each of them to the 
card.'''
# balance = 0
# money1 = int(input('first money '))
# money2 = int(input('second money '))
# money3 = int(input('third money '))
# balance += money1
# balance -= money2
# balance += money3
# print('in your card you have ', balance, 'dram')

'''5. Create 7 legal variables and check type of them.'''  
# name1 = int(input('x = '))
# print(type(name1))

# name_2 = 4.6
# print(type(name_2))

# NAME3 = 'text'
# print(type(NAME3))

# Name_4 = False
# print(type(Name_4))

# _name_5 = -45
# print(type(_name_5))

# NAME_6 = True
# print(type(NAME_6))

# _Name_7_ = 'text 2'
# print(type(_Name_7_))

'''6. Create 10 variables integer and float and compare this variables'''
# x = int(input('x = '))
# y = float(input('y = '))
# print(x > y)

# x = 8
# y = 9.6
# print(x == y)

# x = int(input('x = '))
# y = float(input('y = '))
# print(x <= y)

# x = float(input('x = '))
# y = int(input('y = '))
# print(x >= y)

# x = float(input('x = '))
# y = float(input('y = '))
# print(x != y)

# x = 8.6
# y = -9.4
# print(x < y)

# x = int(input('x = '))
# y = int(input('y = '))
# c = x % y
# print(c > y)

# x = float(input('x = '))
# y = float(input('y = '))
# x +=y	
# print(x >= 0)

# x = int(input('x = '))
# y = float(input('y = '))
# c = x // y
# print(c <= x)

# x = 3.65
# y = -5.61
# c = x * y
# print(c > y)

'''7.Create a python program which convert the pound in 
kilograms.'''
# pound = float(input('pound = '))
# kg = pound / 2.2
# print('kg = ', kg)

'''8. Create a python program which convert the miles in 
kilometers.'''
# mile = float(input('mile = '))
# km = 1.6 * mile
# print('km = ', km)

'''9. Create a python program to find the Square Root'''
# x = float(input('x = '))
# y = x ** 0.5
# print(y)

'''10.Write a python program which have two input(initial price and final price),count how much percentage discounted the product'''
# price1 = int(input('first price = '))
# price2 = int(input('second price = '))
# x = price2 * 100 / price1
# y = 100 - x
# print('discount =',y,'%')

'''11.Write a python program which have 2 input(int or float),you have 2 concentric circles(first circle's radius - R, second circle's radius - r, R > r) 
count the area crossing of circles'''
# R = float(input('R = '))
# r = float(input('r = '))
# s = 3.14 * R **2 - 3.14 * r ** 2 
# print('s = ',s)

'''12.Create a python program which convert km / h in m / s.'''
# x = int(input('km/h = '))
# y = x * 1000 / 3600
# print('m/s = ',y)

'''13.Write a python program that has 2 input sizes in meters (float or.int) 
and it calculates how many tiles are needed on the floor of the room. The area of 1 tile is 50 * 50 cm'''
# x = int(input('side 1 = '))
# y = int(input('side 2 = '))
# s = x * y * 100 * 100
# tile1 = 50 * 50
# tiles = s / tile1
# print(tiles,'tiles')