from Loan import Loan

class LocalLoan(Loan):
    def __init__(self, customer, value, interestRate, installments, inflationRate):
        super().__init__(customer, value, interestRate, installments)
        self.inflationRate = inflationRate

    def getTotalLoan(self):
        if self.installments == 1:
            total = self.value * (1 + self.interestRate + self.inflationRate)
        else:
            total = self.value * (1 + self.interestRate + self.inflationRate) ** self.installments
        return total




