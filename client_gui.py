from customtkinter import CTk,CTkTextbox,CTkButton

class client_gui(CTk):
    def __init__(self):
        super().__init__()
        self.title('mygui')
        self.geometry('920x560')
        self.resizable(False,False)

        self.text = CTkTextbox(self,width=250).pack()
        
        self.get = CTkButton(self,width=50).pack()


if __name__ == '__main__':
    cl = client_gui()
    cl.mainloop()


