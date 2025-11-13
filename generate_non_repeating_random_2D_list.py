import random

#GNRR2DL => generate non repeating random 2d list
class GNRR2DL:
    def __init__(self,row,column):
        self.row = row
        self.column = column
        self.numbers = []

    def exec(self):
        for i in range(self.row):
            for j in range(self.column):
                while True:
                    number = random.randint(1,self.row * self.column)
                    if number not in self.numbers:
                        self.numbers.append(number)
                        break
        return self.numbers