# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 10:32:14 2022

"""


def calculate_eligibility(NumPeople,HouseCost,Deposit,Sal1,Sal2,Overpayment):
    
    #output: [MortgageAmount, AnnualRepayment, TotalRepaid, TotalOverpayment, YearsOverpayment]
    MortgageAmount = 0
    AnnualRepayment = 0
    TotalRepaid = 0
    TotalOverpayment = 0
    YearsOverpayment = 0
            
    #check for non-zero values
    if 0<NumPeople<3:
        #print('Correct num of people')
        if HouseCost > 0:
            #print('house cost isnt 0')
            if Deposit/HouseCost > 0.1:
                #print('Deposit is enough')
                if Sal1>0 and Sal2>=0:
                    #print("Salaries arent 0")
                    MortgageAmount = 5*(Sal1+Sal2)
                else:
                    return [MortgageAmount, AnnualRepayment, TotalRepaid, YearsOverpayment]                    
            else:
                return [MortgageAmount, AnnualRepayment, TotalRepaid, YearsOverpayment]  
        else:
            return [MortgageAmount, AnnualRepayment, TotalRepaid, YearsOverpayment]
    else:
        return [MortgageAmount, AnnualRepayment, TotalRepaid, YearsOverpayment]   
    
    if Overpayment<0:
        return [MortgageAmount, AnnualRepayment, TotalRepaid, YearsOverpayment]
    else:
        x = MortgageAmount #amount borrowed
        r = 0.05 #interest rate
        y = 20 #years of mortgage
        p = (r*x)/(1-(1+r)**(-y)) #minimum annual payment
        AnnualRepayment = p
        ovp = Overpayment #annual overpayment 
        
        annp = p+ovp #total annual payment 
        
        TotalRepaid = p*y #total paid over 20 years
        
        TotalOverpayment = 0
        Current_owe = x
        
        i = 0
        
        #print(p)
        #print(TotalRepaid)
        
        while i<y:
            Current_owe = Current_owe*(1+r) - annp
            TotalOverpayment += annp
            #print('year {}, currently owe {}'.format(i+1,Current_owe) )
            if Current_owe < annp:
                TotalOverpayment += Current_owe
                Current_owe = 0
                #print('currently in year {}'.format(i+1))
                i+=2
                break
            i+=1
            
        YearsOverpayment= i
        #print('total paid {}'.format(TotalOverpayment))  
        return [MortgageAmount, round(AnnualRepayment,2), round(TotalRepaid,2), YearsOverpayment] 

    
    
print(calculate_eligibility( 3, 120000, 18000, 29000, 17000, 150 ))
    
        
    