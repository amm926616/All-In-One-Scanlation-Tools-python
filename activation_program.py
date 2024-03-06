import tkinter as tk 
import pyperclip as clip
from easy_json import edit_values

class Activate():
	def __init__(self, pc, subscription_number):
		self.passed = False 
		self.pc = pc
		self.subscription_number = subscription_number
		self.root = tk.Tk()
		self.root.title("Activate the program")
		self.root.resizable(0, 0)
		self.root.config(bg='#303030')
		self.sub_code = tk.Label(self.root, text="subscription code: " + subscription_number, fg='#f88dff', bg='#303030').grid(row=0, column=0, sticky='e')
		self.copy = tk.Button(self.root, text='copy ', command=self.copy_code, bg='#505050', fg='#00d8ff')
		self.copy.grid(row=0, column=1, sticky='w')
		self.label = tk.Label(self.root, text='"To use this program, you must proceed with a passcode. \nContact the developer to buy a passcode which has 30 days subscription. \nYou need subscription code to ask for passcode."', fg='white', bg='#303030').grid(row=1, column=0, columnspan=2)
		self.label1 = tk.Label(self.root, text='Paste your passcode and press OK', fg='red', bg='#303030')
		self.label1.grid(row=2, column=0, columnspan=2)
		self.entry = tk.Entry(self.root, width=50)
		self.entry.grid(row=4, column=0, columnspan=2)
		self.butoon = tk.Button(self.root, width=10, height=1, text='OK', command=self.check_pc, bg='#505050', fg='#00d8ff').grid(row=5, column=0, columnspan=2, padx=10, pady=10)
		self.root.mainloop()

	def check_pc(self):
		user_pc = self.entry.get()
		if user_pc == self.pc:
			edit_values('sub_state', 'ALREADYPAIDFORTHEPROGRAM')
			self.label1.config(text='Thank you so much for your subscription. \nPlease close this window and start the program again. \nThe program is ready to use.', fg='#0eff03')
			self.passed = True
		elif user_pc == '':
			self.label1.config(text="You haven't put anything yet.")
		else:
			self.label1.config(text="The passcode doesn't seem to be right")

	def copy_code(self):
		clip.copy(self.subscription_number)
