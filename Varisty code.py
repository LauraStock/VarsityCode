# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x = 100 #amount borrowed
r = 0.05 #interest rate
y = 20 #years of mortgage
p = (r*x)/(1-(1+r)**(-y)) #minimum annual payment
ovp = 0 #annual overpayment 

annp = p+ovp #total annual payment 

Tot_p_No_Ovp = p*y #total paid over 20years

Tot_p = 0
Current_owe = x

i = 0

print(p)
print(p*y)

while i<y:
    Current_owe = Current_owe*(1+r) - annp
    Tot_p += annp
    print('year {}, currently owe {}'.format(i+1,Current_owe) )
    if Current_owe < annp:
        Current_owe = 0
        Tot_p += Current_owe
        print('currently in year {}'.format(i+1))
        break
    i+=1
    
    
print('total paid {}'.format(Tot_p))  
  
