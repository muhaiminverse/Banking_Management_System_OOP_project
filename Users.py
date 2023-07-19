from Bank import Bank
from Create_account import Create_account

#User Account ---------
class User(Create_account , Bank):
    accounts = []
    Transaction_history = {}

    def __init__(self, name) -> None:
        super().__init__(name)
        self.main_balance = 0

    def add_account(self, name):
        self.accounts.append(name)

    def check_history(self):
        print(f' Hisory of {self.name}: \n')
        for key, value in self.Transaction_history.items():
            print(key, value)

    def deposit(self, balance):
        self.main_balance += balance
        self.Transaction_history['deposit'] = balance
    
    def withdrawal(self, amount):
        if(amount>=self.main_balance):
            remaining = amount - self.main_balance
            availabel_amount = amount - remaining
            self.main_balance-=availabel_amount
            print(f'You can not get furture {remaining} BDT, 0 balance in account')
        else:
            if self._Bank_vault - amount  < 0 :
                print(' Bank is bankrupt ')
            else:
                self.main_balance-=amount
                self.Transaction_history['withdraw'] = amount


    @property
    def availavlbe_balance(self):
        return self.main_balance


    def transfer(self, transfer_to, amount):
        for account in self.accounts:
            if account.name == transfer_to.name:
                account.deposit(amount)
                self.withdrawal(amount)
                self.Transaction_history['transfer'] = amount

    @property
    def loan_grant(self):
         return self._loanAllowance 
    
    
    @loan_grant.setter
    def reqest_loan(self, amount):
         if(amount < self.main_balance * 2 ):
            self._loanAllowance -= amount
            self.main_balance += amount
            print(f'{self.name} current balance is {self.main_balance}')
       

