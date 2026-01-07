'''
Natthida sriphan
663040479-3
P2
'''

from bank_account import BankAccount

john = BankAccount("John", "saving", 500)
tim = BankAccount("Tim", "loan", -1000000)
sarah = BankAccount("Sarah", "saving")

john.deposit(3000)
print(f"John balance: {john.get_balance():,}\n")

print(f"Tim loan: {tim.get_balance():,}")
tim.pay_loan((tim.get_balance()) / 2)
print(f"After payment: {tim.get_balance():,}\n")

sarah.deposit(50000000)
sarah_loan = BankAccount("Sarah", "loan", -100000000)

john.print_customer()
print()