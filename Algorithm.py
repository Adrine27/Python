'''1.Recursion'''
# def recursion():
# 	print('hello world')
# 	recursion()
# recursion()

'''2.factorial'''
# def factorial(x):
# 	if x == 0:
# 		return 1
# 	elif x == 1:
# 		return 1
# 	else:
# 		return x * factorial(x-1)
# print(factorial(5)) 

'''3.fibonacci'''
# def fibonacci(x):
# 	if x == 1:
# 		return 0
# 	elif x == 2:
# 		return 1
# 	else:
# 		return fibonacci(x - 1) + fibonacci(x - 2)
# print(fibonacci(5))

'''4.Linery search'''

# def linery_search(my_list,n,x):
# 	for i in range(0,n):
# 		if my_list[i] == x:
# 			return i
# 	return -1
# my_list = [2,3,4,10,40,21]
# x = 21
# n = len(my_list)
# result = linery_search(my_list,n,x)
# if result == -1:
# 	print('element is not present in list')
# else:
# 	print('element is present at index',result)


# def linary_search(my_list,n,x):
# 	for i in range(0,n):
# 		if my_list[i] == x:
# 			return 1
# 	return -1


# my_list = [1,2,3,4,5,6]
# n = len(my_list)
# x = 5
# result = linery_search(my_list,n,x)
# if result == 1:
# 	print('this element is in the list',x)
# else:
# 	print('this element is not in the list')

'''5.Binary search'''
# def binery_search(my_list,search,start,stop):
# 	if start > stop:
# 		return False
# 	else:
# 		mid = (start + stop) // 2
# 		if search == my_list[mid]:
# 			return mid
# 		elif search < my_list[mid]:
# 			return binery_search(my_list,search,start,mid - 1)
# 		else:
# 			return binery_search(my_list,search,mid + 1, stop)
# search = 156
# start = 0
# my_list = [1,12,14,18,27,34,56,89,123,156,198,300,900,990,1020]
# stop = len(my_list)
# result = binery_search(my_list,search,start,stop)
# if result == False:
# 	print('Item',search,'Not found')
# else:
# 	print('item',search,'found at index:',result)

'''6.Bubble sort'''
# old_list = [10,75,43,15,25,-4,27]
# def bubble_sort(old_list):
# 	last_item = len(old_list) - 1
# 	for i in range(0,last_item):
# 		for j in range(0,last_item - i):
# 			if old_list[j] > old_list[j + 1]:
# 				old_list[j],old_list[j + 1] = old_list[j + 1],old_list[j]
# 	return old_list
# print('Old list',old_list)
# new_list = bubble_sort(old_list).copy()
# print('New list:',new_list)

# old_list = [5,45,3,9,85,1]
# def bubble_sort(old_list):
# 	last_item = len(old_list) - 1
# 	for i in range(0,last_item):
# 		for j in range(0,last_item - i):
# 			if old_list[j] > old_list[j + 1]:
# 				old_list[j],old_list[j + 1] = old_list[j + 1],old_list[j]
# 	return old_list
# print('old_list',old_list)
# new_list = bubble_sort(old_list).copy()
# print('new list',new_list)



