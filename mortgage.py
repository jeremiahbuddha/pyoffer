
class Mortgage(object):

    def __init__(self, max_value, max_down_payment, interest_rate, num_years):
        self.VALUE = max_value
        self.MAX_VALUE = max_value 
        self.DOWN_PAYMENT = max_down_payment
        self.RATE = interest_rate
        self.PERCENT_DOWN = max_down_payment / max_value
        self.NUM_YEARS = num_years
        self._closing_costs = 0.03 * self.VALUE

    def reset_value_from_asking_price(self,ask_price):
        self.VALUE = ask_price * (1.0 - self.PERCENT_DOWN)
        self.DOWN_PAYMENT = ask_price * self.PERCENT_DOWN
        self._closing_costs = 0.03 * self.VALUE

    def get_total_down(self):
        return self.DOWN_PAYMENT + self._closing_costs

    def get_monthly_payment(self):
        principal = self.VALUE
        interest = self.RATE / (100. * 12.)
        num_payments = 12. * self.NUM_YEARS
        monthly_payment = principal * (interest / 
                              (1. - (1. + interest) ** (-num_payments)))
        return monthly_payment        

