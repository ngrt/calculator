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
            self.