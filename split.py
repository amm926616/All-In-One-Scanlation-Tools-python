import tkinter as tk 
from tkinter import filedialog
from PIL import Image
import os
from time import sleep
from settings import Settings

class Split():
	def __init__(self, master):
		self.settings = Settings()
		master.resizable(0, 0)
		master.title('Images Splitting Tool')
		master.config(bg=self.settings.root_color)

		#4 buttons
		self.load_bt = tk.Button(master, text="Load Images Folder", command=self.ask_folder_dir, fg=self.settings.fg_color, bg=self.settings.bg_color)
		self.load_bt.grid(row=0 , column=0, padx=10, pady=10, sticky='ew')
		self.save_bt = tk.Button(master, text="Save Images Folder", command=self.ask_save_dir, fg=self.settings.fg_color, bg=self.settings.bg_color)
		self.save_bt.grid(row=1 , column=0, padx=10, pady=10, sticky='ew')		
		self.start_bt = tk.Button(master, text='Start the process', command=self.split_images, fg=self.settings.fg_color, bg=self.settings.bg_color)
		self.start_bt.grid(row= 7, column=0, padx=10, pady=10, sticky='ew')
		self.done_bt = tk.Button(master, text='Close the window', command=master.destroy, fg=self.settings.fg_color, bg=self.settings.bg_color)
		self.done_bt.grid(row= 7, column=1, padx=10, pady=10, sticky='ew')

		#Create a variable to hold the option.
		self.option_2_or_3 = tk.IntVar(value=2)
		self.keep_or_delete = tk.StringVar(value='keep')

		#4 radio buttons
		self.by2_rb = tk.Radiobutton(master, selectcolor=self.settings.bg_color, variable=self.option_2_or_3, value=2, text="split by 1/2", fg=self.settings.fg_color, bg=self.settings.bg_color).grid(row= 4, column=0, padx=10, pady=1, sticky='ew')
		self.by3_rb = tk.Radiobutton(master, selectcolor=self.settings.bg_color, variable=self.option_2_or_3, value=3, text="split by 1/3", fg=self.settings.fg_color, bg=self.settings.bg_color).grid(row= 5, column= 0, padx=10, pady=1, sticky='ew')
		self.keep_rb = tk.Radiobutton(master, selectcolor=self.settings.bg_color, variable=self.keep_or_delete, value='keep', text='keep the old images', fg=self.settings.fg_color, bg=self.settings.bg_color).grid(row= 4, column=1, padx=10, pady=1, sticky='ew')
		self.delete_rb = tk.Radiobutton(master, selectcolor=self.settings.bg_color, variable=self.keep_or_delete, value='delete', text='delete the old images', fg=self.settings.fg_color, bg=self.settings.bg_color).grid(row= 5, column=1, padx=10, pady=1, sticky='ew')

		#2 labels
		self.choose_the_method = tk.Label(master, text="*Choose the method", fg=self.settings.fg_color, bg=self.settings.bg_color)
		self.choose_the_method.grid(row=3, column=0, sticky='ew')
		self.choose_keepordelete = tk.Label(master, text='*Keep or delete the images?', fg=self.settings.fg_color, bg=self.settings.bg_color)
		self.choose_keepordelete.grid(row=3, column=1, sticky='ew')
		self.save_location_lb = tk.Label(master, text="<<Save the images to a folder", fg=self.settings.fg_color, bg=self.settings.bg_color)
		self.save_location_lb.grid(row=1 , column=1, sticky='w')
		self.load_location_lb = tk.Label(master, text="<<Load images from a folder", fg=self.settings.fg_color, bg=self.settings.bg_color)
		self.load_location_lb.grid(row=0 , column=1, sticky='w')

		# label to show the process to user
		self.process = tk.Label(master, text='First, please choose the images folder and a folder to save.', fg=self.settings.fg_color, bg=self.settings.bg_color)
		self.process.grid(row=6, column=0, columnspan=2, sticky='ew')

		#name count and extension
		self.name_count = 1
		self.extension = 0

	def ask_folder_dir(self):
		global folder_dir
		folder_dir = filedialog.askdirectory(initialdir=os.path.expanduser("~"), title='Select a folder')
		if folder_dir:
			self.load_location_lb.config(text=folder_dir)
			images = os.listdir(folder_dir)
			self.process.config(text='There are ' + str(len(images)) + ' images.')
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
		
	def split_by_2(self, image, keep_or_delete):
		#opening the image
		image = folder_dir + '/' + image
		im = Image.open(image)

		#the width and the height of new images
		width = im.width
		height = (im.height)/2
		height = int(height)

		upper = im.crop((0, 0, width, height))
		lower = im.crop((0, height, width, 2*height))

		if keep_or_delete == 'delete':
			os.remove(image)

		upper.save(str(save_dir) + self.slash() + str(self.name_count) + '_' + str(self.extension) + '.jpg')
		self.name_count += 1 

		lower.save(str(save_dir) + self.slash() + str(self.name_count) + '_' + str(self.extension) + '.jpg')
		self.name_count += 1




	def split_by_3(self, image, keep_or_delete):
		#opening the image
		image = folder_dir + '/' + image
		im = Image.open(image)

		#the width and the height of new images
		width = im.width
		height = (im.height)/3
		height = int(height)

		upper = im.crop((0, 0, width, height))
		middle = im.crop((0, height, width, 2*height))
		lower = im.crop((0, 2*height, width, 3*height))

		if keep_or_delete == 'delete':
			os.remove(image)

		upper.save(str(save_dir) + self.slash() + str(self.name_count) + '_' + str(self.extension) + '.jpg')
		self.name_count += 1 

		middle.save(str(save_dir) + self.slash() + str(self.name_count) + '_' + str(self.extension) + '.jpg')
		self.name_count += 1

		lower.save(str(save_dir) + self.slash() + str(self.name_count) + '_' + str(self.extension) + '.jpg')
		self.name_count += 1



	def list_and_sort(self, folder_dir):
		images = os.listdir(folder_dir)
		images = [i for i in images if i.endswith('.jpg')]
		images.sort()
		return images

	def split_images(self):
		images = self.list_and_sort(folder_dir)
		self.name_count = 1

		if self.option_2_or_3.get() == 2:
			for image in images:
				self.split_by_2(image, self.keep_or_delete.get())		

		elif self.option_2_or_3.get() == 3:
			for image in images:
				self.split_by_3(image, self.keep_or_delete.get())

		self.process.config(text='All images have been split.')

