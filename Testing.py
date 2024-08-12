import random
import time

# def questions():

# 	question = input("Enter value: ")

# 	while True:

# 		try:
# 			int(question)
# 			return question

# 		except ValueError:

# 			print("You must enter a positive integer")
# 			question = input("Enter value: ")




# a = 'vf'

# if isinstance(a, str):

# 	print(questions())
# 	print(a)


se = [2, 4, 6, 8]

de = random.choice(se)

print(de)

se.remove(de)



de = random.choice(se)

print(de)

print(se)