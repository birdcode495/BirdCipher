

def questions():

	question = input("Enter value: ")

	while True:

		try:
			int(question)
			return question

		except ValueError:

			print("You must enter a positive integer")
			question = input("Enter value: ")




a = 'vf'

if isinstance(a, str):

	print(questions())
	print(a)