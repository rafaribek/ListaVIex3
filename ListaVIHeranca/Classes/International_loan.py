from Loan import Loan

class InternationalLoan(Loan):
    def __init__(self, customer, value, interestRate, installments, exchangeRate, transactionFee):
        super().__init__(customer, value, interestRate, installments)
        self.exchangeRate = exchangeRate
        self.transactionFee = transactionFee

    def getTotalLoan(self):
        if self.installments == 1:
            total = self.value * self.exchangeRate * (1 + self.interestRate + self.transactionFee)
        else:
            total = self.value * self.exchangeRate * (1 + self.interestRate + self.transactionFee) ** self.installments
        return total


