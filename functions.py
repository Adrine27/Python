'''1.Write a python function to 
create a simple Calculator.'''

# def sum_(x,y):
# 	return x + y
# def subtract_(x,y):
# 	return x - y
# def multiply_(x,y):
# 	return x * y  
# def devide_(x,y):
# 	return x / y
# print('Select the action')
# while True:
# 	sel = int(input('sum(1),subtract(2),multiply(3),devide(4)'))
# 	if sel in (1,2,3,4):
# 		x = float(input('x = '))
# 		y = float(input('y = '))
# 		if sel == 1:
# 			print(x,'+',y,'=',sum_(x,y))
# 		elif sel == 2:
# 			print(x,'-',y,'=',subtract_(x,y))
# 		elif sel == 3:
# 			print(x,'*',y,'=',multiply_(x,y))
# 		else:
# 			print(x,'/',y,'=',devide_(x,y))
# 		cont = input('continue?(y or n) ')
# 		if cont == 'y':
# 			continue
# 		else:
# 			break


'''2.Write a python function 
to find max of two numbers.'''
# def numbers(x,y):
# 	if x > y: 
# 		return x
# 	else:
# 		return y
# x = float(input('x = '))
# y = float(input('y = '))
# print(numbers(x,y))


'''3.Write a python function
to sum all numbers.'''
# def sum(numbers):
# 	sum_ = 0
# 	for i in list_:
# 		sum_ += i
# 	return sum_
# list_ = [1,2,3,4,5]
# print(sum(list_))

'''4.Write a python function
to multiply all numbers.'''
# def multiply(numbers):
# 	res = 1
# 	for i in list_:
# 		res *= i
# 	return(res)
# list_ = [1,2,3,4,5]
# print(multiply(list_))

'''5.Write a python program
 to sum all letter and 
number in your string.'''
# def sum(numlet):
# 	res1 = 0
# 	res2 = 0
# 	for i in word:
# 		if i.isalpha():
# 			res2 += 1
# 		if i.isdigit():
# 			res1 += int(i)
# 	print('sum of numbers:',res1,'\ncount of letters:',res2)
# word = input('write a word(lestters and numbers): ')
# sum(word)

'''6.You are given a program that takes all 3 
passengers ages as inputs and inserts them in 
a list. Complete the program so that if it 
finds a value less than 16, it breaks the 
loop and outputs "Too young! ".
If the age requirement is satisfied, the 
program outputs "Get ready!".'''
# def passengers(ages):
# 	for i in list_:
# 		if i < 16:
# 			print('Too young')
# 			break
# 		else:
# 			print('Get ready!')
# 			break
# age1 = int(input('age1: '))
# age2 = int(input('age2: '))
# age3 = int(input('age3: '))
# list_ = []
# list_.extend([age1,age2,age3])
# passengers(list_)


'''7. km to mile
Write a python function which
conversion kilometer to miles.'''
# def num(km):
#   mile = km * 0.6
#   return mile
# km = int(input('km: '))
# print(num(km))


'''8. Time
Write a python function which
conversion days to seconds.'''
# def day(x):
#   return 24*60*60*x
# print(day(5))


'''9. Password
Write a python function which
generate a valid password.'''
# import random
# def password(x,y):
#   z = x + y 
#   return z
# i = 0
# while i < 3:
#   x = random.randint(1,10)
#   y = random.choice('qwertyuiopasdfghjklzxcvbnm')
#   x = str(x)
#   i += 1
#   print(password(x,y))


'''10. Factorial'''
# def fac(num):
#   res = 1
#   if num < 0:
#       print('Error.Write a positive number')

#   else:
#       for i in range(1,num + 1):
#           res *= i
#       print(res)
# num = int(input('number: '))
# fac(num)


'''11. Max
Given an list of numbers.
Find the maximum element in 
list.Without use max function.'''
# def max_(number):
#   res = number[0]
#   for i in number:
#       if res < i:
#           res = i
#   return res
# numbers = [1,2,5,6,4]
# print(max_(numbers))


'''12. Ip
Write a Python program which 
will remove all zeros from an 
IP address.
ip = "216.008.094.196"'''
# def func(ip):
#       ip = ip.replace('0','')
#       return ip
# ip = '216.008.094.196'
# print(func(ip))


'''13. Tennis
Imagine you and the computer are playing tennis. 
write a program where you have a sheet where victory 
points are kept and you need to figure out who is the 
winner.A set is won by the first side to win 6 games.
You should to show the result of the match. If game
win you in list add “a” if pc “b”.
results=['b','a','a','a','a','a','a','a','a','a','a','a','b','b','b','b','b','b','a
','a','a','a', 'a','b','b','b','b','b',
'a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']'''

# results = ['b','a','a','a','a','a','a','a','a','a','a','a','b','b','b','b','b','b','a','a','a',
# 'a','a','b','b','b','b','b','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a',]
# def func(result):
#   comp = 0
#   user = 0
#   comp_point = 0
#   user_point = 0
#   for i in results:
#       if i == 'b':
#           comp += 1
#       elif i =='a':
#           user += 1
#       if user >= 6 and user - comp >=2:
#           user_point += 1
#           comp = 0
#           user = 0
#       elif comp >= 6 and comp - user >=2:
#           comp_point += 1
#           comp = 0
#           user = 0
#   print(comp_point,user_point)
# func(results)