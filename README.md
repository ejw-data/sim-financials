# sim-financials

Calculator that can do the following:
* Car calculator 
    - inputs:  selling price, down payment, interest rate, book value, insurance cost, taxes, maintenance cost, repair cost, ?replacement cost, fuel cost, registration fees, 
    - outputs: current expense, annual cash flow, future savings
* House calculator:
    - inputs: selling price, offer price, down payment, interest rate, surrounding house value, maintenance cost, repair cost, insurance cost, heating/cooling cost, electric cost, sewer costs, internet/cable costs, roof replacement, furnace replacement, siding replacement, insulation replacement, remodelling, property taxes, selling tax, realator fees, yard expenses, 
    - outputs:

* Rent calculator:
    - inputs: rent cost, internet cost, gym cost, insurance, electricity expense
    - outputs:  current expense, annual cash flow

* Retirement calculator:
    - Bond calc:
    - Stock calc:
    - Investment property calc:
    - Expenses


Other considerations:
* Compare rent versus buying scenario - is there are savings?
    - The goal is to reduce total cash flow to balance all savings; for example, housing cost directly effects retirement savings and general spending and purchase initiatives.  
    - Scenario:  Buy house then have direct and indirect expenses, but could rent.  The comparision is interest expenses, maintenance expenses, taxes, utility costs, internet/cable that are recurring for ownership and rent and required expenses.  
    - Excellent analysis could be:  1) Calc annual cash flows and equity for house and apartment.  2) Next calc the savings if the rent savings was used as down payment.  

Designed with OOP so that the processes can be repeated and results stored to get a broad range of aggregated results.



Data Structure: 
```
    setup={ id: sim_id
            meta: {start_year: #, end_year: #, sim_length: #, retirement_year: # }
            balance_sheet:{
                2015: 
                    {income:[
                        {amount: #, source:xxx},
                        {amount: #, source:xxx}
                        ],
                    expenses:[],
                    assets:[]
                    }
                
            }
          }
```