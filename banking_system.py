class User():
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def user_detail(self):
        print("User name", self.name)
        print("Age", self.age)
        print("Phone", self.phone)


class hdfc_bank(User):
    def __init__(self, name, age, phone):
        super().__init__(name, age, phone)
        self.bank_balance = 0

    def deposit_amount(self, amount):
        self.bank_balance = self.bank_balance + amount
        print(f"{amount} has been deposited")
        print(f"your bank balance is {self.bank_balance}")

    def withdraw_amount(self, amount):
        if amount > self.bank_balance:
            print("your bank balance is not sufficient")
            print(f"your bank balance is {self.bank_balance}")
        else:
            self.bank_balance = self.bank_balance - amount
            print(f"{amount} has been debited")
            print(f"your bank balance is {self.bank_balance}")

    def view_bank_details(self):
        self.user_detail()
        print(f"your bank balance is {self.bank_balance}")


output = hdfc_bank("Brynold", 20, 7879878)
output.deposit_amount(1000)
print("----------")
output.withdraw_amount(100)
print("----------")
output.view_bank_details()
