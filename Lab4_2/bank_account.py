'''
Natthida sriphan
663040479-3
Bank Account
'''

class BankAccount:
    saving_run = 0
    loan_run = 0
    branch_number = 1724
    branch_name = "KKU Complex"

    def __init__(self, name, acc_type='saving', balance=0):
        self.name = name
        self.type = acc_type
        self.balance = balance

        if self.type == 'saving':
            BankAccount.saving_run += 1
            self.runing = f"{BankAccount.branch_number}-1-{BankAccount.saving_run}"
        else:
            BankAccount.loan_run += 1
            self.runing = f"{BankAccount.branch_number}-2-{BankAccount.loan_run}"

    def print_customer(self):
        print("----- Customer Record -----")
        print(f"Name: {self.name}")
        print(f"Account number: {self.runing}")
        print(f"Account type: {self.type}")
        print(f"Balance: {self.balance:,}")
        print("----- End Record -----")

    @classmethod
    def change_branch_name(cls, new_name):
        cls.branch_name = new_name

    def deposit(self, amount=0):
        if self.type == 'saving':
            self.balance += amount
        return self.balance

    def withdraw(self, amount=0):
        if self.type == 'saving':
            self.balance -= amount
        return self.balance

    def pay_loan(self, amount=0):
        if self.type == 'loan':
            self.balance += amount
        return self.balance

    def get_loan(self, amount=0):
        if self.type == 'loan' and self.balance >= -50000:
            self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    @staticmethod
    def calc_interest(bal, int_rate, payment):
        year = 1
        print("----- Loan Plan -----")
        while bal > 0:
            interest = bal * (int_rate / 100)
            loan = bal + interest
            pay = payment if loan > payment else loan
            bal = loan - pay

            print(
                f"Year {year}: loan = {loan:.2f}  "
                f"payment {pay:.2f}  bal = {bal:.2f}"
            )
            year += 1
        print("----- End Plan -----")
