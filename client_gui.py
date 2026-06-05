from customtkinter import CTk

class client_gui(CTk):
    def __init__(self):
        super().__init__()
        self.title('mygui')
        self.geometry('920x560')
        self.resizable(False,False)

if __name__ == '__main__':
    cl = client_gui()
    cl.mainloop()


