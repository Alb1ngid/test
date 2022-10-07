class Verification:

    def __init__(self,login,password):
        self.login=login
        self.password=password
        self.__lenPass()

    def __lenPass(self):
        if len(self.password)<8:
            raise ValueError('слабый пароль')

    def save(self):
        with open('users','a') as r:
            r.write(f'{self.login,self.password}'+'\n')



