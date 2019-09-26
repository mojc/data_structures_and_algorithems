class CreditCard:
    def __init__(self, customer, bank, acnt, limit, balance=0):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_acnt(self):
        return self._acnt
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance

    def charge(self, price):
        try:
            float(price)
        except (ValueError, TypeError, NameError):
            print('did not enter numeric value')
            raise

        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        try:
            float(amount)
        except:
            print('did not enter numeric value')
            raise
        if amount < 0:
            raise ValueError("can't make negative payment")
        self._balance -= amount

if __name__ == "__main__":
    my_card = CreditCard('M', 'nlb', '111', 200)
    print(my_card.get_balance())
    your_card = CreditCard('b', 'n', '2333', 100, 40)
    print(your_card.get_balance())
    your_card.get_balance()
    my_card.make_payment(100)
    #my_card.make_payment('a')
    #my_card.make_payment(-100)