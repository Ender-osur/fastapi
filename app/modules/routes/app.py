from enum import Enum
from fastapi import APIRouter, Depends
from .strategy import PaymentStrategy, CreditCardPayment, PayPalPayment, BitcoinPayment, PsePayment, MercadoPagoPayment


class Payment(Enum):
    CREDIT_CARD = "credit_card"
    PAYPAL = "paypal"
    BITCOIN = "bitcoin"
    PSE = "pse"
    MERCADOPAGO = "mercadopago"


def get_strategy(typeOfPayment: Payment) -> PaymentStrategy:
    defined_payments = {
        Payment.CREDIT_CARD: CreditCardPayment(),
        Payment.PAYPAL: PayPalPayment(),
        Payment.BITCOIN: BitcoinPayment(),
        Payment.PSE: PsePayment(),
        Payment.MERCADOPAGO: MercadoPagoPayment(),
    }
    return defined_payments[typeOfPayment]

router = APIRouter()

@router.get("/process_payment")
def process_payment(amount: float, typeOfPayment: PaymentStrategy = Depends(get_strategy)) -> dict:
    return {"status": typeOfPayment.process_payment(amount = amount)}

@router.get("/calculate_fees")
def calculate_fees(amount: float, typeOfPayment: PaymentStrategy = Depends(get_strategy)) -> float:
    return typeOfPayment.calculate_fees(amount = amount)

@router.get("/validate_transaction")
def validate_transaction(transaction_id: str, typeOfPayment: PaymentStrategy = Depends(get_strategy)) -> bool:
    return typeOfPayment.validate_transaction(transaction_id = transaction_id)
