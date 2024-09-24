import pickle

# Класс Bank для работы с банковским счетом
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

# Функция для сохранения объектов в файл
def save_def(objects, filename):
    with open(filename, 'wb') as file:
        pickle.dump(objects, file)
    print(f"Данные сохранены в файл {filename}")

# Функция для загрузки объектов из файла
def load_def(filename):
    with open(filename, 'rb') as file:
        objects = pickle.load(file)
    print(f"Данные загружены из файла {filename}")
    return objects

# Пример использования для класса Bank
bank1 = Bank(10000, 5.0)
bank2 = Bank(5000, 3.0)
bank3 = Bank(2000, 7.0)

# Сохранение объектов
banks = [bank1, bank2, bank3]
save_def(banks, 'bank_data.pkl')

# Загрузка объектов
loaded_banks = load_def('bank_data.pkl')
for bank in loaded_banks:
    print(f"Сумма: {bank.amount}, Процентная ставка: {bank.interest_rate}")
