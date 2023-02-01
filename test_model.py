
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
    setup={ id: sim_id
            meta: {start_year: #, end_year: #, sim_length: #, retirement_year: # }
            balance_sheet:{
                2015: 
                    {income:[
                        {income_source1: #, employer:xxx},
                        {income_source2: #}
                        ],
                    expenses:[],
                    assets:[]
                    }
                
            }
          }
    """
    # setup up the above structure first
    
    def __init__(self):
        self.sim_id = next(self.simulation_id)
        self.setup = {}

    def init(self, start_year, retirement_year, sim_length ):
        self.setup['id'] = self.sim_id
        self.setup['balance_sheet']={}
        self.setup['meta']={}
        self.setup['meta']['start_year'] = start_year
        self.setup['meta']['end_year'] = start_year + sim_length
        self.setup['meta']['simulation_length'] = sim_length
        self.setup['meta']['retirement_year'] = retirement_year

        for i in range(sim_length):
            balance_sheet_dict={}
            balance_sheet_dict['income']=[]
            balance_sheet_dict['expenses']=[]
            balance_sheet_dict['assets']=[]

            year = start_year+i
            self.setup['balance_sheet'][year]=balance_sheet_dict

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

        def __init__(self, employer, monthly_income, hire_year, growth):
            self.income_id = f"i{next(self.income_id)}"
            self.employer = employer
            self.monthly_income = monthly_income

            # # calc income per year
            # for i in len(self.setup['simulation_length']):
            #     if (i <= hire_year - self.setup['start_year'] ):
            #         annual_income = 0
            #     else:
            #         annual_income = (monthly_income*12)*(1+growth)^(hire_year - (i + self.setup['start_year']))
            #         self.setup['balance_sheet'].where(eoy == (i + self.setup['start_year']))
        def update_income(self, new_income):
            self.monthly_income = new_income