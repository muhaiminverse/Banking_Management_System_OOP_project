from Admin import Admin
from Users import User

def main():
    print('User ----------------------------- \n')
# User ------------------------------------------
    korim = User('Korim Ahmend')
    jorim = User('jorim Ahmend')

    #Creating account
    korim.add_account(korim)
    jorim.add_account(jorim)

    print('Balance after deposit ------ \n')
    # Depositing
    korim.deposit(200)
    jorim.deposit(500)

    #showing balance
    print(f' Bank balance Korim: { korim.availavlbe_balance} BDT')
    print(f' Bank balance Jorim {jorim.availavlbe_balance} BDT')
    print('\n')


    print('Transfer ------ \n')
    # Transferring amount from korim to jorim
    korim.transfer(jorim, 100)

    #showing balance
    print(f' After Transfer Korim: { korim.availavlbe_balance} BDT')
    print(f' After Transfer Jorim {jorim.availavlbe_balance} BDT')
    print('\n')

    print('Loan ------ \n')
    # taking loan twice the amount 
    jorim.reqest_loan = 100
    print(f' After loan Jorim {jorim.availavlbe_balance} BDT')

    # taking loan more then twice the amount 
    jorim.reqest_loan = 3000
    print('\n')

    # 1st withdrawal account is 0 2nd withdrawal error message 
    print('Withdrawal ------ \n')
    korim.withdrawal(100)
    print(f' After withdrawal korim {korim.availavlbe_balance} BDT')
    korim.withdrawal(100)
    print('\n')

    print('Chacking History ------ \n')
    korim.check_history()
    jorim.check_history()
    print('\n')


    print('Admin ----------------------------- \n')

# Admin ------------------------------------------
    rafiq = Admin('jorim Ahmend')

    rafiq.print_Bank_balance
    rafiq.print_loan


if __name__ == '__main__':
    main()