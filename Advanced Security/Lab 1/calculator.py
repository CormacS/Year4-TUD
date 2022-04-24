from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Python Calculator")
        
        self.equation=Entry(master, width=45, borderwidth=5,fg='white', bg='black')

        self.equation.grid(row=0, column=0, columnspan=10)

        self.createButton()

    def createButton(self):
        button0 = self.add(0)
        button1 = self.add(1)
        button2 = self.add(2)
        button3 = self.add(3)
        button4 = self.add(4)
        button5 = self.add(5)
        button6 = self.add(6)
        button7 = self.add(7)
        button8 = self.add(8)
        button9 =  self.add(9)
        button_add = self.add('+')
        button_sub = self.add('-')
        button_mult = self.add('*')
        button_div = self.add('/')
        button_clear = self.add('c')
        button_equal = self.add('=')

        row1=[button7,button8,button9,button_add]
        row2=[button4,button5,button6,button_sub]
        row3=[button1,button2,button3,button_mult]
        row4=[button_clear,button0,button_equal,button_div]

        r=1
        for row in [row1, row2, row3, row4]:
            i=0
            for buttn in row:
                buttn.grid(row=r, column=i, columnspan=1,)
                i+=1
            r+=1

    def add(self,value):
        return Button(self.master, text=value, width=9,fg='white', bg='black', command = lambda: self.buttonClicked(str(value)))

    def buttonClicked(self, value):
        current_equation=str(self.equation.get())
        
        if value == 'c':
            self.equation.delete(-1, END)
        
        elif value == '=':
            answer = str(eval(current_equation))
            self.equation.delete(-1, END)
            self.equation.insert(0, answer)
        
        else:
            self.equation.delete(0, END)
            self.equation.insert(-1, current_equation+value)

if __name__=='__main__':
    
    root = Tk()
    
    my_gui = Calculator(root)
    
    root.mainloop()
