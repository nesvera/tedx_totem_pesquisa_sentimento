from tkinter import Tk

class Root(Tk):
    def __init__(self):
        super().__init__()

        title = "Urna eletronica TedX Blumenau Democracia"
        start_width = 1024
        start_length = 600
        background_color = "#DFDFDF"

        self.geometry(f"{start_width}x{start_length}+0+0")
        self.title(title)
        self.configure(background=background_color)
        self.wm_attributes('-type', 'splash')
        #self.attributes("-fullscreen", True)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
