class Loan:
    def __init__(self, customer, value, interestRate, installments):
        self.customer = customer
        self.value = value
        self.interestRate = interestRate
        self.installments = installments

    def getTotalLoan(self):
        raise NotImplementedError("Este método deve ser sobrescrito nas subclasses")

    def value_installment(self, delayed=False, days=None):
        if delayed and days is not None:
            return self.value * (days * (self.value * self.interestRate))
        return self.value