
class Address(object):
    def __init__(self, street, city, state_abbrv, zipcode):
        self.STREET = street
        self.CITY = city
        self.STATE_ABBRV = state_abbrv.upper()
        self.ZIPCODE = zipcode

    def __str__(self):
        return "{0}, {1}, {2}, {3}".format(self.STREET, self.CITY, 
            self.STATE_ABBRV, self.ZIPCODE)

class Property(object):

    def __init__(self, address, num_units, asking_price, rent_per_unit):
        self.ADDRESS = address
        self.NUM_UNITS = num_units
        self.ASKING_PRICE = asking_price
        self.RENT_PER_UNIT = rent_per_unit

    def print_info(self):
        print "Address:\t{0}\nAsking Price:\t{1}".format(self.ADDRESS, self.ASKING_PRICE) 
        print "Num Units:\t{0}\nRent Per Unit:\t{1}".format(self.NUM_UNITS,self.RENT_PER_UNIT)
