'''1. Function
Given three numbers a, b (a ≤ b) and step. Create an list of 
evenly spaced elements starting from a to b spaced by 
step. you have 3 argument:
Input Output 
1 5 1 [1, 2, 3, 4, 5] 
10 100 20 [10, 30, 50, 70, 90]'''
# def func(a,b,step):
# 	i = 1
# 	list_ = [a]
# 	x = a
# 	while i < b // step:
# 		x += step
# 		list_.append(x)
# 		i += 1
# 	print(a,b,step,list_)
# func(10,100,20)


'''2. List
Write a function. Create the list which elements are 
products between two neighbours.
Input Output
input : [3, 7, 12, 5, 20, 0] output: [21, 84, 60, 100, 0]
input : [1, 1, 4, 32, 6] output: [1, 4, 128, 192 ]'''
# def func(list1):
# 	list2 = []
# 	for i in range(len(list1) - 1):
# 		a = list1[i] * list1[i + 1]
# 		list2.append(a)
# 	return list2

# print(func([3,7,12,5,20,0]))


'''3. New sentence
Given a sentence with missing words and an array of 
words. Replace all ‘_’ in a sentence with the words from the 
array.
Input “_ we have a _.” 
[“Ashot”, “problem”] 
Output: “Ashot we have a problem.'''
# res = '_ have a _'.split()
# list_ = ['Ani','problem']
# count = 0
# for i in range(len(res)):
# 	if res[i] == '_':
# 		res[i] = list_[count]
# 		count += 1
# print(' '.join(res))


'''4. sum word
Given a list of strings. Find the strings with maximum and 
minimum lengths in array. Print the sum of their lengths.
Input: [“anymore”, “raven”, “me”, “communicate”] 
Output: 13'''
# res = ['anymore','raven','me','communicate']
# c = [len(i) for i in res]
# print(max(c) + min(c))


'''5. find index
Given a list of numbers and a number. Find the index of a 
first element which is equal to that number. If there is not 
such a number, that find the index of the first element 
which is the closest to it. Input Output
[21, -9, 15, 2116, -71, 33], -71 4
[ 36, -12, 47, -58, 148, -55, -19, 10], -56 5'''

# def find_index(my_list,lenght,search):
# 	if search in my_list:
# 		return f'{search} number at index {my_list.index(search)}'
# 	else:
# 		new_list = []
# 		for i in my_list:
# 			res = abs(search - i)
# 			new_list.append(res)
# 		return f'{search} number near at index {new_list.index(min(new_list))}'
# my_list = [21, -9, 15, 2116, -71, 33]
# lenght  = len(my_list)
# search = int(input('number: '))
# result = find_index(my_list,lenght,search)
# print(result)



'''6. New Dict
Define a function which can generate a dictionary where 
the keys are numbers between 1 and N (both included) and 
the values are square of keys. The function should print the 
dict.Example : 
N = 5 
{1: 1, 2:4, 3:9, 4:16, 5:25}'''
# 1.
# n = 5
# dict_ = {}
# for i in range(1,n + 1):
# 	dict_.update({i:i ** 2})
# print(dict_)

# 2.
# n = 5
# c ={i:i ** 2 for i in range(1,n + 1)}
# print(c)


'''7. INVERT Dict
Given an dict. Invert it (keys become values and values 
become keys). If there is more than key for that given value 
create an list.Input 
{ ‘a’: 1, ‘b’: 2, ‘c’: 2 }
Output 
{ 1: ‘a’, 2: [‘b’, ‘c’] } '''
# def chage_dict(MyDict):
# 	result = {}
# 	for i,j in MyDict.items():
# 		if j in result:
# 			if isinstance(j,list):
# 				result[j].append(i)
# 			else:
# 				result[j] = list(result[j])
# 				result[j].append(i)
# 		else:
# 			result[j] = i
# 	return result
# MyDict = {
# 	'a':1,
# 	'b':2,
# 	'c':2
# }
# print(chage_dict(MyDict))
		
'''8. FIBONACCI
Write a function using recursion to find fibonacci numbers:'''

# def fibonacci(x):
# 	if x == 1:
# 		return 0
# 	elif x == 2:
# 		return 1
# 	else:
# 		return fibonacci(x-1) + fibonacci(x-2)
# print(fibonacci(7))
