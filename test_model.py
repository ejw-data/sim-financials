
from time_value import *
import itertools

class estimator:

    # collect basic info
    # sim_length = input('How many years should be simulated?  ')
    # sim_start_year = input('What year is the initial year?  ')

    # sim identifier
    simulation_id = itertools.count()


    # used to collect instance settings
    inputs = []
    # [{step: init, param: ()}, {step: add_income, param: ()}, {step: add_house, param: ()}]
    # used to collect summarized results of each test
    results = []

    """
    https://www.geeksforgeeks.org/how-to-create-a-list-of-object-in-python-class/
    setup={l:v, k:v, 
            balance_sheet:[
                {year: 2015, 
                 income:[
                    {income_source1: #, id},
                    {income_source2: #}
                 ]
                }
            ]
          }
    """
    def __init__(self):
        self.sim_id = next(self.simulation_id)
        self.setup = {}

    def init(self, start_year, retirement_year, sim_length ):
        self.setup['id'] = self.sim_id
        self.setup['start_year'] = start_year
        self.setup['end_year'] = start_year + sim_length
        self.setup['simulation_length'] = sim_length
        self.setup['retirement_year'] = retirement_year

    def add_inputs(self, parameters):
        self.inputs.append(parameters)

    def add_results(self, totals):
        self.results.append(totals)


    def print_setup(self):
        print(self.setup)

    # INCOME ---------------------------
    
    def add_income(self, base, growth, start_year):
        """
        Function used to add recurring income like a salary
        Do I need to make this an object for tracking
        """
        self.income_source(25000)

        return [ base*(1+growth)^i for i in range(len(self.setup['retirement_year'] - start_year))]
    
    def one_off_income():
        return 10000
    
    def update_income(self, base, growth, start_year):
        return 1
    
    def remove_income():
        return 1

    # EXPENSES  ---------------------------
    
    # APARTMENT Rental Calcs
    def add_apartment():
        return 1

    
    # INNER CLASSES  ---------------------------
    class income_source():
        """
        Stores income source id and salary and method of updating
        Hopefully an easy way of accessing
        """
        income_id = itertools.count()

        def __init__(self, monthly_income):
            self.income_id = f"i{next(self.income_id)}"
            self.monthly_income = monthly_income
        
        def update_income(self, new_income):
            self.monthly_income = new_income