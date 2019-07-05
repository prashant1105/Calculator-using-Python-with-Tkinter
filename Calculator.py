#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 10:23:56 2019

@author: prashantpk
"""



from tkinter import *  # tkinter is used for GUI designing in Python...
class Calculator:
    
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator") # To give a name to the window...
        self.root.minsize(400, 400)   # To fix the minimum size of the window...
        self.root.maxsize(400, 400)   # To fix the maximum size of the window...
        self.result = Label(self.root, text = "", width = 60, height = 5, bg = "white")
        self.result.grid(row=0, column=0, columnspan = 4)
        
        # First Row Buttons...
        Button(self.root, text="1", width=10, height=5, bg="pink", command = lambda : self.get_num("1")).grid(row=1, column=0)
        Button(self.root, text="2", width=10, height=5, bg="blue", command = lambda : self.get_num("2")).grid(row=1, column=1)
        Button(self.root, text="3", width=10, height=5, bg="pink", command = lambda : self.get_num("3")).grid(row=1, column=2)
        Button(self.root, text="+", width=10, height=5, bg="blue", command = lambda : self.get_operator("+")).grid(row=1, column=3)
        
        # Second Row Buttons...
        Button(self.root, text="4", width=10, height=5, bg="pink", command = lambda : self.get_num("4")).grid(row=2, column=0)
        Button(self.root, text="5", width=10, height=5, bg="blue", command = lambda : self.get_num("5")).grid(row=2, column=1)
        Button(self.root, text="6", width=10, height=5, bg="pink", command = lambda : self.get_num("6")).grid(row=2, column=2)
        Button(self.root, text="-", width=10, height=5, bg="blue", command = lambda : self.get_operator("-")).grid(row=2, column=3)
        
        # Third Row Buttons...
        Button(self.root, text="7", width=10, height=5, bg="pink", command = lambda : self.get_num("7")).grid(row=3, column=0)
        Button(self.root, text="8", width=10, height=5, bg="blue", command = lambda : self.get_num("8")).grid(row=3, column=1)
        Button(self.root, text="9", width=10, height=5, bg="pink", command = lambda : self.get_num("9")).grid(row=3, column=2)
        Button(self.root, text="*", width=10, height=5, bg="blue", command = lambda : self.get_operator("*")).grid(row=3, column=3)
        
        # Fourth Row Buttons...
        Button(self.root, text="0", width=10, height=5, bg="pink", command = lambda : self.get_num("0")).grid(row=4, column=0)
        Button(self.root, text="/", width=10, height=5, bg="blue", command = lambda : self.get_operator("/")).grid(row=4, column=1)
        Button(self.root, text="C", width=10, height=5, bg="pink", command = lambda : self.clear()).grid(row=4, column=2)
        Button(self.root, text="=", width=10, height=5, bg="blue", command = lambda : self.get_result()).grid(row=4, column=3)
        self.root.mainloop()
        
    def get_num(self, number):
        new = self.result['text'] + number
        self.result.configure(text=new)
        
    def get_operator(self, operator):
        self.first_number = int(self.result['text'])
        self.result.configure(text = "")
        self.operator = operator
        
    def clear(self):
        self.result.configure(text = "")
        
    def get_result(self):
        self.second_number = int(self.result['text'])
        
        if (self.operator == "+"):
            self.result.configure(text = str(self.first_number + self.second_number))
            
        elif (self.operator == "-"):
            self.result.configure(text = str(self.first_number - self.second_number))
            
        elif(self.operator == "*"):
            self.result.configure(text = str(self.first_number * self.second_number))
            
        else:
            if self.second_number == 0:
                self.result.configure(text = "Wrong Entry")
            else:
                self.result.configure(text = str(self.first_number / self.second_number))
        
obj = Calculator()