'''1.Write a Python program to sort a dictionary
by value.'''
#1.
# thisdict = {
# 	'first':4,
# 	'second':6,
# 	'third':3,
# 	'fourth':10
# }
# x = sorted(thisdict.values())
# print(x)

#2.
# thisdict1 = {
# 	'first':4,
# 	'second':6,
# 	'third':3,
# 	'fourth':10
# }
# x = []
# thisdict2 = {}
# for y in thisdict1.values():
# 	x.append(y)
# 	x.sort()
# for y in x:
# 	for z in thisdict1:
# 		if thisdict1[z] == y:
# 			thisdict2.update({z:y})
# print(thisdict2)

'''2. Write a Python program to add a key to a
dictionary.'''
# thisdict = {
# 	'first':1,
# 	'second':2
# }
# thisdict.update({'third':3})
# print(thisdict)

'''3.Write a Python program to check whether a
given key already exists in a dictionary'''

# thisdict = {
# 	'first':1,
# 	'second':2,
# 	'third':3
# }
# x = 'second'
# if x in thisdict.keys():
# 	print(True)

'''4.Write a Python program to merge two
Python dictionaries.
dict1 = {'a': 50, 'b': 700}
dict2 = {'c': 400, 'd': 600}
output: {'a': 50, 'b': 700, 'c': 400, 'd': 600'''

# dict1 = {
# 'a': 50,
#  'b':700
#   }
# dict2 = {
# 'c': 400,
#  'd': 600
#  }
# dict1.update(dict2)
# print(dict1)

'''5. Write a Python program to multiply all the
values in a dictionary.
For example:
mydict = {'a':1,'b':2,'c':12} output: 24'''

# mydict = {
# 'a':1,
# 'b':2,
# 'c':12
# } 
# y = 1
# for i in mydict.values():
# 	y *= i
# print(y)

'''6. Create a Python program to find the highest
3 values in a dictionary.
{'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
output: {'F': 69, 'A': 67, 'D': 56}'''

# dict1 = {
# 	'D': 56, 
# 	'E': 12,
# 	 'F': 69,
# 	  'C': 45,
# 	   'B': 23, 
# 	     'A': 67
# }
# x = []
# dict2 = {}
# x.append(y)
# x.sort()
# c = x[-3:]
# for y in dict1.values():
# 	for k in dict1:
# 		if dict1[k] in c:
# 			dict2.update({k:dict1[k]})
# print(dict2)

'''7.New_dict
Create a new dictionary:
For example…
s = 'a,2,b,5,c,8,a,4,e,11'
{“a”:6,”b”:5,”c”:8,”e”:11}'''

# s = 'a,2,b,5,c,8,a,4,e,11'.split(',')
# res = {}
# for i in range(0,len(s),2):
# 	if s[i] in res:
# 		res[s[i]] += int(s[i+1])
# 	else:
# 		res[s[i]] = int(s[i+1])
# 		print(res)


'''8.Dict from a string
Create a dictionary from a string.
Get the count of the letters from the string.
word = ‘exercises’
output: {“e”:3,”x”:1,”r”:1,”c”:1,”i”:1,”s”:2'''
# word = 'exercises'
# res = {}
# for i in word:
# 	res[i] = word.count(i)
# print(res) 


'''9. Remove
Remove all duplicate items in list
input:
old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]
output:
new_list = [{'key1':'value1'},{},{'key2':'value2'}'''
# my_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]
# c = []
# for i in my_list:
# 	if i not in c:
# 		c.append(i)
# print(c)

# c = 0
# my_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]
# for i in range(len(my_list)):
# 	if my_list.count(my_list[c]) > 1:
# 		my_list.remove(my_list[c])
# else:
# 	c += 1
# print(my_list)


'''10. New List
Write a Python program to join adjacent members 
of a given list.
Original list:
['1', '2', '3', '4', '5', '6', '7', '8']
Join adjacent members of a given list:
['12', '34', '56', '78']'''
# my_list = ['1','2','3','4','5','6','7','8']
# res = []
# for i in range(0,len(my_list),2):
# 	y = my_list[i] + my_list[i+1]
# 	res.append(y)
# print(res)


'''11. millionaire 
Create a python game Millionaire.'''
# questions = {
# 	'Question 1':{
# 		'q':['When was the battle of Avarayr\na)160 b)400 c)451 d)452','c'],
# 	},
# 	'Question 2':{
# 		'q':['What is high of Everest \na)160 b)400 c)451 d)8849','d'],
# 		},
# 	'Question 3':{
# 	'q':['What will be 9*2-14/7*3 \na)10 b)14 c)12 d)8','c']
# 	},
# 	'Question 4':{
# 	'q':['How many letters are there in the Armenian alphabet? \na)35 b)39 c)30 d)26','b']
# 	},
# 	'Question 5':{
# 	'q':['What is the capital of Great Britain? \na)London b)Paris c)New York d)Berlin','a']
# 	}
# }
# for i in questions:
# 	print(i)
# 	print(questions[i]['q'][0])
# 	ans = input('ans: ')
# 	if ans == questions[i]['q'][1]:
# 		print('right')
# 	else:
# 		print('wrong')


