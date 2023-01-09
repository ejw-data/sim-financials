from time_value import *
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
    

    
