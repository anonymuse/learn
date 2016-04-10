class Worker:
    def __init__(self, name, pay):
            self.pay = pay
            self.name = name

    def lastName(self):
            return self.name.split(' ')[-1]

    def giveRaise(self, percent):
            self.pay *= float( percent + 100 ) / 100
            return self.pay

