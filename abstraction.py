from abc import ABC, abstractmethod
class payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def get_method(self):
        pass

    @abstractmethod
    def process(self):
        pass

    def receipt(self):
        print(f"Payment of {self.amount} via {self.get_method()} processed.")

class creditcard(payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def process(self):
        print(f"Processing credit card payment of {self.amount} on card {self.card_number}")

    def get_method(self):
        return "Credit Card"

class upi(payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    def process(self):
        print(f"Processing UPI payment of {self.amount} to {self.upi_id}")

    def get_method(self):
        return "UPI"

class netbanking(payment):
    def __init__(self, amount, bank_name):
        super().__init__(amount)
        self.bank_name = bank_name

    def process(self):
        print(f"Processing net banking payment of {self.amount} via {self.bank_name}")

    def get_method(self):
        return "Net Banking"

c = creditcard(500, "124-678")
u = upi(600, "idk@tr")
n = netbanking(700, "SBI")

c.process()
c.receipt()
u.process()
u.receipt()
n.process()
n.receipt()