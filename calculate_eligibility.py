# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 10:32:14 2022

"""


def calculate_eligibility(NumPeople,HouseCost,Deposit,Sal1,Sal2):
            
    #check for non-zero values
    if 0<NumPeople<3:
        #print('Correct num of people')
        if HouseCost > 0:
            #print('house cost isnt 0')
            if Deposit/HouseCost > 0.1:
                #print('Deposit is enough')
                if Sal1>0 and Sal2>=0:
                    #print("Salaries arent 0")
                    borrow = 5*(Sal1+Sal2)
                    return ("You could be able to borrow up to £{} for a mortgage towards your home.".format(borrow))
                else:
                    return "Invalid input"                    
            else:
                return "You need to have a larger deposit to get a mortgage for this home."  
        else:
            return "Invalid input"
    else:
        return "Invalid input"    
    
    
print(calculate_eligibility(1, 120000, 10, 29000, 0))
    
        
    