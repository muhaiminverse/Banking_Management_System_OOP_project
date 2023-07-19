from Bank import Bank
from Create_account import Create_account

# Admin Account ------
class Admin(Create_account , Bank):
    
    admin_accounts = []
    def __init__(self, name):
        super().__init__(name)

    @property
    def print_loan(self):
        print(f'Banks Loan: {self._loanAllowance}\n') 

    @property
    def print_Bank_balance(self):
        print(f'Banks Balance: {self._Bank_vault}\n') 
        

    def turn_of_loan(self , value):
        if(value == 1):
            self.off = 1
        elif(value == 0):
            self.off = 0
            
    