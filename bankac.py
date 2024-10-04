class BankAccount:
    interest_rate = 0.05  

    def __init__(self, account_holder):
        self.account_holder = account_holder  
        self.balance = 0  

    def deposit(self, amount):
        """Adds the amount to the balance."""
        self.balance += amount

    def withdraw(self, amount):
        """Subtracts the amount from the balance if there are sufficient funds."""
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def apply_interest(self):
        """Adds interest to the current balance based on the class variable interest_rate."""
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest

    def display_account_info(self):
        """Displays the account holder's name and the current balance."""
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance:.2f}")

account1 = BankAccount("Okolimo Joseph")
account2 = BankAccount("Winnie Asio")


account1.deposit(1000)
account1.withdraw(500)
account2.deposit(2000)
account2.withdraw(1000)

account1.apply_interest()
account2.apply_interest()


print("Account 1 Information:")
account1.display_account_info()
print("\nAccount 2 Information:")
account2.display_account_info()