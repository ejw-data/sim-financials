from test_model import estimator

e1 = estimator()

e1.init(2015, 2022, 10)

e1.print_setup()

# list of incomes
income_list=[]

income_list.append(estimator.income_source(22))

for obj in income_list:
    print(obj.income)