'''1. Calculator'''
# class calculator:

# 	def __init__(self,x,y):
# 		self.x = x
# 		self.y = y

# 	def add(self):
# 		return self.x + self.y
# 	def minus(self):
# 		return self.x - self.y
# 	def div(self):
# 		return self.x / self.y
# 	def mult(self):
# 		return self.x * self.y

# res = calculator(5,12)
# ch = input('+ - * / ')
# if ch == '+':
# 	print(res.add())
# elif ch == '-':
# 	print(res.minus())
# elif ch == '*':
# 	print(res.mult())
# elif ch == '/':
# 	print(res.div())


'''2. Car
Create a class for Car and Person'''
# class CarPerson:
# 	def __init__(self,car,name):
# 		self.car = car
# 		self.name = name
# x = CarPerson('Mercedes','Vardushik')
# print(x.car,x.name)


'''3.Change. 
Create a class Change:You have 3 methods 
in your class:
Usd --- Eur
Usd --- Amd
Usd --- Ru'''

# class Change:
# 	def __init__(self,Usd):
# 		self.Usd = Usd
# 	def Amd(self):
# 		return Usd * 480
# 	def Eur(self):
# 		return Usd * 0.8
# 	def Ru(self):
# 		return Usd * 70
# Usd = int(input('Usd:'))
# result = Change(Usd)
# choice = input('Amd,Eur,Ru: ')
# if choice == 'Amd':
# 	print(result.Amd())
# elif choice == 'Eur':
# 	print(result.Eur())
# elif choice == 'Ru':
# 	print(result.Ru())
# else:
# 	print('Error')


'''4.Max
Write a python class to find max, min num
and sum in your list:
don’t use max sum and min function'''
# class MinMax:
#     def __init__(self,list_,min_,max_):
#         self.list_ = list_
#         self.min_ = min_
#         self.max_ = max_
#     def result1(self):
#         print('min:',self.min_,'\nmax:',self.max_)
# class Sum:
#     def __init__(self,list_,sum_):
#         self.list_ = list_
#         self.sum_ = sum_
#     def result2(self):
#         for i in list_:
#             self.sum_ += i
#         print('sum:',self.sum_)


# list_ = [6,8,4,7]
# list_.sort()
# sum_ = 0
# p1 = MinMax(list_,list_[0],list_[-1])
# p2 = Sum(list_,sum_)
# p1.result1()
# p2.result2()


'''5.Highest 2
Write a python class to find two highest values in 
your dict:'''
# class highest2:
#     def __init__(self,MyDict,list_,max1,max2):
#         self.MyDict = MyDict
#         self.list_ = list_
#         self.max1 = max1
#         self.max2 = max2
#     def result(self):
#         for i in MyDict.values():
#             list_.append(i)
#         list_.sort()
#         self.max1 = list_[-2]
#         self.max2 = list_[-1]
#         print('The two highest values are:',self.max1,',',self.max2)

# MyDict = {
#     'first':45,
#     'second':72,
#     'third':16
# }
# list_ = []
# max1 = 0
# max2 = 0
# p1 = highest2(MyDict,list_,max1,max2)
# p1.result()


'''6.Inheritance
Write a python class where your child class takes 
all methods in parent class and print them.'''
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# class Student(Person):
#     def __init__(self,name, age, hobby):
#         super().__init__(name, age)
#         self.hobby = hobby
#     def about(self):
#         return f"Name: {self.name}\nAge: {self.age}\nHobby: {self.hobby}"  
# res = Student("Margo",81,'read')
# print(res.about())


'''7.Rectangle
Write a Python class named Rectangle
constructed by a length and width and a method
which will compute the area of a rectangle.'''
# class Rectangle:
#     def __init__(self,height,weight):
#         self.height = height
#         self.weight = weight
#     def area(self):
#         return self.height * self.weight
# class Square(Rectangle):
#     def __init__(self,length):
#         super().__init__(length,length)
# s = Square(10)
# print(s.area())


'''8.Polymorphism
Write a python class where we use polymorphism:
Example:
a.country() - Erevan
b.country() - Paris'''
# class Armenia:
#     def country(self):
#         print('Yerevan')
# class France:
#     def country(self):
#         print('Paris')
# a = Armenia()
# b = France()
# a.country()
# b.country()


