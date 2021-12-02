'''1. Odd
Write a recursive function to determine whether all 
digits of the number are odd or not. 
Input Output
4211133 False
7791 True 
5 True'''
# x = 135798
# x = str(x)
# def number_odd(x):
# 	if int(x[-1]) % 2 == 0:
# 		return False
# 	elif len(x) == 1:
# 		return True
# 	else:
# 		return number_odd(x[:-1])
# print(number_odd(x))

'''2. Threading 
Write a python function all even number in 
10.000 use threading and print time.'''

# import threading
# import time
# def func(start,step,end):
# 	while start + step <= end:
# 		print(start + step)
# 		time.sleep(0.1)
# 		func(start + 2,step,end)
# 		break
# y = threading.Thread(target=func,args=(0,2,100))
# y.start()


'''3.Given N number. Write a recursive function that 
should print from 1 to N numbers.
Input Output 
5 1, 2, 3, 4, 5 '''
# def printN(a,n):
# 	if a > n:
# 		return
# 	print(a,end = ' ')
# 	return printN(a + 1,n)
# printN(1,5)