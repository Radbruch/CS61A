# -*- coding: utf-8 -*-
"""
Created on Sun May 23 22:52:48 2021

@author: Joyce
"""

class Account:
    interest = 0.02
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        else:
            self.balance = self.balance - amount
            return self.balance
        
class CheckingAccount(Account):
    '''A bank account that charges for withdrawals, and has lower interest rate'''
    withdraw_fee = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
    
class Bank:
    '''A bank *has* accounts
    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    '''
    def __init__(self):
        self.accounts = []
        
    def open_account(self, holder, amount, kind = Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account
    
    def pay_interest(self):
        for i in self.accounts:
            i.deposit(i.balance * i.interest)
            
    
        
        
        
        
        
        
        