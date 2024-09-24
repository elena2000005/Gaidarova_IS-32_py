class Bank:
    def __init__(self, amount, interest_rate):
        self.amount = amount  # сумма денег на счету
        self.interest_rate = interest_rate  # годовая процентная ставка

    def calculate_interest(self):
        """Метод для вычисления процентных начислений"""
        interest = self.amount * (self.interest_rate / 100)
        return interest

    def withdraw(self, amount_to_withdraw):
        """Метод для снятия денег"""
        if amount_to_withdraw > self.amount:
            return "Недостаточно средств на счету."
        self.amount -= amount_to_withdraw
        return f"Вы сняли {amount_to_withdraw}. Остаток на счету: {self.amount}"

# Пример использования
bank_account = Bank(10000, 5.0)
print(f"Процентные начисления: {bank_account.calculate_interest()}")
print(bank_account.withdraw(2000))
