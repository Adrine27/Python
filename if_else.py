'''1. Write a Python program to calculate a dog'sage in human years.
Note: For the first two years, a dog year
is equal to 10.5 human years. After that,
each dog year equals 4 human years'''
# dog = int(input('dog age = '))
# human = ''
# if dog < 0:
# 	print('wrong')
# elif dog >= 0 and dog <= 2:
# 	human = dog * 5.25
# else:
# 	human = 10.5 + (dog - 2) * 4
# print('human age =',human)

'''2. Write a Python program to check
whether an alphabet is a vowel or
consonant'''
# letter = input('letter ')
# vowel = 'aeiouy'
# if letter in vowel:
# 	print('yes')
# else:
# 	print('no')

'''3. Write a Python program to check this
year is leap year or no'''
# year = int(input('year:'))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
# 	print('it is a leap year')
# else:
# 	print('it is not a leap year')

'''4. Write a Python program to check if
your number is odd or even.'''
# x = int(input('x = '))
# if x % 2 != 0:
# 	print("it's a odd number")
# else:
# 	print("it's a even number")

'''5. Write a python program which will say who
win in game.
The winner is the one which have 2 point.
You should try to find pc number(0-5):
if find (your point +=1) otherwise (pc point +=1):'''
# import random
# x = int(input('my number(0-5) = '))
# y = random.randint(0,5)
# print('pc number =',y)
# pc = 0
# me = 0
# if x == y:
# 	me += 1
# 	print('pc point:',pc,'my point:',me)
# else:
# 	pc += 1
# 	print('pc point:',pc,'my point:',me)
# x = int(input('my number(0-5) = '))
# y = random.randint(0,5)
# print('pc number =',y)
# if x == y:
# 	me += 1
# 	print('pc point:',pc,'my point:',me)
# else:
# 	pc += 1
# 	print('pc point:',pc,'my point:',me)
# if me > pc:
# 	print('you win')
# elif me < pc:
# 	print('you lose')
# else:
# 	print('no one')

'''6. Write a python program to Check if a 
Number is Positive, Negative or 0.'''
# x = int(input('x = '))
# if x > 0:
# 	print("it's a positive")
# elif x < 0:
# 	print("it's a negative")
# else:
# 	print("it's 0")


'''7.Take two int values from user and print greatest among them.'''
# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
# 	print('x is greatest')
# else:	
# 	print('y is greatest') 

'''8.Take input of age of 3 people by user and determine oldest 
and youngest among them.'''
# age1 = int(input('first age: '))
# age2 = int(input('second age: '))
# age3 = int(input('third age: '))
# if age2 < age1 > age3:
# 	print('first is oldest ')
# elif age1 < age2 > age3:
# 	print('second is oldest')
# elif age1 < age3 > age2:
# 	print('third is oldest')
# if age2 > age1 < age3:
# 	print('first is youngest')
# elif age1 > age2 < age3:
# 	print('second is youngest')
# elif age1 > age3 < age2:
# 	print('third is youngest')


'''9.You have number. Write a python program which to print a 
new number with digits reversed as of original one. 
For example:
INPUT : 1234 OUTPUT : 4321
INPUT : 5982 OUTPUT : 2895'''
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

'''10.Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using 
following rules print their place of service.
if employee is female, then she will work only in urban areas.
if employee is a male and age is in between 20 to 40 then he may work in 
anywhere
if employee is male and age is in between 40 t0 60 then he will work in urban 
areas only.
And any other input of age should print "ERROR".'''
# age = int(input('age: '))
# gender = input('M or F: ')
# marital_status = input('Y or N: ')
# if gender == 'F' and marital_status == 'Y':
# 	print('you can work only in urban areas.')
# elif gender == 'M' and 20 <= age <= 40 and marital_status == 'N':
# 	print('you can work in anywere ')
# elif gender == 'M' and 40 <= age <= 60 and marital_status == 'Y':
# 	print('you can work in urban areas only')
# elif age < 20 and age > 60:
# 	print('ERROR')

'''11.Rock, Paper, Scissors'''
# import random
# user = input('R(Rock),P(Paper) or S(Scissors) ')
# pc = random.choice(['R','P','S'])
# print('pc choice:',pc)
# if user == pc:
# 	print('No one')
# elif (user == 'R' and pc == 'S') or (user == 'S' and pc == 'R') or (user == 'P' and pc == 'R'):
# 	print('You win')
# elif (user == 'R' and pc == 'P') or (user == 'S' and pc == 'R') or (user == 'P' and pc == 'S'):
# 	print('You lose')

'''12.You (input) and pc have followers (pc have 
random followers) if your followers
is great 20 % than pc you are blogger otherwise 
pc is blogger.'''
# import random
# my_followers = int(input('my followers: '))
# pc_followers = random.randint(0,100)
# print('pc followers:',pc_followers)
# x = pc_followers * 20 / 100 + pc_followers
# if my_followers >= x:
# 	print('You are blogger')
# else:
# 	print('PC is blogger')

'''13.You and the Pc take part in the rally, You must 
pass 12 km. PC passed in 3 minutes and You are 
10% later than Pc. how much is the speed of 
your car.'''
# km = 12
# m = km * 1000
# pc_minute = 3
# my_minute = pc_minute*10/100 + pc_minute
# my_second = my_minute * 60
# x = m / my_second
# print(x)

'''14.The given number is of one digited or two digited or 
three digited or more than three digited.
input >> 176
output >> 3 Digit'''
# x = int(input('write a number '))
# y = 0
# for i in str(x):
# 	y += 1
# print(y)

'''15.The given character is an uppercase letter or 
lowercase letter or a digit or a special character.
Use ord().
input >> @
output >> @ - Special character'''
# x = input('write letter or number or special character: ')
# if x.isupper():
# 	print("it's uppercase letter")
# elif x.islower():
# 	print("it's lowercase letter")
# elif x.isdigit():
# 	print("it's a number")
# else:
# 	print("it's a special character")


'''16.Dice'''
# import random
# while True:
# 	x = random.randint(1,6)
# 	print('The number of dice is:',x)
# 	if x == 1:
# 		print('.')
# 	if x == 2:
# 		print('..')
# 	if x == 3:
# 		print('...')
# 	if x == 4:
# 		print('..''\n''..')
# 	if x == 5:
# 		print('. .''\n'' .''\n''. .')
# 	if x == 6:
# 		print('...''\n''...')
# 	y = input('Do you want to continue the game?(Y or N) ')
# 	if y == 'Y':
# 		continue
# 	else:
# 		print('The game is over')
# 		break

'''17.Write a python program to output this
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
# x = 5
# for i in range(x):
# 	for g in range(i):
# 		print('* ', end = '')
# 	print('')

# for i in range(x,0,-1):
#     for g in range(i):
#         print('* ', end = '')
#     print('')