'''9. century
Create a class which given a year, return the 
century it is in. The first century spans from the 
year 1 up to and including the year 100, the 
second - from the year 101 up to and including the 
year 200, etc.
For year = 1900, the output should be = 19'''

# class YearCent:
# 	def __init__(self,year):
# 		self.year = year
# 	def cent(self):
# 		if self.year % 100 == 0:
# 			century = self.year // 100
# 			print(century)
# 		else:
# 			century = year // 100 + 1
# 			print(century)


# year = int(input('year: '))
# p1 = YearCent(year)
# p1.cent()




'''10. Palindrome
Create a class given the string, check if it is a palindrome.
word should be lowercase and 1 ≤ inputString.length ≤ 105
Example 
For inputString = "aabaa", the output should be true; 
For inputString = "abac", the output should be false; 
For inputString = "a", the output should be true.'''
# class Palindrome:
# 	def __init__(self,word):
# 		self.word = word
# 	def pal(self):
# 		list_ = []
# 		if self.word.islower() and 1 <= len(self.word) <= 105:
# 			list_.extend(self.word)
# 			list_.reverse()
# 			x = ''.join(list_)
# 			if self.word == x:
# 				print(x)
# 				print(True)
# 			else:
# 				print(x)
# 				print(False)
# 		else:
# 			print('the word will be lowercase and length will be bigger than 1 and smaller than 105')


# word = input('write a word: ')
# p = Palindrome(word)
# p.pal()



'''11. Largest
Create a Class which given an list of integers, find the pair 
of adjacent elements that has the largest product and 
return that product.
For inputList = [3, 6, -2, -5, 7, 3], 
the output should be = 21.'''
# class Max:
# 	def __init__(self,list_):
# 		self.list_ = list_
# 	def max(self):
# 		list_2 = []
# 		for i in range(len(self.list_)-1):
# 			x = self.list_[i] * self.list_[i + 1]
# 			list_2.append(x)
# 		list_2.sort()
# 		print(list_2[-1])



# list_ = [3, 6, -2, -5, 7, 3]
# p = Max(list_)
# p.max()




'''12. find highest word
Create a class which given a list of strings, return another list 
containing all of its longest strings.
Example 
For inputList = ["aba", "aa", "ad", "vcd", "aba"], 
the output should be
 allLongestStrings(inputList) = ["aba", "vcd", "aba"].'''

# class MaxWord:
# 	def __init__(self,list_1):
# 		self.list_1 = list_1
# 	def max(self):
# 		res = [i for i in self.list_1 if len(i) == max([len(i) for i in self.list_1])]
# 		return res

# list_1 = ["aba", "aa", "ad", "vcd", "aba"]
# p = MaxWord(list_1)
# print(p.max())




'''13. Lucky
Ticket numbers usually consist of an even number of digits.A ticket number is 
considered lucky if the sum of the first half of the digits is equal to the sum of the 
second half.Given a ticket number n, determine if it's lucky or not. Example For 
n = 1230, the output should be 
Lucky(n) = true; 
For n = 239017, 
the output should be Lucky(n) = false'''

# class Lucky:
# 	def __init__(self,n):
# 		self.n = n
# 	def lucky(self):
# 		list_ = []
# 		sum1 = 0
# 		sum2 = 0
# 		list_.extend(self.n)
# 		if len(list_) % 2 == 0:
# 			for i in range(len(list_) // 2):
# 				sum1 += int(list_[0])
# 				list_.remove(list_[0])
# 			print('first sum:',sum1)
# 			for j in list_:
# 				sum2 += int(j)
# 			print('second sum:',sum2)
# 			if sum1 == sum2:
# 				print(True)
# 			else:
# 				print(False)
# 		else:
# 			print("the number of digits' will be even")	

# n = str(int(input("ticket's digits: ")))
# p = Lucky(n)
# p.lucky()




'''14. List sort
Create a class: Some people are standing in a row in a park. There are trees 
between them which cannot be moved. Your task is to rearrange the people by 
their heights in a non-descending order without moving the trees. People can be 
very tall!
Example
 For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
 sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].'''

