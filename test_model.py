
from time_value import *
import itertools
from datetime import datetime as dt
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
                        {amount: #, source:xxx},
                        {amount: #, source:xxx}
                        ],
                    expenses:[],
                    assets:[],
                    liabilities:[]
                    }
                
            }
          }
    """
    # setup up the above structure first
    
    def __init__(self):
        self.sim_id = next(self.simulation_id)
        self.setup = {}

    def __repr__(self) -> str:
        # in future put future value at retirement
        # should I use @dataclass to simplify things
        # https://www.youtube.com/watch?v=ojrbuVKblew
        # https://www.youtube.com/watch?v=Vj-iU-8_xLs
        # https://www.youtube.com/watch?v=RZPbPYM1HuE
        return f"Simulation ID: {self.sim_id}"

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
            balance_sheet_dict['liabilities']=[]

            year = start_year+i
            self.setup['balance_sheet'][year]=balance_sheet_dict

    def add_inputs(self, parameters):
        self.inputs.append(parameters)

    def add_results(self, totals):
        self.results.append(totals)


    def print_setup(self):
        print(self.setup)

    def print_income(self):
        income_dict={}
        start = self.setup['meta']['start_year']
        end = self.setup['meta']['end_year']
        for year in range(start, end):
            income_list = self.setup['balance_sheet'][year]['income']
            income_sum = 0
            for incomes in income_list:
                income_sum += incomes['amount']
            income_dict[year]= income_sum
        print(income_dict)

    def print_expenses(self):
        expenses_dict={}
        start = self.setup['meta']['start_year']
        end = self.setup['meta']['end_year']
        for year in range(start, end):
            expenses_list = self.setup['balance_sheet'][year]['expenses']
            expenses_sum = 0
            for expense in expenses_list:
                expenses_sum += expense['amount']
            expenses_dict[year]= expenses_sum
        print(expenses_dict)
    
    # INCOME ---------------------------
    
    def add_income(self, employer, base, growth, start_year):
        """
        Function used to add recurring income like a salary
        Do I need to make this an object for tracking
        """
        # self.income_source(employer, base)

        for i in range(start_year, self.setup['meta']['retirement_year'] + 1):
            income_record = {'source':employer, 'amount':round(base*(1+growth)**(i - start_year),2)}
            self.setup['balance_sheet'][i]['income'].append(income_record)

        # return [ base*(1+growth)^i for i in range(len(self.setup['retirement_year'] - start_year))]
    
    def one_off_income(self, description, amount, year):
        income_record = {'source':description, 'amount': amount}
        self.setup['balance_sheet'][year]['income'].append(income_record)
    
    def update_income(self, employer, base, growth, start_year):
        for i in range(start_year, self.setup['meta']['retirement_year'] + 1):
            work_experience = self.setup['balance_sheet'][i]['income']
            for j in range(len(work_experience)):
                if (work_experience[j]['source']==employer) and (base > 0):
                    work_experience[j]['amount'] = round(base*(1+growth)**(i - start_year),2)
                elif (work_experience[j]['source']==employer) and (base <= 0):
                    del work_experience[j]

    # EXPENSES  ---------------------------
    
    # GENERAL Expenses

    def add_general_expense(self, start_year, food=240, tech=35, pet=50):
        # personal items
        total = food + tech + pet
        annual_expense = total*12
        for year in range(start_year, self.setup['meta']['retirement_year'] + 1):
            expense_list = self.setup['balance_sheet'][year]['expenses']
            expense_list.append({'source':'general expense', 'amount': annual_expense})
      

    # APARTMENT Rental Calcs
    def add_apartment(self, monthly_amount, start_date, end_date ):
        start= dt.strptime(start_date, "%m/%Y")
        end = dt.strptime(end_date, "%m/%Y")

        if start.year != end.year:
            start_amount = (12- start.month)*monthly_amount
            end_amount = (end.month - 1)*monthly_amount
            annual_amount = monthly_amount*12
            years = range(start.year, end.year+1)
            for year in years:
                expense_list = self.setup['balance_sheet'][year]['expenses']
                if year == start.year:
                    expense_list.append({'source':'apartment rent', 'amount':start_amount})
                elif year == end.year:
                    expense_list.append({'source':'apartment rent', 'amount':end_amount})
                else:
                    expense_list.append({'source':'apartment rent', 'amount':annual_amount})
        else:
            annual_amount = (end.month - start.month-1)*monthly_amount
            year = start.year
            expense_list = self.setup['balance_sheet'][year]['expenses']
            expense_list.append({'source':'apartment rent', 'amount': annual_amount})

    # ASSETS
    # HOUSE Purchase
    def add_house(self, selling_price, down_payment, interest_rate, loan_term, start_year):
        principle= selling_price - down_payment
        # monthly mortgage payment
        mortgage_payment = pv_an(principle, interest_rate, 12, loan_term) 
        print('Mortgage: ', mortgage_payment)
        loan_end = start_year + loan_term
        sim_end = self.setup['meta']['end_year']
        end_year = sim_end if loan_end > sim_end else loan_end+1

        principle_component=0
        for year in range(start_year, end_year):
            interest_component=0
            

            for month in range(0,12):    
                interest_update = principle*(interest_rate/12)  
                interest_component += interest_update

                principle_update = mortgage_payment - interest_update
                principle_component += principle_update

                principle = principle - principle_update 
                print("Principle (", year, "/", month, ")", principle_update)
            
            expense_list = self.setup['balance_sheet'][year]['expenses']
            expense_list.append({'source':'mortgage interest', 'amount': round(interest_component,2)})

            expense_list = self.setup['balance_sheet'][year]['assets']
            expense_list.append({'source':'home equity', 'amount': round(principle_component,2)})

            expense_list = self.setup['balance_sheet'][year]['liabilities']
            expense_list.append({'source':'home principle', 'amount': round(principle,2)})

    
    
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