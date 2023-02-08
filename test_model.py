
from time_value import *
import itertools
from datetime import datetime as dt
class estimator:
    """
    Class used to estimate personal finances over many years.
    OOP style so many variations of the same model can be run
    and collected.
    """

    # sim identifier
    simulation_id = itertools.count()

    # used to collect instance settings and outcomes
    # for running many models with variations. Used in future version.
    inputs = []
    results = []

    def __init__(self):
        self.sim_id = next(self.simulation_id)
        self.setup = {}

    def __repr__(self) -> str:
        return f"Simulation ID: {self.sim_id}"

    def init(self, start_year, retirement_year, sim_length, start_savings ):
        self.start_savings = start_savings
        self.setup['id'] = self.sim_id
        self.setup['balance_sheet']={}
        self.setup['meta']={}
        self.setup['meta']['start_year'] = start_year
        self.setup['meta']['end_year'] = start_year + sim_length
        self.setup['meta']['simulation_length'] = sim_length
        self.setup['meta']['retirement_year'] = retirement_year

        for year in range(start_year, start_year+sim_length):
            balance_sheet_dict={}
            balance_sheet_dict['income']=[]
            balance_sheet_dict['expenses']=[]
            balance_sheet_dict['assets']=[]
            balance_sheet_dict['liabilities']=[]

            self.setup['balance_sheet'][year]=balance_sheet_dict

            # set initial savings information; note: this structure is different than income/expenses
            if year == start_year:
                self.setup['balance_sheet'][year]['assets'].append({'savings': start_savings})
            else:
                self.setup['balance_sheet'][year]['assets'].append({'savings': 0})

    # ADD model inputs/results to list
    def add_inputs(self, parameters):
        self.inputs.append(parameters)

    def add_results(self, totals):
        self.results.append(totals)

    # PRINT model contents
    def print_setup(self):
        print(self.setup)

    def print_income(self):
        income_dict={}
        start = self.setup['meta']['start_year']
        end = self.setup['meta']['end_year']
        for year in range(start, end):
            income_sum = self.sum_parameters('income', year)
            income_dict[year]= income_sum
        print(income_dict)

    def print_expenses(self):
        expenses_dict={}
        start = self.setup['meta']['start_year']
        end = self.setup['meta']['end_year']
        for year in range(start, end):
            expenses_sum = self.sum_parameters('expenses', year)
            expenses_dict[year]= expenses_sum
        print(expenses_dict)

    def sum_parameters(self, type, year):
        param_list = self.setup['balance_sheet'][year][type]
        param_sum = 0
        for param in param_list:
            param_sum += param['amount']
        return param_sum
        
    def balance_sheet_search(self, year, type, key):
        current_savings = self.setup['balance_sheet'][year][type]
        for index in range(len(current_savings)):
            if key in current_savings[index].keys():
                break
        return current_savings[index]
    
    def update_savings(self):
        start_year = self.setup['meta']['start_year']
        end_year = self.setup['meta']['end_year']

        for year in range(start_year, end_year):

            # more explicit cal using starting savings
            if year == start_year:
                past_savings = {'savings': self.start_savings}
            else:
                past_savings = self.balance_sheet_search(year-1, 'assets', 'savings')
            
            # set location of savings info
            current_savings = self.balance_sheet_search(year, 'assets', 'savings')
            
            # calc past savings + all income - all expenses in a year
            income = self.sum_parameters("income", year)
            expenses = self.sum_parameters("expenses", year)
            current_savings['savings'] = round(past_savings['savings'] + income - expenses, 2)
            # print("Savings (", year, "): ", past_savings['savings'], income, expenses )

    # INCOME ---------------------------
    
    def add_income(self, employer, base, growth, start_year):
        """
        Function used to add recurring income like a salary
        """
        total = 0
        for year in range(start_year, self.setup['meta']['retirement_year'] + 1):
            amount = round(base*(1+growth)**(year - start_year),2)
            total += amount
            income_record = {'source':employer, 'amount':amount}
            self.setup['balance_sheet'][year]['income'].append(income_record)
        
        # after updating income or expenses then run savings update    
        self.update_savings()
    
    def one_off_income(self, description, amount, year):
        income_record = {'source':description, 'amount': amount}
        self.setup['balance_sheet'][year]['income'].append(income_record)

        # after updating income or expenses then run savings update    
        self.update_savings()

    def update_income(self, employer, base, growth, start_year):
        for i in range(start_year, self.setup['meta']['retirement_year'] + 1):
            work_experience = self.setup['balance_sheet'][i]['income']
            for j in range(len(work_experience)):
                if (work_experience[j]['source']==employer) and (base > 0):
                    work_experience[j]['amount'] = round(base*(1+growth)**(i - start_year),2)
                elif (work_experience[j]['source']==employer) and (base <= 0):
                    del work_experience[j]
        
        # after updating income or expenses then run savings update    
        self.update_savings()

    # EXPENSES  ---------------------------
    
    # GENERAL Expenses

    def add_general_expense(self, start_year, food=240, entertainment= 200, tech=35, pet=50):
        # personal items
        total = food + tech + pet + entertainment
        annual_expense = total*12
        for year in range(start_year, self.setup['meta']['retirement_year'] + 1):
            expense_list = self.setup['balance_sheet'][year]['expenses']
            expense_list.append({'source':'general expense', 'amount': annual_expense})

        # after updating income or expenses then run savings update    
        self.update_savings()

    # APARTMENT Rental Calcs
    def add_apartment(self, monthly_amount, start_date, end_date ):
        start= dt.strptime(start_date, "%m/%Y")
        end = dt.strptime(end_date, "%m/%Y")

        if start.year != end.year:
            start_amount = (12- start.month)*monthly_amount
            end_amount = (end.month - 1)*monthly_amount
            annual_amount = monthly_amount*12
            years = range(start.year, end.year+1)
            total = 0
            for year in years:
                expense_list = self.setup['balance_sheet'][year]['expenses']
                if year == start.year:
                    total += start_amount
                    expense_list.append({'source':'apartment rent', 'amount':start_amount})
                elif year == end.year:
                    total += end_amount
                    expense_list.append({'source':'apartment rent', 'amount':end_amount})
                else:
                    total += annual_amount
                    expense_list.append({'source':'apartment rent', 'amount':annual_amount})
        else:
            annual_amount = (end.month - start.month-1)*monthly_amount
            year = start.year
            expense_list = self.setup['balance_sheet'][year]['expenses']
            expense_list.append({'source':'apartment rent', 'amount': annual_amount})
            
        # after updating income or expenses then run savings update    
        self.update_savings()


    def child(self, start_year, number_guardians):
        end_year = self.setup['meta']['end_year']
        adult_year = start_year + 18
        end_year = adult_year if adult_year < end_year else end_year

        expense_list = self.setup['balance_sheet'][start_year]['expenses']
        expense_list.append({'source':'child birth', 'amount': 1900})

        for year in range(start_year, end_year):
            income = self.sum_parameters("income", year)
            #ref: https://en.wikipedia.org/wiki/Cost_of_raising_a_child
            current_age = year - start_year
            if number_guardians == 1:
                if income <40410:
                    cost = 8019 + 96.86*current_age
                else:
                    cost = 16675 + 246.48*current_age
            else:
                if income < 59410:
                    cost = 8826 + 75.62*current_age
                elif income < 102870:
                    cost = 11989 + 141.52*current_age
                else:
                    cost = 19662 + 264.86*current_age
            
            expense_list = self.setup['balance_sheet'][year]['expenses']
            expense_list.append({'source':'childcare', 'amount': cost})
            expense_list.append({'source':'college504b', 'amount': 3000})

            assets_list = self.setup['balance_sheet'][year]['assets']
            assets_list.append({'source':'college504b', 'amount': 3000})
        # after updating income or expenses then run savings update    
        self.update_savings()
    
    # ASSETS
    # HOUSE Purchase
    def add_house(self, selling_price, down_payment, interest_rate, loan_term, start_year):
        principle= selling_price - down_payment
        # monthly mortgage payment
        mortgage_payment = pv_an(principle, interest_rate, 12, loan_term) 
        # print('Mortgage: ', mortgage_payment)
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
                # print("Principle (", year, "/", month, ")", principle_update)
            
            expense_list = self.setup['balance_sheet'][year]['expenses']
            expense_list.append({'source':'mortgage interest', 'amount': round(interest_component,2)})
            expense_list.append({'source':'mortgate principle', 'amount': round(principle_component,2)})
            
            assets_list = self.setup['balance_sheet'][year]['assets']
            assets_list.append({'source':'home equity', 'amount': round(principle_component,2)})

            liabilities_list = self.setup['balance_sheet'][year]['liabilities']
            liabilities_list.append({'source':'home principle', 'amount': round(principle,2)})

        # after updating income or expenses then run savings update    
        self.update_savings()
    
    
    
    
    # EXPERIMENTAL
    
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