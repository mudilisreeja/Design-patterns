from abc import ABC,abstractmethod
class PaymentStrategy(ABC):
    def pay(self,amount):
        pass
class CreditCardPayment(PaymentStrategy):
    def __init__(self,card_number,card_holder_name):
        self.card_number=card_number
        self.card_holder_name=card_holder_name
    def pay(self,amount):
        print(f"Paid {amount} using Credit Card. Card Holder: {self.card_holder_name}")
class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid {amount} using PayPal. Account Email: {self.email}")

class ShoppingCart:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def checkout(self, amount):
        self._strategy.pay(amount)
if __name__ == "__main__":
  credit_card_payment = CreditCardPayment("1234-5678-9012-3456", "John Doe")
  cart = ShoppingCart(credit_card_payment)
  cart.checkout(100)

# Change to PayPal
  paypal_payment = PayPalPayment("john.doe@example.com")
  cart.set_strategy(paypal_payment)
  cart.checkout(200)