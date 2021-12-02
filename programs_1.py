'''1. Dict
You have two list convert it in dictionary and add 
in (mydict.txt) and show result:
for example: input :
first = [‘Ani’, ‘Jessy’, ‘Ben’] 
second = [1,2,3]
my_dict = {1 : “Ani” , 2: “Jessy”, 3: “Ben”}'''
# first = ['Ani','Jessy','Ben']
# second = [1,2,3]
# dict_ = dict(zip(second,first))
# print(dict_)
# f = open('mydict.txt','w')
# f.write(str(dict_))

'''2.Create json file and save them lyrics (song) 
and print in cmd word this song.'''
# import json
# songs = {
# 	'hello':'sadcfeasdrfvsad',
# 	'senorita':'adcmfeajfnciebdic',
# 	'ti':'iasuedcnwiedcbnjdsc'
# }
# songs = [songs]
# with open('song.json','w') as f:
# 	json.dump(songs,f)
# song = input('song name: ')
# with open('song.json') as f:
# 	c = json.load(f)
# 	c = c[0]
# 	if song in c:
# 		print(song,c[song])
# 	else:
# 		print('no')

'''3.Write a python program which have one input an 
integer, representing the sum of all the multiples of 
3 and 5 below the given input. and save this result 
in json file.
for example: 
input 10 (3, 5, 6 and 9)
output:23'''
# import json
# def sum_(n):
# 	n = 0
# 	for i in range(x):
# 		if i % 3 == 0 or i % 5 == 0:
# 			n += i
# 	print('sum =',n)
# 	with open('sum.json','w') as f:
# 		json.dump(n,f)
# x = int(input('write a number: '))
# sum_(x)

'''4. Vowels
Write a program that takes in a string as input, 
counts and outputs the number of vowels. 
And add result in json file.
for example:
input: test
output: 1'''
# import json
# word = input('write a word: ')
# vowels = 'aeiouy'
# count = 0
# for i in word:
# 	if i in vowels:
# 		count += 1
# 		with open('vowel.json','w') as f:
# 			json.dump(count,f)
# print(count)

'''5.You have text.txt file and contains such text:
Another pause and more eying and siding around 
each other
You can create one dict where you have.
‘’Another’’:1
‘’and’’:2
…………….'''
# f = open('text.txt','w')
# f.write('Another pause and more eying and siding around each other')
# f = open('text.txt','r')
# x = f.readline().split()
# dict_ = {}
# for i in x:
# 	count = x.count(i)
# 	dict_.update({i:count})
# print(dict_)

'''6. NEw list
Write a python function which get a new list 
from a given list, consisting of the first 
repeating elements.
my_list = [“a”,”b”,”a”,”c”,”b”]
output “a”,”b”,”c”'''
# def function(my_list2):
# 	my_list2 = []
# 	for i in my_list1:
# 		if i not in my_list2:
# 			my_list2.append(i)
# 	print(my_list2)
# my_list1 = ['a','b','a','c','b']
# function(my_list1)

'''7.You have word.txt file and in them you have 
one story.
Write a Python function that accepts this 
story and calculate the number of uppercase 
letters and lowercase letters. '''
# f = open('word.txt','w')
# f.write('isdhbcsIDbJNCIJASBjbsdcjbSJDBCdfvd')
# def count(upper,lower):
# 	for i in x:
# 		if i.isupper():
# 			upper += 1
# 		elif i.islower():
# 			lower += 1
# 	print('upper-',upper,'\nlower-',lower)
# f = open('word.txt','r')
# x = f.readline()
# upper = 0
# lower = 0
# count(upper,lower)

'''8.You have test.txt file and in them you have 
one story overwrite this story in another file.'''
# f1 = open('test1.txt','w')
# f1.write('xdcfvghjkkmjnhbgvfcdxsdfghj')
# f1 = open('test1.txt','r')
# f2 = open('test2.txt','w')
# for i in f1:
# 	f2.write(i)

