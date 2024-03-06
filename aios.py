import tkinter as tk
import webbrowser
from settings import Settings
from easy_paste import EasyPaste
from join import Join 
from split import Split 
from downpic import DownPic

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.title('All in one Scanlation tools')
        self.resizable(False, False)

        self.frame = tk.Frame(bg=self.settings.root_color)
        self.frame.pack()

        # define buttons
        bt_join = tk.Button(self.frame, text="Join the images", command=self.create_join_window, fg=self.settings.fg_color, bg=self.settings.bg_color)
        bt_join.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        bt_split = tk.Button(self.frame, text="Split the images", command=self.create_split_window, fg=self.settings.fg_color, bg=self.settings.bg_color)
        bt_split.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

        bt_downpic = tk.Button(self.frame, text="Download from URL", command=self.create_downpic_window, fg=self.settings.fg_color, bg=self.settings.bg_color)
        bt_downpic.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

        bt_easypaste = tk.Button(self.frame, text="Easy Paste", command=self.create_easypaste_window, fg=self.settings.fg_color, bg=self.settings.bg_color)
        bt_easypaste.grid(row=1, column=1, pady=10, padx=10, sticky='ew')

        bt_fblink = tk.Button(self.frame, text="Fb Channel", command=self.open_facebook, fg=self.settings.fg_color, bg=self.settings.bg_color)
        bt_fblink.grid(row=3, column=0, pady=10, padx=10, sticky='ew')

        bt_youtubelink = tk.Button(self.frame, text="You Tube", command=self.open_youtube, fg=self.settings.fg_color, bg=self.settings.bg_color)
        bt_youtubelink.grid(row=3, column=1, pady=10, padx=10, sticky='ew')

        # label
        label = tk.Label(self.frame, text='For scanlation tutorials, visit us on YouTube and Facebook', anchor='center', bg=self.settings.bg_color, fg=self.settings.fg_color)
        label.grid(row=2, column=0, columnspan=3, sticky='ew')

        self.join_window = None
        self.split_window = None 
        self.easypaste_window = None
        self.downpic_window = None

    def create_join_window(self):
        if self.join_window is None or not self.join_window.winfo_exists():
            # create a toplevel window under the first frame
            self.join_window = tk.Toplevel(self.frame)
            Join(self.join_window)
        else:
            self.join_window.lift()

    def create_split_window(self):
        if self.split_window is None or not self.split_window.winfo_exists():
            # create a toplevel window under the first frame
            self.split_window = tk.Toplevel(self.frame)
            Split(self.split_window)
        else:
            self.split_window.lift()

    def create_easypaste_window(self):
        if self.easypaste_window is None or not self.easypaste_window.winfo_exists():
            # create a toplevel window under the first frame
            self.easypaste_window  = tk.Toplevel(self.frame)
            EasyPaste(self.easypaste_window)
        else:
            self.easypaste_window.lift()

    def create_downpic_window(self):
        if self.downpic_window is None or not self.downpic_window.winfo_exists():
            # create a toplevel window under the first frame
            self.downpic_window = tk.Toplevel(self.frame)
            DownPic(self.downpic_window)
        else:
            self.downpic_window.lift()

    def open_facebook(self):
        webbrowser.open('https://www.facebook.com/profile.php?id=100090927574628')

    def open_youtube(self):
        webbrowser.open('https://www.youtube.com/channel/UCwH7FdD-fp6LcraA7tDM8sA')
