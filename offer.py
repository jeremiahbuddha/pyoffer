#! /Library/Frameworks/Python.framework/Versions/Current/bin/python

import sys

def get_mortgage_payment(principal,rate,num_payments):
    interest = rate / (100. * 12.)
    payment = principal * (interest / (1. - (1. + interest) ** (-num_payments)))
    return payment

def get_offer_price(monthly_income, monthly_expenses, asking_price, 
                    desired_ROI, percent_down, interest_rate, closing_costs):
    for i in xrange(100000):
        offer = asking_price - i
        new_mortgage = get_mortgage_payment(offer * (1.0 - percent_down),
                 interest_rate, 30.0 * 12.0)
        money_earned = 12.0 * (monthly_income - monthly_expenses - new_mortgage)
        this_money_down = (offer * percent_down + closing_costs)
        this_ROI = money_earned / (this_money_down)
        if (this_ROI - desired_ROI) * 100.0 > 0.001:
            return offer, this_money_down, this_ROI, new_mortgage

    print "No solution found!!"
    print this_ROI, desired_ROI
    print offer, this_money_down, this_ROI, new_mortgage
    sys.exit()

### ============================================================================
### ============================================================================
### Cashflow inputs
NUM_UNITS = 6
MONTLY_RENT = 475.0
DESIRED_ROI = 0.50

ASKING_PRICE = 199000
INTEREST_RATE = 0.05
PERCENT_DOWN = 0.25
CLOSING_COSTS = ASKING_PRICE * 0.03
### ============================================================================

# Get monthly income
m_income = NUM_UNITS * MONTLY_RENT

# Get monthly expenses
m_mortgage = get_mortgage_payment(ASKING_PRICE * (1.0 - PERCENT_DOWN),
                 INTEREST_RATE, 30.0 * 12)
m_insurance = 0.08 * m_mortgage
m_tax = 600.0 #0.12 * m_mortgage
m_managment = 0.08 * m_mortgage
m_expenses = m_insurance + m_tax + m_managment
tot_m_expenses = m_expenses + m_mortgage

# Get yearly ROI
money_down = ASKING_PRICE * PERCENT_DOWN + CLOSING_COSTS
money_earned = 12.0 * (m_income - tot_m_expenses)
asking_ROI = money_earned / money_down


print "### ======================================\n"
print "Asking:\n Price: {0}\n Down Payment: {1}\n ROI: {2}".format(
       ASKING_PRICE, money_down, asking_ROI)
print "Cashflow: {0}".format(m_income - tot_m_expenses)

if (asking_ROI < DESIRED_ROI):
    offer, this_money_down, this_ROI, new_mortgage = get_offer_price(m_income, m_expenses, ASKING_PRICE,
                      DESIRED_ROI, PERCENT_DOWN, INTEREST_RATE, CLOSING_COSTS)
    print "### ======================================\n"
    print "Offer Analysis:\n Suggested offer {0}\n Down Payment: {1}\n ROI: {2}".format(
           offer, this_money_down, this_ROI)

