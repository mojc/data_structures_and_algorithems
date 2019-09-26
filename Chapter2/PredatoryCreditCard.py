# C-2.28
from R2_5 import CreditCard

class PredatoryCreditCard(CreditCard):
    def __init__(self, costumer, bank, acnt, limit, apr):
        super().__init__(costumer, bank, acnt, limit)
        self._apr = apr
        self._month_charge_count = 0
        self._min_month_payment = 0
        self._percent = 0.1
        self._late_fee = 5

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        if success:
            self._month_charge_count +=1
            if self._month_charge_count > 10:
                self._balance -= 1
        return success

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
        if self._min_month_payment > 0:
            self._balance -= self._late_fee
        if self._balance > 0:
            self._min_month_payment = self._balance * self._percent
        
        self._month_charge_count = 0

print(PredatoryCreditCard('m', 'n', 123, 100, 10))