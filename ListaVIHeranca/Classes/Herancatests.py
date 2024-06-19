import unittest
from Classes.Local_loan import LocalLoan
from Classes.International_loan import InternationalLoan

class TestLoanCalculations(unittest.TestCase):

    def test_local_loan_single_payment(self):
        local_loan = LocalLoan(customer="Carlos",value=10000, interestRate=0.05, installments=1, inflationRate=0.02)
        expected_total = 10000 * (1 + 0.05 + 0.02)
        result = local_loan.getTotalLoan()
        assert expected_total == result, \
        f"Erro no cálculo de empréstimo nacional com pagamento único. Esperado: {expected_total}, Obtido: {result}"

    def test_local_loan_installments(self):
        local_loan = LocalLoan(customer="Carlos",value=10000, interestRate=0.05, installments=12, inflationRate=0.02)
        expected_total = 10000 * (1 + 0.05 + 0.02) ** 12
        result = local_loan.getTotalLoan()
        assert expected_total == result, \
        f"Erro no cálculo de empréstimo nacional parcelado. Esperado: {expected_total}, Obtido: {result}"

    def test_international_loan_single_payment(self):
        international_loan = InternationalLoan(customer="Carlos",value=10000, interestRate=0.05, installments=1, exchangeRate=5.0,
                                               transactionFee=0.01)
        expected_total = 10000 * 5.0 * (1 + 0.05 + 0.01)
        result = international_loan.getTotalLoan()
        assert expected_total == result, \
        f"Erro no cálculo de empréstimo internacional com pagamento único. Esperado: {expected_total}, Obtido: {result}"

    def test_international_loan_installments(self):
        international_loan = InternationalLoan(customer="Carlos",value=10000, interestRate=0.05, installments=12, exchangeRate=5.0, transactionFee=0.01)
        expected_total = 10000 * 5.0 * (1 + 0.05 + 0.01) ** 12
        result = international_loan.getTotalLoan()
        assert expected_total == result,\
        f"Erro no cálculo de empréstimo internacional parcelado. Esperado: {expected_total}, Obtido: {result}"

    def test_local_loan_value_installment_delayed(self):
        local_loan = LocalLoan(customer="Carlos",value=10000, interestRate=0.05, installments=1, inflationRate=0.02)
        delayed = True
        days = 10
        expected_value = 10000 * (days * (10000 * 0.05))
        result = local_loan.value_installment(delayed=delayed, days=days)
        assert expected_value == result,\
        f"Erro no cálculo de parcela com atraso para empréstimo nacional. Esperado: {expected_value}, Obtido: {result}"

    def test_international_loan_value_installment_delayed(self):
        international_loan = InternationalLoan(customer="Carlos",value=10000, interestRate=0.05, installments=1, exchangeRate=5.0, transactionFee=0.01)
        delayed = True
        days = 10
        expected_value = 10000 * (days * (10000 * 0.05))
        result = international_loan.value_installment(delayed=delayed, days=days)
        assert expected_value == result,\
        (f"Erro no cálculo de parcela com atraso para empréstimo internacional. Esperado: {expected_value}, Obtido: {result}")

if __name__ == '__main__':
    unittest.main()

