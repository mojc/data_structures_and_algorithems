from R2_5 import CreditCard

class DirectCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, balance=0):
        super().__init__(self, customer, bank, acnt, limit)