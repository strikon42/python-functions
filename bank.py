#!/usr/bin/env python
# coding: utf-8

# In[25]:


class Account():
    def __init__(self,owner,balance=0):
        
        self.owner = owner
        self.balance = balance
    
    def deposit(self,dep_amt):
        
        self.balance = self.balance + dep_amt
        
        print(f"Added {dep_amt} to the balance")
        
    def withdeawal(self,wd_amount):
        
        if self.balance >= wd_amount:
            self.balace = self.balance - wd_amount
            
            print("Withdrawal accepted")
        else: 
            print("Sorry not enough funds!")
    def __str__(self):
        
        return f"Owner: {self.owner} /n Balance: {self.balace}"
    

