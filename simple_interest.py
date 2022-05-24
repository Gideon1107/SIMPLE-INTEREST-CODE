#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:31:27 2022

@author: gideon
"""
import sys

class s_interest():
    def __init__(self):
        self.p= int(input("Enter initial principal 'P': "))
        self.r= int(input("Enter annual interest rate 'r': "))
        self.t= int(input("Enter time in years 't': "))
        pass
        
    def operator(self):
        self.rrate = self.r/100
        self.rt = self.rrate*self.t
        self.onert = (1 + self.rt)
        self.famount = int(self.p*self.onert)
        self.interest = (self.p*self.r*self.t)//100
        print("Simple interest 'S.I' = ",self.interest)
        print("Total amount 'A': ",self.famount)
        print("\n")
        print("Do you want to calculate again?")
        opt = str(input("If Yes enter 'Y' if No enter 'N': \n"))
        if opt == "Y" or "y":
            self.__init__()
            self.operator()
        elif opt == "N" or "n":
            sys.exit()
        
m = s_interest()
m.operator()
