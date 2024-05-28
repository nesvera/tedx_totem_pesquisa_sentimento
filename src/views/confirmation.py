from tkinter import Frame, Label, PhotoImage, ttk
from PIL import Image

class ConfirmationView(Frame):
    def __init__(self, *args, **kwargs):

        self.candidate_number = kwargs.pop("candidate_number", "")
        self.candidate_name = kwargs.pop("candidate_name", "")
        self.candidate_party = kwargs.pop("candidate_party", "")
        self.candidate_image = kwargs.pop("candidate_image", "")

        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)

        self.configure(bg="#DFDFDF")

        self.header = Label(self, text="SEU VOTO", font=(None, 25), bg="#DFDFDF")
        self.header.grid(row=0, column=0, columnspan=5, padx=00, pady=(20, 30))

        self.number_label = Label(self, text="Número:", font=(None, 15), bg="#DFDFDF")
        self.number_selected = Label(self, text=self.candidate_number, font=(None, 20), anchor="w", justify="left", bg="#DFDFDF")
        self.number_label.grid(row=1, column=0, padx=(10, 0), pady=(50, 1), sticky="w")
        self.number_selected.grid(row=1, column=1, columnspan=2, padx=(0, 10), pady=(50, 1), sticky="w")

        self.feeling_label = Label(self, text="Candidato:", font=(None, 15), bg="#DFDFDF")
        self.feeling_selected = Label(self, text=self.candidate_name, font=(None, 20), anchor="w", justify="left", bg="#DFDFDF")
        self.feeling_label.grid(row=2, column=0, padx=(10, 0), pady=(0, 1), sticky="w")
        self.feeling_selected.grid(row=2, column=1, columnspan=2, padx=(0, 10), pady=(0, 1), sticky="w")

        self.name_label = Label(self, text="Filiação:", font=(None, 15), bg="#DFDFDF")
        self.name_selected = Label(self, text=self.candidate_party, font=(None, 20), anchor="w", justify="left", bg="#DFDFDF")
        self.name_label.grid(row=3, column=0, padx=(10, 0), pady=(0, 1), sticky="w")
        self.name_selected.grid(row=3, column=1, columnspan=2, padx=(0, 10), pady=(0, 0), sticky="w")

        self.label_s1 = Label(self, text="Aperte a tecla:", font=(None, 15), bg="#DFDFDF")
        self.label_s1.grid(row=5, column=0, padx=(10, 0), pady=(140,1), sticky="w")

        self.label_s2 = Label(self, text="VERDE: para CONFIRMAR", font=(None, 15), bg="#DFDFDF")
        self.label_s2.grid(row=6, column=1, padx=(10, 0), pady=(0,1), sticky="w")

        self.label_s3 = Label(self, text="LARANJA: para CORRIGIR", font=(None, 15), bg="#DFDFDF")
        self.label_s3.grid(row=7, column=1, padx=(10, 0), pady=(0,1), sticky="w")

        image = PhotoImage(file=self.candidate_image)
        self.image_label = Label(image=image)
        self.image_label.image = image
        self.image_label.grid(row=0, column=1, padx=(0, 10), pady=(20, 20))
        #self.image_label.place(x=200, y=200)

    def erase(self):
        self.image_label.grid_remove()
        self.destroy()
