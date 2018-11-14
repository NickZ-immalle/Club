class Membership:
    def __init__(self, name, month, year):
        self.name = name
        self.month = month
        self.year = year

    def Membership(self, name, month, year):
        if self.month < 1 or self.month > 12:
            print("Month ", self.month, " out of range. Must be in range 1 ... 12")

        self.name = name
        self.month = month
        self.year = year

    def getName(self):
        return self.name

    def getMonth(self):
        return self.month

    def getYear(self):
        return self.year

    def toString(self):
        print("Name: ", self.name, " joined in month ", self.month, " of ", self.year)