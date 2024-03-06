import random, re 
from hint import Hint

class Pw_Generator():
	def __init__(self):
		self.elements_dict = {
		    "a": "u3Y$",
		    "b": "+b0P",
		    "c": "~Cp6",
		    "d": "O^d8",
		    "e": "^e5B",
		    "f": "Rw4~",
		    "g": "n2N^",
		    "h": "c@T8",
		    "i": "_dG6",
		    "j": "9G&o",
		    "k": "w+W3",
		    "l": "Gx@4",
		    "m": "L4b@",
		    "n": "+3zI",
		    "o": "O6r!",
		    "p": "D2p#",
		    "q": "Wg&3",
		    "r": "3Jj&",
		    "s": "E6&e",
		    "t": "X~3g",
		    "u": "^eO6",
		    "v": "J4+o",
		    "w": "h@6K",
		    "x": "q#W4",
		    "y": "Bm5^",
		    "z": "+3Ip"
		}

		#tuples for tranformation 3(inversion)
		self.d_inversion = {'~': '1', '!': '2', '@': '3', '#': '4', '$': '5', '^': '6', '&': '7', '*': '8', '_': '9', '+': '0'}
		self.d_keys = tuple(self.d_inversion.keys())
		self.d_numbers = tuple(self.d_inversion.values())

		self.hint = Hint().get_hint()
		self.pc = ''
		self.p_sh = self.hint.index('#')
		self.p_ex = self.hint.index('@')
		self.p_in = self.hint.index('$')

		#hint without trans and numbers
		self.hint_w_tn = self.hint.replace('#', '')
		self.hint_w_tn = self.hint_w_tn.replace('@', '')
		self.hint_w_tn = self.hint_w_tn.replace('$', '')
		self.hint_w_tn = re.sub(r'\d+', '', self.hint_w_tn)
		# print("line 51 " + self.hint_w_tn)

		self.hint_tuple = tuple([i for i in self.hint_w_tn])

	def get_pc(self):
		#pc without transformers
		pc = ''.join([self.elements_dict[i] for i in self.hint_tuple])
		self.pc = pc

	def get_value(self, i):
		value = self.elements_dict[self.hint_tuple[i]]
		return value

	def sh_pc(self):
		sh1 = (0, 1, 3, 2)
		sh2 = (1, 0, 3, 2)
		sh3 = (2, 1, 0, 3)
		sh4 = (0, 3, 1, 2)
		sh5 = (1, 0, 2, 3)
		sh6 = (3, 0, 2, 1)
		sh7 = (3, 2, 0, 1)
		sh8 = (0, 2, 3, 1)

		all_sh = (sh1, sh2, sh3, sh4, sh5, sh6, sh7, sh8)
		sh_method = tuple(all_sh[self.p_sh])
		# print('>>sh_method' + str(sh_method))

		new_tuple = tuple(self.hint_tuple[sh_method[i]] for i in range(4))
		self.hint_tuple = new_tuple

		self.get_pc()

	def ex_pc(self):
		if self.p_ex == 0 or self.p_ex == 1:
			ex_method = 0
		elif self.p_ex == 2 or self.p_ex == 3:
			ex_method = 1
		elif self.p_ex == 4 or self.p_ex == 5:
			ex_method = 2
		elif self.p_ex == 6 or self.p_ex == 7:
			ex_method = 3

		i = 0

		#extract the index positional strings for all 4 main strings.
		s1 = self.get_value(i)[ex_method]
		s2 = self.get_value(i+1)[ex_method]
		s3 = self.get_value(i+2)[ex_method]
		s4 = self.get_value(i+3)[ex_method]

		#the new string combined of 4 s'
		ex_str = s1 + s2 + s3 + s4
		# print(">>extracted string: " + ex_str)
		
		#modifying the main strings
		str_1 = self.get_value(i).replace(f'{s1}', '')
		str_2 = self.get_value(i+1).replace(f'{s2}', '')
		str_3 = self.get_value(i+2).replace(f'{s3}', '')
		str_4 = self.get_value(i+3).replace(f'{s4}', '')

		# s' extracted pc
		str_ex_pc = str_1 + str_2 + str_3 + str_4
		# print(">>remaining string: " + str_ex_pc)

		new_pc = str_ex_pc + ex_str
		self.pc = new_pc

	def in_pc(self):
		new_pc = ''
		for i in range(16):
			if self.pc[i].isupper():
				new_pc += self.pc[i].lower()
			elif self.pc[i].islower():
				new_pc += self.pc[i].upper()
			elif self.pc[i] in self.d_numbers:
				index = self.d_numbers.index(self.pc[i])
				new_pc += self.d_keys[index]
			elif self.pc[i] in self.d_keys:
				index = self.d_keys.index(self.pc[i])
				new_pc += str(self.d_numbers[index])
		self.pc = new_pc

	def run_pw_generator(self):
		self.get_pc()
		# print("---Original pc:")
		# print(self.pc)
		self.sh_pc()
		# print("---After shuffling:")
		# print(self.pc)
		self.ex_pc()
		# print("---After extracting:")
		# print(self.pc)
		self.in_pc()
		# print("---After inverting:")
		# print(self.pc)

