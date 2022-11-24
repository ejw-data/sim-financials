

# create time value functions  

def fv_pv(pv, i, n, t):
    '''
    Calculate the future value given present value
    pv:  present value
    i :  nominal annual interest rate
    n :  number of compounding terms in a year
    t :  number of years     
    '''
    time_factor = (1+i/n)**(n*t)
    fv = pv*time_factor
    return fv

def pv_fv(fv,i,n,t):
    '''
    Calculate the present value given future value
    fv:  future value
    i :  nominal annual interest rate
    n :  number of compounding terms in a year
    t :  number of years 
    '''
    time_factor = (1+i/n)**(n*t)
    pv = fv/time_factor
    return pv


def pv_an(an,i,n,t):
    '''
    Calculate the present value given an annuity
    an:  constant annuity amount
    i :  nominal annual interest rate
    n :  number of compounding terms in a year
    t :  number of years 
    '''
    time_factor = (1 - (1/(1+i/n)**(n*t)))/i
    pv = an*time_factor
    return pv

def an_pv(pv,i,n,t):
    '''
    Calculate the annuity given the present value
    pv:  present value
    i :  nominal annual interest rate
    n :  number of compounding terms in a year
    t :  number of years 
    '''
    time_factor = (1 - (1/(1+i/n)**(n*t)))/i
    an = pv/time_factor
    return an

