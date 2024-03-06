import requests 
import os 
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog
from settings import Settings

class DownPic():
    def __init__(self, master):
        self.settings = Settings()
        master.resizable(0, 0)
        master.title('Download from url')
        master.config(bg=self.settings.root_color)

        #row 0
        self.label = tk.Label(master, text='Paste your url here:', fg=self.settings.fg_color, bg=self.settings.bg_color).grid(row=0, column=0,  padx=1, pady=10, sticky='e')
        self.text = tk.Text(master, width=50, height=1)
        self.text.grid(row=0, column=1, padx=1, pady=10, sticky='w')

        #row 1
        self.folder_bt = tk.Button(master, text='Save Images Folder', command=self.ask_folder_dir, fg=self.settings.fg_color, bg=self.settings.bg_color)
        self.folder_bt.grid(row=1, column=0, padx=1, pady=10, sticky='ew')
        self.folder_lb = tk.Label(master, text='<<Save the images to a folder.', fg=self.settings.fg_color, bg=self.settings.bg_color)
        self.folder_lb.grid(row=1, column=1, padx=1, pady=10, sticky='w')

        #row 2
        self.process = tk.Label(master, text='Please select a folder before downloading', fg=self.settings.fg_color, bg=self.settings.bg_color)
        self.process.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

        self.caution = tk.Label(master, text="***Caution! The program doesn't gurantee to work for all websites since there are restrictions, \nit is recommended to directly download images from web brower***", fg='yellow', bg=self.settings.bg_color).grid(row=3, column=0, columnspan=2)

        #row 3
        self.start_bt = tk.Button(master, text='Start Downloading', command=self.download, fg=self.settings.fg_color, bg=self.settings.bg_color)
        self.start_bt.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

        # folder path 
        self.folder_path = 'images'
        self.i = 1

    def slash(self, i):
        if i < 10:
            return '/0'
        else:
            return '/'

    def ask_folder_dir(self):
        folder_path = filedialog.askdirectory(initialdir='.', title='Select a folder')
        self.folder_path = folder_path
        self.folder_lb.config(text=folder_path)

    def download(self):
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
        url = self.text.get("1.0", tk.END)
        # send a request to the website
        response = requests.get(url)

        # parse the HTML content of the website
        soup = BeautifulSoup(response.content, "html.parser")

        # find all image tags in the HTML
        images = soup.find_all("img")

        # download each image and save it to the folder
        for image in images:
            image_url = image.get("src")
            response = requests.get(image_url)
            open(self.folder_path + self.slash(self.i) + f"{self.i}.jpg", "wb").write(response.content)
            self.i += 1
        self.process.config(text='Download images are saved in ' + '"' + self.folder_path + '"')


        

