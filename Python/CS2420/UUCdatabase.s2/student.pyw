class Student:
    def __init__(self, l, f, s, e, a):
        self.mLast = l
        self.mFirst = f
        self.mSSN = s
        self.mEmail = e
        self.mAge = a

    def GetAge(self):
        return self.mAge

    def __eq__(self, rhs):
        return self.mSSN==rhs.mSSN

    def __ne__(self, rhs):
        return self.mSSN!=rhs.mSSN

    def __lt__(self, rhs):
        return self.mSSN<rhs.mSSN
    

    
