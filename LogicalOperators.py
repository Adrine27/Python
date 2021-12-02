'''1. Write a python program to check have your name ‘a’ or no.You have 2 input.'''
# name = input('name ')
# letter = input('letter ')
# res = letter in name
# print(res)

'''2. Write a python program to check if there 
are bananas, oranges and apples in your 
fridge'''
# fruit = input('fruit ')
# fruits = 'banana, orange, apple'
# res = fruit in fruits
# print(res)

'''3. Given a number x. Check following conditions: 
 x is less or equal to -8 or x is greater than 12
 x is greater than 10 and is less or equal to 50
 x is greater than -10 and is less than 10 
 x isn’t equal to 20 or x is greater than 50
 Print the results (they should be True or False)'''
# x = int(input('x = '))
# a = x <= -8 or x > 12
# b = x > 10 and x <= 50
# c = x > -10 and x < 10
# d = x != 20 or x > 50
# print(a,b,c,d)

'''4. Write a python program to check if there 
are bananas, oranges and apples in your 
fridge, and if you don’t have one of them you 
should go buy this , and check have you at 
home light if not, take those items out of the 
fridge'''
# banana = input('banana(yes or no) ').lower() == 'yes'
# orange = input('orange(yes or no) ').lower() == 'yes'
# apple = input('apple(yes or no) ').lower() == 'yes'
# x = banana and not light 
# print(x)
# y = orange and not light
# print(y)
# z = apple and not light
# print(z)


'''5.Write a python program to create a 
histogram in one print from given number. You 
know that your number have three-digit. 
Example:
>>> input 254
>>> output **
           *****
           ****'''
# a = int(input('x(three digits) = '))
# x = a // 100
# y = (a - x * 100) // 10
# z = a % 10
# res1 = x * '*'
# res2 = y * '*'
# res3 = z * '*'
# print(res1+'\n'+res2+'\n'+res3)

'''6.You have two input,in numbers all 2,4 you will replace with 5,
 and than multiply them, if the answer negative replace it to positive. '''
# x = input('x = ')
# y = input('y = ')
# z1 = x.replace('2','5')
# z2 = z1.replace('4','5')
# z3 = y.replace('2','5')
# z4 = z3.replace('4','5')
# a = int(z2) * int(z4)
# print('first number =',z2,'second number =',z4,'a =',abs(a))