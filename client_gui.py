from customtkinter import CTk,CTkFrame,CTkButton,filedialog
from connection import update,down
import asyncio
import threading


class client_gui(CTk):
  
    def __init__(self):
        super().__init__()
        self.dir = None
        self.title('mygui')
        self.geometry('920x560')
        self.resizable(False,False)

        self.frame = CTkFrame(self,width=350,height=300)
        self.frame.pack()
        

        self.get = CTkButton(self,width=50,text='update',command=lambda:asyncio.run(update(self.frame)))
        self.get.pack()

        self.net = CTkButton(self,width=50,text='choose directory',command=self.choose)
        self.net.pack()

        self.download = CTkButton(self,width=50,text='download',command=lambda:asyncio.run(down(self.dir)))
        self.download.pack()    




    def runner(self):
        threading.Thread(target=lambda:asyncio.run(update(self.text)),daemon=True).start()
        

    def choose(self):
        self.dir = filedialog.askdirectory(title='choose directory')
        print(self.dir)




if __name__ == '__main__':
    cl = client_gui()
    cl.mainloop()


