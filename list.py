'''1. Write a Python program to
 sum all the items in a list'''
# 1.
# my_list = [1,3,5,7,9,11,13]
# sum_ = 0
# for i in my_list:
# 	sum_ += i
# print(sum_)

# 2.
# my_list = [1,3,5,7,9,11,13]
# x = sum(my_list)
# print(x)

'''2. Write a Python program 
to multiplies all the items 
in a list'''
# my_list = [1,3,5,7,9,11,13]
# y = 1
# for i in my_list:
# 	y = y * i
# print(y)

'''3. Write a Python program to 
get the largest text from a list'''
#1.
# my_list = ['aaaaaa','bbbbbbb','ccc']
# y = my_list[0]
# for i in my_list:
# 	if len(i) > len(y):
# 		y = i
# print(y)

#2.
# my_list = ['aaaaaa','bbbbbbb','ccc']
# res = max(my_list, key = len)
# print(res)

'''4.Write a Python program that have two 
lists and returns True if they have at least 
one common member.'''
# my_list = [2,5,8,4,6,7]
# my_list2 = [12,2,11,23]
# for i in my_list:
# 	for j in my_list2:
# 		if i == j:
# 			print('True')

'''5. Write a Python program to Sort Words in 
Alphabetic Order'''
# my_list = ['banana','apple','kiwi','cherry']
# my_list.sort()
# print(my_list)


'''6. New List
Create new list which have 6 different data types.
For example: str, int'''
#my_list = [1,1.5,'hello',False,['yes'],'('yes'),range(100)]

'''7. Mac
Create new list which have data notebooks and you want check if 
the data have Mac?
For example: my_list = [“Hp”, “Asus”, “Dell”, “Mac”, ”Lenovo”] 
output: True'''
# my_list = ['Hp','Asus','Dell','Mac','Lenovo'] 
# x = 'Mac'
# if x in my_list:
#   print(True)

'''8. Password
Create python program which will check if your password is strong 
or no. if Len your password is great than 8 and if your password have 
2 numbers and 2 of the following special characters ('!', '@', '#', '$', '%', 
'&', '*') Sample Input: Python@$World11
 Sample Output: Strong'''
# chars = '!@#$%^&*()'
# while True:
#   your_password = input('write a password: ')
#   digit = 0
#   char = 0
#   if len(your_password) < 8:
#       print('Write a password again,it will be more than 8')
#       continue
#   for i in your_password:
#       if i.isdigit():
#           digit += 1
#       elif i in chars:
#           char += 1
#   if digit < 2:
#       print('digits will be more than 2')
#       break
#   if char < 2:
#       print('chars will be more than 2')
#       break
#   print('your password is strong')
#   break

'''9. Link Finder
Create python program where you want to find id in link if link have 
id print id.
Sample Input: https://www.youtube.com/watch?v=RRW2aUSw5vU
Sample Output: RWW2aUSwvU v'''
# link = 'https://www.youtube.com/watch?v=FfWpgLFMI7w'
# id_link = link[link.index('=')+1:]
# print(id_link)

'''10.Sign in
Create python program where you want to check if input word is 
palindrome or no .if yes print Open otherwise Trash
Sample Input: RACECAR
Sample Output: Open'''
# word = input('write a word')
# if word[0:] == word[::-1]:
#   print('Open')
# else:
#   print('Trash')

'''11. String-to-List
Create python program to convert string to a list.'''
#1.
# x = 'lwauefguilerf'
# print(list(x))

#2.
# x = 'lwauefguilerf'
# a = []
# for i in x:
#   a.append(i)
# print(a)

#3.
# x = 'lwauefguilerf'
# y = [i for i in x]
# print(y)

'''12. Even Numbers
Create python program which will show all even numbers in your 
string. Note: you have input where have 5 numbers: 
Sample Input: 12 21 15 19 8
Sample Output: 12 8'''
# x = '12 21 15 19 8'.split()
# for i in x:
#   if int(i) % 2 == 0:
#       print(i)

'''13. Odd
Write a Python program to select the odd items of a list. And delete
even items.'''
# my_list = [12,25,45,74,6,9]
# my_list2 = []
# for i in my_list:
#   if int(i) % 2 != 0:
#       my_list2.append(i)
# print(my_list2)
    
'''14. Secret Santa
Your group have 5 people and each of them can 
take one name and when take this name is delete 
from this list.And he can not take his name:'''

# group = ['Adrine','Nver','Ani','Narek','Arevik']
# print(group)
# while True:
#   y = input('Write your name: ')
#   x = input('Select a name: ')
#   if y in x:
#       print("it is your name,pls take someone else's name")   
#       continue
#   if x in group:
#       group.remove(x)
#       print(group)