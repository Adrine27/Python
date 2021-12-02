# import random
# res = random.choice('up')
# point = 0
# if res == 'u':
# 	print('Start user')
# 	while True:
# 		end = 3
# 		while True:
# 			if point > 18:
# 				end = 21 - point
# 			user = input(f'1-{end}:')
# 			if user.isdigit():
# 				user = int(user)
# 				if user >= 1 and user <= end:
# 					print(f'User:{point} + {user} = {point + user}')
# 					point += user
# 					break
# 				else:
# 					print(f'Enter a number between 1- {end}')
# 			else:
# 				print('Only numbers')
# 		if point >= 21:
# 			print('Win pc')
# 			break
# 		pc = 4 - point % 4
# 		print(f'PC:{point} + {pc} = {point + pc}')
# 		point += pc
	
# else:
# 	print('Start pc')
# 	while True:
# 		end = 3
# 		if point > 18:
# 			end = 21 - point
# 		if point % 4 == 0:
# 			pc = random.randint(1,end)
# 		else:
# 			pc = 4 - point % 4
# 		print(f'PC:{point} + {pc} = {point + pc}')
# 		point += pc
# 		if point >= 21:
# 			print('Win user')
# 			break
# 		end = 3
# 		while True:
# 			if point > 18:
# 				end = 21 - point
# 			user = input(f'1-{end}:')
# 			if user.isdigit():
# 				user = int(user)
# 				if user >= 1 and user <= end:
# 					print(f'User:{point} + {user} = {point + user}')
# 					point += user
# 					break
# 				else:
# 					print(f'Enter a number between 1- {end}')
# 			else:
# 				print('Only numbers')
# 		if point >= 21:
# 			print('Win pc')
# 			break