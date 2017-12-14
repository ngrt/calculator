from tinker import *

#master object = the frame
master = Tk()

#textbox displaying the calculation
display = Entry(master, width = 11, justify = 'right', bd = 0, bd = 'lightgrey')

#the windows name
master.title("Calculator")

class Calculator:
    def __init__(self):
        self.var1 = ""
        self.var2 = ""
        self.result = 0
        self.current = 0
        self.operator = 0

    def numb_butt(self, index):
        if self.current is 0:
            self.var1 = str(self.var1) + str(index)
            display.delete(0, END)
            display.insert(0, string=self.var1)
        else:
            self.var2 = str(self.var2) + str(index)
            display.delete(0, END)
            display.insert(0, string=self.var2)

    def equate(self):
        if self.operator is 0:
            self.result = float(self.var1) + float(self.var2)
        elif self.operator is 1:
                self.result = float(self.var1) - float(self.var2)
        elif self.operator is 2:
                self.result = float(self.var1) * float(self.var2)
        elif self.operator is 3:
                self.result = float(self.var1) / float(self.var2)
        display.delete(0, END)
        display.insert(0, string=self.result)
