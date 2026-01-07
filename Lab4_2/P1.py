'''
Natthida sriphan
663040479-3
P1
'''

from bank_account import BankAccount
acc1 = BankAccount("Alice", "saving", 1000)
acc2 = BankAccount("Bob", "saving", 500)

loan1 = BankAccount("Charlie", "loan", 10000)

acc1.deposit(500)
acc1.withdraw(200)

loan1.get_loan(2000)
loan1.pay_loan(1500)

acc1.print_customer()
acc2.print_customer()
loan1.print_customer()

BankAccount.change_branch_name("Central Plaza")
print("New branch name:", BankAccount.branch_name)

BankAccount.calc_interest(1000, 5, 100)
