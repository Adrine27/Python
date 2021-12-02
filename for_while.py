# x = int(input('number'))
# a = x % 10
# b = (x % 100) // 10
# c = (x % 1000) // 100
# d = x // 1000
# y = str(a) + str(b) + str(c) + str(d)
# print(y)

# x = input('number')
# res = x[::-1]
# print(res)

# while True:
# 	mail = input('write your mail ')
# 	ketitex = 0
# 	shnikitex = 0
# 	for i in mail:
# 		if i == '@':
# 			break
# 		shnikitex += 1	
# 	for g in mail:
# 		if g == '.':
# 			break
# 		ketitex += 1
# 	print(shnikitex,ketitex)
# 	if ketitex > shnikitex and shnikitex != 0:
# 		print('good')
# 		break
# 	else:
# 		print('not good')

# while True:
# 	test = input('mail')
# 	x = test.index('@')
# 	y = test.index('.')
# 	if x < y and x != 0:
# 		print('good',test)
# 		break
# 	else:
# 		print('false')

# x = int(input('write a number '))
# y = 0
# for i in str(x):
# 	y += 1
# print(y)
	
# km = 12
# m = km * 1000
# pc_minute = 3
# my_minute = pc_minute*10/100 + pc_minute
# my_second = my_minute * 60
# x = m / my_second
# print(x)

# x = int(input('x = '))
# y = int(input('y = '))
# z = range(1000)
# for i in z:
# 	if i % x == 0 and i % y == 0:
# print(i) 

# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
# 	start = x
# else:
# 	start = y
# end = x * y + 1
# count = 0
# for i in range(start,end,start):
# 	count += 1
# 	if i % x == 0 and i % y == 0:
# 		print(i)
# 		break
# print('count',count)

# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
# 	start = x
# else:
# 	start = y
# count = start
# while True:
# 	if count % x == 0 and count % y == 0:
# 		print(count)
# 		break
# 	else:
# 		count += start

'''1.Write a Python program to find the smallest number which are
divisible by 12 and 15.'''
# x = 12
# y = 15
# start = y
# end = x * y + 1
# for i in range(start,end,start):
# 	if i % x == 0 and i % y == 0:
# 		print(i)
# 		break

'''2.Write a Python program to count the number of even and odd
numbers from a series of numbers(1-100).'''
# x = range(1,100)
# count1 = 0
# count2 = 0
# for i in x:
# 	if i % 2 == 0:
# 		count1 += 1
# 	if i % 2 == 1:
# 		count2 += 1
# print('even numbers:',count1,'\n','odd numbers:',count2)

'''3.Write a Python program to get the Fibonacci series between 0
to 40:
Fib_num = 0,1,1,2,3,5,8 …..'''
# x,y = 0,1
# while y < 40:
# 	print(y,end = '')
# 	x,y = y,x+y
	
'''4.Write a Python program that accepts a string and calculate
the number of digits and letters.
string = ‘python 3.9’'''
# string = 'python 3.9'
# count_letters = 0
# count_digits = 0
# for i in string:
# 	if i.isalpha():
# 		count_letters += 1
# 	if i.isdigit():
# 		count_digits += 1
# print('letters:',count_letters,'\n','digits:',count_digits)


'''5.Write a Python program which have number (73421):
You should calculate (7 + 3 + 4 ….):'''
# x = '73421'
# y = 0
# for i in x:
# 	y += int(i)
# print(y)

'''6.Write a loop to find the factorial of any number. You have one
input.'''
# x = int(input('x = '))
# y = 1
# if x < 0:
# 	print('error')
# elif x == 0:
# 		print('factorial = 1')
# else:
# 	for i in range(y,x+1):
# 		y = y * i
# 	print('factorial =',y)

'''7.Write a python program to compute the greatest
common divisor of two positive integers.
Example:
>>> input 12 8
>>> output 4'''
# x = int(input('x = '))
# y = int(input('y = '))
# i = 1
# while i < x and i < y:
# 	if x % i == 0 and y % i == 0:
# 		gcd = i
# 	i = i + 1
# print('the greatest divisor is:',gcd)


'''8.Write a python program to compute the smallest
number that is divisible by both integer a and b.
Example:
>>> input 14 8
>>> output 2'''
# x = int(input('x = '))
# y = int(input('y = '))
# i = 2
# while i < x and i < y:
# 	if x % i == 0 and y % i == 0:
# 		lcm = i
# 		break
# 	i = i + 1
# print('the smallest divisor is:',lcm)


'''9.Write a python program to check if user age in (18-20) and if
gender is male.'''
# age = int(input('age: '))
# gender = input('male or female: ')
# if age >= 18 and age <= 20 and gender == 'male':
# 	print('True')
# else:
# 	print('False')


'''10.Write a python program to output L with "*"'''
# x = ''
# for row in range(0,7):
# 	for column in range(0,7):
# 		if (column == 1 or (row == 6 and column != 0 and column < 6)):
# 			x = x + '*'
# 		else:
# 			x = x + ' '
# 	x = x + '\n'
# print(x)

'''11.check if the triangle is right calculate the area of triangle, or not check again'''
# while True:
# 	angle1 = int(input('first angle: '))
# 	angle2 = int(input('second angle: '))
# 	if angle1 + angle2 == 90:
# 		print("yes it's a right triangle")
# 		x = int(input('x = '))
# 		y = int(input('y = '))
# 		S = x * y / 2
# 		print('S =',S)
# 		break
# 	else:
# 		print("it's a not right triangle,try again")
# 		continue