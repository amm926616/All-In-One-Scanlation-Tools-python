import tkinter as tk
from PIL import Image
from tkinter import filedialog
import os
from settings import Settings

class Join():
	def __init__(self, master):
		self.settings = Settings()
		master.resizable(0, 0)
		master.title('Images Joining Tool')
		master.config(bg=self.settings.root_color)

		#4 buttons
		self.load_bt = tk.Button(master, text="Load Images Folder", command=self.ask_folder_dir, bg=self.settings.bg_color, fg=self.settings.fg_color)
		self.load_bt.grid(row=0 , column=0, padx=10, pady=10, sticky='ew')
		self.save_bt = tk.Button(master, text="Save Images Folder", command=self.ask_save_dir, bg=self.settings.bg_color, fg=self.settings.fg_color)
		self.save_bt.grid(row=1 , column=0, padx=10, pady=10, sticky='ew')		
		self.start_bt = tk.Button(master, text='Start the process', command=self.join, bg=self.settings.bg_color, fg=self.settings.fg_color)
		self.start_bt.grid(row= 6, column=0, padx=10, pady=10, sticky='ew')
		self.done_bt = tk.Button(master, text='Close the window', command=master.destroy, bg=self.settings.bg_color, fg=self.settings.fg_color)
		self.done_bt.grid(row= 6, column=1, padx=10, pady=10, sticky='ew')

		#Create a variable to hold the option.
		self.option_2_or_3 = tk.IntVar(value=2)
		self.keep_or_delete = tk.StringVar(value='keep')

		#4 radio buttons
		self.by2_rb = tk.Radiobutton(master, selectcolor=self.settings.bg_color, variable=self.option_2_or_3, value=2, text="join by 2", bg=self.settings.bg_color, fg=self.settings.fg_color).grid(row= 3, column=0, padx=10, pady=1, sticky='ew')
		self.by3_rb = tk.Radiobutton(master, selectcolor=self.settings.bg_color, variable=self.option_2_or_3, value=3, text="join by 3", bg=self.settings.bg_color, fg=self.settings.fg_color).grid(row= 4, column= 0, padx=10, pady=1, sticky='ew')
		self.keep_rb = tk.Radiobutton(master, selectcolor=self.settings.bg_color, variable=self.keep_or_delete, value='keep', text='keep the old images', bg=self.settings.bg_color, fg=self.settings.fg_color).grid(row= 3, column=1, padx=10, pady=1, sticky='ew')
		self.delete_rb = tk.Radiobutton(master, selectcolor=self.settings.bg_color, variable=self.keep_or_delete, value='delete', text='delete the old images', bg=self.settings.bg_color, fg=self.settings.fg_color).grid(row= 4, column=1, padx=10, pady=1, sticky='ew')

		#2 labels
		self.choose_the_method = tk.Label(master, text="*Choose the method", bg=self.settings.bg_color, fg=self.settings.fg_color)
		self.choose_the_method.grid(row=2, column=0, sticky='ew')
		self.choose_keepordelete = tk.Label(master, text='*Keep or delete the images?', bg=self.settings.bg_color, fg=self.settings.fg_color)
		self.choose_keepordelete.grid(row=2, column=1, sticky='ew')
		self.save_location_lb = tk.Label(master, text="<<Save the images to a folder", bg=self.settings.bg_color, fg=self.settings.fg_color)
		self.save_location_lb.grid(row=1 , column=1, padx=10, pady=10, sticky='ew')
		self.load_location_lb = tk.Label(master, text="<<Load images from a folder", bg=self.settings.bg_color, fg=self.settings.fg_color)
		self.load_location_lb.grid(row=0 , column=1, padx=10, pady=10, sticky='ew')

		#remainder
		self.remainder = 0

		# label to show the process to user
		self.process = tk.Label(master, text='First, please choose the images folder and a folder to save.', bg=self.settings.bg_color, fg=self.settings.fg_color)
		self.process.grid(row=5, column=0, columnspan=2, sticky='ew')

		# name count and extension
		self.name_count = 1
		self.extension = 0

	def ask_folder_dir(self):
		global folder_dir
		folder_dir = filedialog.askdirectory(initialdir=os.path.expanduser("~"), title='Select a folder')
		if folder_dir:
			self.load_location_lb.config(text=folder_dir)
			images = os.listdir(folder_dir)
			self.process.config(text='There are ' + str(len(images)) +' images')
		else:
			pass

	def ask_save_dir(self):
		global save_dir
		save_dir = filedialog.askdirectory(initialdir=os.path.expanduser("~"), title='Select a folder')
		if save_dir:
			self.save_location_lb.config(text=save_dir)
		else:
			pass

	def slash(self):
		if self.name_count < 10:
			slash = '/0'
		else:
			slash = '/'

		return slash

	def join_by_2(self, image1, image2):
		im1 = Image.open(image1)
		im2 = Image.open(image2)

		new_im = Image.new('RGB', (im1.width, im1.height + im2.height))

		new_im.paste(im1, (0, 0))
		new_im.paste(im2, (0, im1.height))

		new_im.save(str(save_dir) + self.slash() + str(self.name_count) + '_' + str(self.extension) + '.jpg')

		self.name_count += 1

	def join_by_3(self, image1, image2, image3):
		im1 = Image.open(image1)
		im2 = Image.open(image2)
		im3 = Image.open(image3)

		new_im = Image.new('RGB', (im1.width, im1.height + im2.height + im3.height))

		new_im.paste(im1, (0, 0))
		new_im.paste(im2, (0, im1.height))
		new_im.paste(im3, (0, im1.height + im2.height))

		new_im.save(str(save_dir) + self.slash() + str(self.name_count) + '_' + str(self.extension) + '.jpg')

		self.name_count += 1

	def list_and_sort(self):
		images = os.listdir(folder_dir)
		images = [i for i in images if i.endswith('.jpg')]
		images.sort()
		return images

	def check_division(self):
		images = os.listdir(folder_dir)
		if self.option_2_or_3.get() == 2:
			remainder = len(images)%2

			if remainder == 0:
				self.remainder = 0
			elif remainder == 1:
				self.remainder = 1

		elif self.option_2_or_3.get() == 3:
			remainder = len(images)%3

			if remainder == 0:
				self.remainder = 0
			elif remainder == 1:
				self.remainder = 1
			elif remainder == 2:
				self.remainder = 2

	def saving_last(self, old):
		old = folder_dir + '/' + old 
		new = str(save_dir) + self.slash() + str(self.name_count) + '_' + str(self.extension) + '.jpg'
		os.rename(old, new)

	def join(self):
		self.name_count = 1
		images = self.list_and_sort()
		method = self.option_2_or_3.get()
		choice = self.keep_or_delete.get()
		self.check_division()

		if self.remainder == 0 and method == 2:
			for i in range(0, len(images), 2):
				image1 = folder_dir + '/' + images[i]
				image2 = folder_dir + '/' + images[i+1]
				self.join_by_2(image1, image2)

				if self.keep_or_delete.get() == 'delete':
					os.remove(image1)
					os.remove(image2)

		elif self.remainder == 1 and method == 2:
			last = images.pop()

			for i in range(0, len(images), 2):
				image1 = folder_dir + '/' + images[i]
				image2 = folder_dir + '/' + images[i+1]
				self.join_by_2(image1, image2)
			self.saving_last(last)

		elif self.remainder == 1 and method == 3:
			last = images.pop()

			for i in range(0, len(images), 3):
				image1 = folder_dir + '/' + images[i]
				image2 = folder_dir + '/' + images[i+1]
				image3 = folder_dir + '/' + images[i+2]

				self.join_by_3(image1, image2, image3)

			self.saving_last(last)


		elif self.remainder == 2 and method == 3:
			second = images.pop()
			first = images.pop()

			for i in range(0, len(images), 3):
				image1 = folder_dir + '/' + images[i]
				image2 = folder_dir + '/' + images[i+1]
				image3 = folder_dir + '/' + images[i+2]

				self.join_by_3(image1, image2, image3)

			self.join_by_2(first, second)


		elif self.remainder == 0 and method == 3:
			for i in range(0, len(images), 3):
				image1 = folder_dir + '/' + images[i]
				image2 = folder_dir + '/' + images[i+1]
				image3 = folder_dir + '/' + images[i+2]

				self.join_by_3(image1, image2, image3)

		self.process.config(text='All images have been joined.')

