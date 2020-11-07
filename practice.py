class BankAccount:
    def deposit(self):
        self.cash += self.cash

    def withdraw(self):
        self.cash -= self.cash
        print(f"Remaining balance is: {self.cash}")
