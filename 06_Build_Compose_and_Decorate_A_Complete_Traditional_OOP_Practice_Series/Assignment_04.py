class Bank:
    bank_name = "HBL"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

bank1 = Bank()
Bank.change_bank_name("state bank")
print(Bank.bank_name)