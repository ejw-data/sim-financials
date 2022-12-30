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
