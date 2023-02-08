# https://www.yahoo.com/finance/news/housing-heres-what-it-will-take-to-buy-a-home-this-year-165050707.html
# functionality:
#    1.  buy car include maintenance
#    2.  sell car
#    3.  
#    x4.  buy house 
#    4.  house maintenance
#    5.  sell house
#    6.  
#    x7.  rent apartment
#    8.  save retirement 401K (index fund)
#    9.  save retirement bond
#   10.  buy investment property
#   11.  rent investment property
#   12.  Children birth/early years
#   x12.  Children college
#   12.  Children safety net
#   13.  move to new city
#   14.  taxes
#   x15.  food and groceries
#   x16.  cell phone
#   x17.  pets
#   x18.  entertainment
#   19.  public transportation
#   20.  health insurance
#   21.  education expenses
#   22.  education loan expenses
#   x23.  side hustle income (one-off() or income())
#   24.  

from time_value import *
import itertools

class estimator:

    # used to collect instance settings
    params = []
    # used to collect summarized results of each test
    results = []

    def __init__(self):
        self.setup = {}
        self.monthly_flows = {}

    def init(self, year):
        self.setup['year'] = year

    def add_params(self, parameters):
        self.params.append(parameters)

    def add_results(self, totals):
        self.results.append(totals)

    # INCOME ---------------------------
    
    def add_income():
        """
        Function used to add recurring income like a salary
        Do I need to make this an object for tracking
        """
        return 1
    
    def one_off_income():
        return 1
    
    def update_income():
        return 1
    
    def remove_income():
        return 1

    # ASSETS ---------------------------
    # HOUSE Calcs
    def add_house(self, selling_price, downpayment, interst_rate, length_loan):
        # https://www.bankrate.com/mortgages/costs-of-buying-a-home/#ongoing
        
        initial_equity = downpayment
        loan_amount = selling_price - downpayment
        annuity = pv_an(loan_amount,interst_rate,12,length_loan)
        annuity_monthly = [annuity for i in range(12*length_loan)]
        equity_monthly = [selling_price/(length_loan*12) for i in range(12*length_loan)]
        interst_expense_monthly = [annuity_monthly[0]/equity_monthly[0] for i in range(12*length_loan)]
        equity_monthly[0] = equity_monthly[0] + initial_equity
        return (equity_monthly, annuity_monthly, interst_expense_monthly)

    def sell_house():
        # real estate commission - 5-6%
        # only 10% of home were sold FSBO and for less ($105K differential)
        # closing costs - $6905 - common seller’s costs may include HOA fees, a pre-listing inspection, 
        #    recording and settlement fees and title insurance.
        # https://www.bankrate.com/real-estate/how-much-does-it-cost-to-sell-house/#unavoidable
        # Capital Gains Tax excluding the first $250,000 if not sold another property within 2 years
        # transfer tax, mansion tax, luxory tariff 
        # moving costs - $911 - $2514
        # if older home then home waranty insurance
        return 1
    
    # CARS Ownership Calcs
    def add_vehicle(purchase_year, vehicle_year, model, type, loan):
        # year, age of vehicle, model, 
        # 

        # ml:  how long before not operatable
        return 1
    
        # RETIREMENT Calcs
    def add_401k():
        """
        No need to calculate withdrawal
        """

        # calc PV - probably don't need
        # calc FV
        # do I need to calculated just with for loop
        return 1
    
    def add_stock():
        return 1
    
    def add_bond(principle, coupon_rate, annual_compounding_terms, term):
        increased_value_per_compound_period = principle*(coupon_rate/annual_compounding_terms)
        n_periods = annual_compounding_terms*term

        # present_value
        # future_value at maturation
        # add to an ongoing tracker
        # should I calculate all values at once or calculate year-by-year
        return 1
    

    # EXPENSES  ---------------------------
    
    # APARTMENT Rental Calcs
    def add_apartment():
        return 1
    
    # INCOME TAXES
    # probably need to make this a function of each income
    # and track as a class variable
    

    # GENERAL Calcs

    
    # INNER CLASSES  ---------------------------
    class income_source():
        """
        Stores income source id and salary and method of updating
        Hopefully an easy way of accessing
        """
        unique_id = itertools.count()

        def __init__(self, monthly_income):
            self.income_id = next(self.unique_id)
            self.monthly_income = monthly_income

        def update_income(self, new_income):
            self.monthly_income = new_income