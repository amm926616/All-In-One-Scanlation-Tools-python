import random

class Hint():
	def __init__(self):
		pass
		
	def get_hint(self):
		small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

		#letters 
		let1 = random.choice(small_letters)
		let2 = random.choice(small_letters)
		let3 = random.choice(small_letters)
		let4 = random.choice(small_letters)

		#transformers
		tran1 = '#'
		tran2 = '@'
		tran3 = '$'

		#number
		num = str(random.randint(1, 9))

		#listing for hint
		hint_list = [let1, let2, let3, let4, tran1, tran2, tran3, num]
		lst = hint_list.copy()
		random.shuffle(lst)

		hint = ''.join(lst)
		
		return hint


	