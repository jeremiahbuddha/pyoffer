
class Deal(object):

    def __init__(self, proprty, mortgage, target_ROI):
        self.proprty = proprty
        self.mortgage = mortgage
        # Make sure mortgage starts at asking price
        if self.mortgage.VALUE != self.proprty.ASKING_PRICE:
            print "WARNING: Initial mortgage size does not match asking price"
            print "for property in this deal. Mortgage is reset to asking"
            print "price."
            self.mortgage.VALUE = self.proprty.ASKING_PRICE
        self.ASKING_ROI = self.get_ROI(self.mortgage, self.proprty)
        self.TARGET_ROI = target_ROI

    def get_ROI(self, mortgage, proprty):
        money_down = mortgage.get_total_down()
        money_earned = proprty.get_monthly_income() * 12.0
        return money_earned / money_down
 
#    def get_montly_cashflow(self, mortgage, proprty):
#        prop
#        return proprty.get_monthly_income() - 
#
#    def get_offer_price(self):
#
#        for i in range(self.proprty.ASKING_PRICE):
#            offer = self.proprty.ASKING_PRICE - i
#            self.mortgage.VALUE -= i
#
#
#            money_earned = 12.0 * (monthly_income - monthly_expenses - new_mortgage)
#            this_money_down = (offer * percent_down + closing_costs)
#            this_ROI = money_earned / (this_money_down)
#            if (this_ROI - desired_ROI) * 100.0 > 0.001:
#                return offer, this_money_down, this_ROI, new_mortgage
#
#        print "No solution found!!"
#        print this_ROI, desired_ROI
#        print offer, this_money_down, this_ROI, new_mortgage
#        sys.exit()