# class Heights:
# 	def __init__(self,list1):
# 		self.list1 = list1
# 	def SortHeight(self):
# 		j = 0
# 		while j < (len(list1) - 1):
# 			for i in list1:
# 				print(j,' ',i)
# 				if i == -1:
# 					list2.append(i)
# 					j += 1
# 					break
# 				elif i < list1[j]:
# 					list2.append(i)
# 				else:
# 					continue
# 			print(list2)

# list1 = [-1, 150, 190, 170, -1, -1, 160, 180]
# list2 = []
# p = Heights(list1)
# p.SortHeight()




'''15. Weight
Several people are standing in a row and need to be divided into two teams. The 
first person goes into team 1, the second goes into team 2, the third goes into 
team 1 again, the fourth into team 2, and so on.You are given an array of positive 
integers - the weights of the people. Return an array of two integers, where the 
first element is the total weight of team 1, and the second element is the total 
weight of team 2 after the division is complete.
Example For a = [50, 60, 60, 45, 70], the output should be
alternating Sums(a) = [180, 105]'''

# class Teams:
# 	def __init__(self,together):
# 		self.together = together
# 	def team1(self):
# 		sum1 = 0
# 		for i in range(0,len(self.together),2):
# 			sum1 += self.together[i]
# 		list_.append(sum1)
# 	def team2(self):
# 		sum2 = 0
# 		for j in range(1,len(self.together),2):
# 			sum2 += self.together[j]
# 		list_.append(sum2)
# 		print(list_)
# together = [50,60,60,45,70]
# print(together)
# p = Teams(together)
# list_ = []
# p.team1()
# p.team2()


'''16.The doctors and the scientists are found out that you can learn about your illness
coronavirus from home by the following formula. If you duplicate your body temperature by
Celsus with the number of pi(math) and round up to the nearest whole number and if it is
between the intervals of 120 to 128 so you have coronavirus otherwise no.'''

# from math import*
# class Corona:
# 	def __init__(self,temperature):
# 		self.temperature = temperature
# 	def corona(self):
# 		x = self.temperature * pi
# 		x = ceil(x)
# 		if 120 <= x <= 128:
# 			print('You have coronavirus')
# 		else:
# 			print('Everything is ok')
# temperature = float(input('Your temperature: '))
# p = Corona(temperature)
# p.corona()


'''17.The english scientists found out that each english letter has its corresponding numbers. And
they create a chart where: 1 = a, j, s 2 = b, k, t 3 = c, l, u 4 = d, m, v 5 = e, n, w 6 = f, o, x
7 = g, p, y 8 = h, q, z 9 = i, r and you will know if your name is widespread or no when you
square root your name number and arranging number in ascending order is less than 5:'''
# from math import*
# class Widespread:
# 	def __init__(self, name, dict_):
# 		self.name = name
# 		self.dict_ = dict_
# 	def widespread(self):
# 		x = 0
# 		for k in self.name:
# 			for i,j in self.dict_.items():
# 				if k in j:
# 					x += i
# 		print(x)
# 		x = sqrt(x)
# 		x = ceil(x)
# 		if x <= 5:
# 			print('Yes')
# 		else:
# 			print('No')
# dict_ = {
# 	1:'ajs',
# 	2:'bkt',
# 	3:'clu',
# 	4:'dmv',
# 	5:'enw',
# 	6:'fox',
# 	7:'gpy',
# 	8:'hqz',
# 	9:'ir'
# }
# name = input('Write your name: ')
# p = Widespread(name,dict_)
# p.widespread()


'''18.You are Harry Potter and you fight with Lord Voldemort in order to protect your friends.
You should use magic words for winning him. You both use the following magic words
during fighting: Avada Kedavra, Crucio, Imperio . You get 1 point when your word
corresponds to his, otherwise you lose 1 point. You have three attempts and you will
become a winner if you have 2 corresponding words.'''
# import random
# class Game:
# 	def game(self):
# 		my_point = 0
# 		pc_point = 0
# 		while True:
# 			me = input('Avada Kedavra(1), Crucio(2), Imperio(3)')
# 			pc = random.choice('123')
# 			print(pc)
# 			if me == pc:
# 				my_point += 1
# 			else:
# 				pc_point += 1
# 			if my_point == 2:
# 				print('You win')
# 				break
# 			elif pc_point == 2:
# 				print('Win Lord Voldemort')
# 				break
# p = Game()
# p.game()
