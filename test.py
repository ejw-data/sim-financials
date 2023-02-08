from test_model import estimator

e1 = estimator()

e1.init(2015, 2022, 10, 20000)
e1.add_apartment(1200, "05/2015", "04/2018")
e1.add_house(300000, 50000, 0.0425, 30, 2019)
e1.child(2019, 2)
e1.add_income('Grocery United', 3000, 0, 2015)
e1.add_income('Jewell', 30000, 0.05, 2017)
e1.update_income('Jewell', 0, 0, 2020)
e1.add_income('Marianos', 45000, 0, 2020)
e1.one_off_income('insurance collection', 20000, 2019)

print("Setup", "------"*5)
e1.print_setup()
print("Income", "------"*5)
e1.print_income()
print("Expenses", "------"*5)
e1.print_expenses()

# list of incomes
# income_list=[]

# income_list.append(estimator.income_source("Marvel", 22))

# for obj in income_list:
#     print(obj.income)