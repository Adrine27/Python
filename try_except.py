'''IndexError is thrown when trying to access an item at an invalid index.'''
# try:
#  	mylist = []
#  	print(mylist[1])
#  except IndexError:
#  	print('Index Error')


'''KeyError is thrown when a key is not found.'''
# try:
# 	dict_ = {
# 	'a':1,
#  	'b':2
# 		}
# 	print(dict_[5])
# except KeyError:
# 	print('Key Error')

'''TypeError is thrown when an operation or function is applied to an object of
an inappropriate type.'''
# try:
# 	print(10 + 'h')
# except TypeError:
# 	print('Type Error')


'''NameError is thrown when an object could not be found.'''
# try:
# 	print(x)
# except NameError:
# 	print('Name Error')

'''ZeroDivisionError is thrown when the second operator in the division is zero.'''
# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print('number not / 0')

'''ModuleNotFoundError is thrown when a module could not be found.'''
# try:
# 	import a
# except ModuleNotFoundError:
# 	print('Module Not Found Error')


'''Password generator with try except.'''
# import random
# import string
# def generate_password(length):
# 	lower = string.ascii_lowercase
# 	upper = string.ascii_uppercase
# 	digits = string.digits
# 	all_ = lower + upper + digits
# 	password = ''
# 	for i in range(length):
# 		password += random.choice(all_)
# 	return password
# while True:
# 	try:
# 		length = int(input('length of password: '))
# 		break
# 	except ValueError:
# 		print('length will be a number')
# print(generate_password(length))


'''Calculator'''
# try:
# 	x = int(input('x = '))
# 	y = int(input('y = '))
# 	z = int(input('sum(1),subtract(2),multiply(3),devide(4)'))
# 	if z == 1:
# 		print(f'{x} + {y} = {x + y}')
# 	elif z == 2:
# 		print(f'{x} - {y} = {x - y}')
# 	elif z == 3:
# 		print(f'{x} * {y} = {x * y}')
# 	elif z == 4:
# 		try:
# 			print(f'{x} / {y} = {x / y}')
# 		except ZeroDivisionError:
# 			print("y won't be 0")
# except ValueError:
# 	print('will be a number')