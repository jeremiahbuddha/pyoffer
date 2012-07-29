
class Mortgage(object):

    def __init__(self, value, interest_rate, percent_down, num_years):
        self.VALUE = value
        self.RATE = interest_rate
        self.PERCENT_DOWN = percent_down
        self.NUM_YEARS = num_years
        self._principal = value*(1. - percent_down)
        self._down_payment = value - self._principal
        self._closing_costs = 0.03 * self._principal

    def get_total_down(self):
        return self._down_payment + self._closing_costs

    def get_monthly_payment(self):
        principal = self.VALUE * ( 1. - self.PERCENT_DOWN)
        interest = self.RATE / (100. * 12.)
        num_payments = 12. * self.NUM_YEARS
        monthly_payment = principal * (interest / 
                              (1. - (1. + interest) ** (-num_payments)))
        return monthly_payment        

