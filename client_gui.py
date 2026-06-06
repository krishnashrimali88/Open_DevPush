from customtkinter import CTk,CTkTextbox,CTkButton,filedialog
from connection import update
import asyncio
import threading


class client_gui(CTk):
    def __init__(self):
        super().__init__()
        self.title('mygui')
        self.geometry('920x560')
        self.resizable(False,False)

        self.text = CTkTextbox(self,width=250)
        self.text.pack()
        
        self.get = CTkButton(self,width=50,text='update',command=self.runner)
        self.get.pack()

        self.get = CTkButton(self,width=50,text='choose directory',command=self.choose)
        self.get.pack()




    def runner(self):
        threading.Thread(target=lambda:asyncio.run(update(self.text)),daemon=True).start()
        

    def choose(self):
        self.dir = filedialog.askdirectory(title='choose directory')
        print(self.dir)




if __name__ == '__main__':
    cl = client_gui()
    cl.mainloop()


