######################################### FINANCE CALCULATOR #####################################
#                                                                                                #
# One method of managing personal finance is to allocate set amounts of money to certain things. #
# The following code will work on the assumption there are no large monthly outgoings e.g. rent  #
# # However I will eventually add that when I need it                                            #
# You want to put money in a 40% 20% 25% 15% split.                                              #
#                                                                                                #
##################################################################################################

#Input for what monthly income is
income = float(input('What was your income this month?  '))

#Fun account is 25% of monthly income
#Living account is 40% of monthly income
#Emergency fund id 15% of monthly incme
#Savings is 20% of monthly income

# Calculations for the 4 different savings pots
fun = income*0.25
living = income*0.40
emergency = income*0.15
savings = income*0.20

#output
print('###  Fun  ###')
print('')
print(fun)
print('')
print('###  Living  ###')
print('')
print(living)
print('')
print('###  Emergency  ###')
print('')
print(emergency)
print('')
print('@@@@@  Savings  ###')
print('')
print(savings)
print('')
print('')
x = input('Press enter to close')
print(x)
