from tkinter import Tk
from main import Verification

class V2(Verification):
    def __init__(self, login, password):

        super().__init__(login, password)

    def save(self):
        with open('users', 'a') as r:
            for i in r:
                if f'{self.login,self.password}'+'\n'==i:
                    raise ValueError('уже есть')
        Verification.save(self)

    def show(self):
        return self.login,self.password

x=V2('ken','123456789')
x.save()
# g=Tk()
# g.mainloop()

class My_tk(Tk):
    def __init__(self):
        Tk.__init__(self)

root=My_tk()
# root.mainloop()