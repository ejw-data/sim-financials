from test_model import estimator

e1 = estimator()

e1.init(2015, 2022, 10)

e1.add_income('Jewell', 30000, 0.05, 2017)
e1.update_income('Jewell', 0, 0, 2020)

e1.one_off_income('insurance collection', 20000, 2021)

e1.print_setup()

# list of incomes
# income_list=[]

# income_list.append(estimator.income_source("Marvel", 22))

# for obj in income_list:
#     print(obj.income)