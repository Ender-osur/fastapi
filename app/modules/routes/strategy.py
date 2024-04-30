from abc import ABC, abstractmethod

"""
En este caso tenemos una tienda Online que vende licencias de software que recibe tres tipos de pagos:
1. Tarjeta de crédito
2. Paypal
3. Bitcoin
4. PSE
5. MercadoPago
"""


class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass

    @abstractmethod
    def calculate_fees(self, amount: float) -> float:
        pass

    @abstractmethod
    def validate_transaction(self, transaction_id: str) -> bool:
        pass


class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount: float) -> str:
        print(f"Processing credit card payment for {amount}")

    def calculate_fees(self, amount: float) -> float:
        return round(amount * 0.02, 2)

    def validate_transaction(self, transaction_id: str) -> bool:
        print(f"Validating transaction {transaction_id}")
        return True


class PayPalPayment(PaymentStrategy):
    def process_payment(self, amount: float) -> None:
        print(f"Processing PayPal payment for {amount}")

    def calculate_fees(self, amount: float) -> float:
        return round(amount * 0.03, 2)

    def validate_transaction(self, transaction_id: str) -> bool:
        print(f"Validating transaction {transaction_id}")
        return True


class BitcoinPayment(PaymentStrategy):
    def process_payment(self, amount: float) -> None:
        print(f"Processing Bitcoin payment for {amount}")

    def calculate_fees(self, amount: float) -> float:
        return round(amount * 0.01, 2)

    def validate_transaction(self, transaction_id: str) -> bool:
        print(f"Validating transaction {transaction_id}")
        return True

class PsePayment(PaymentStrategy):
    def process_payment(self, amount: float) -> None:
        print(f"Processing Bitcoin payment for {amount}")

    def calculate_fees(self, amount: float) -> float:
        return round(amount * 0.01, 2)

    def validate_transaction(self, transaction_id: str) -> bool:
        print(f"Validating transaction {transaction_id}")
        return True

class MercadoPagoPayment(PaymentStrategy):
    def process_payment(self, amount: float) -> None:
        print(f"Processing Bitcoin payment for {amount}")

    def calculate_fees(self, amount: float) -> float:
        return round(amount * 0.01, 2)

    def validate_transaction(self, transaction_id: str) -> bool:
        print(f"Validating transaction {transaction_id}")
        return True
