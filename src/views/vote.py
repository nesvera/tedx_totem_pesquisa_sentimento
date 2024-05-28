from tkinter import Frame, Label

class VoteView(Frame):
    def __init__(self, *args, **kwargs):
        candidate_number = kwargs.pop("candidate_number", "")

        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)

        candidate_number_d = ["  ", "  "]

        for i, value in enumerate(candidate_number):
            if i >= 2:
                break

            candidate_number_d[i] = value

        self.header = Label(self, text="CANDIDATO", font=(None, 60))
        self.header.grid(row=0, column=0, columnspan=6, padx=0, pady=(100, 10))

        self.digit_one = Label(self, text=candidate_number_d[0], height=0, borderwidth=2, relief="solid", bg="#DFDFDF", font=(None, 100))
        self.digit_two = Label(self, text=candidate_number_d[1], height=0, borderwidth=2, relief="solid", bg="#DFDFDF", font=(None, 100))

        self.digit_one.grid(row=1, column=2, padx=(0,0), pady=(0,10), ipadx=50, ipady=2)
        self.digit_two.grid(row=1, column=3, padx=(0,0), pady=(0,10), ipadx=50, ipady=2)

    def erase(self):
        self.destroy()
