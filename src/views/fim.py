from tkinter import Frame, Label

class FimView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="FIM", font=(None, 60))
        self.header.grid(row=0, column=0, pady=(180,0))

    def erase(self):
        self.destroy()