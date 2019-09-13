# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
bank = pd.read_csv(path)

categorical_var = bank.select_dtypes(include='object')
print(categorical_var)

numerical_var = bank.select_dtypes(include='number')
print(numerical_var)
# code starts here






# code ends here


# --------------
# code starts here
bank.columns
banks = bank.drop('Loan_ID',axis=1)
banks.columns
banks.isnull().sum()

bank_mode = banks.mode(axis=0)
#col = list(banks.columns)

bank_mode.loc[0,:]
banks.isnull().sum()

#for x in banks.columns.values:
#        banks[x]=banks[x].fillna(value=bank_mode[x].loc[0])
##banks = banks[col].apply(lambda x: x.fillna(x.mode,inplace=True))

banks.fillna(bank_mode.loc[0,:],inplace=True)
banks.isnull().sum()

#banks.isnull().sum()

#code ends here


# --------------
# Code starts here
banks[['Gender','Married', 'Self_Employed','LoanAmount']]

avg_loan_amount = pd.pivot_table(banks, values='LoanAmount', index=['Gender','Married','Self_Employed'], aggfunc=np.mean)


# code ends here



# --------------
# code starts here
self_emp_y = banks['Self_Employed'] == 'Yes' 
loan_status = banks['Loan_Status'] == 'Y'
self_emp_n = banks['Self_Employed'] == 'No'
Loan_Status = 614
loan_approved_se = (self_emp_y & loan_status).value_counts()[1]
loan_approved_nse = (self_emp_n & loan_status).value_counts()[1]
print(loan_approved_se ,'   ',loan_approved_nse, Loan_Status)

percentage_se = (loan_approved_se/Loan_Status) * 100
percentage_nse = (loan_approved_nse/Loan_Status) * 100

print("Percent of Loan approval for Self employed people is : ",percentage_se)
print("Percent of Loan approval for people who are not self-employed is: ",percentage_nse)
# code ends here


# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply(lambda x : x/12)
loan_term>=25

big_loan_term = banks[loan_term>=25].shape[0]



# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby('Loan_Status')

loan_groupby = loan_groupby[['ApplicantIncome','Credit_History']]
mean_values = loan_groupby.mean()
print(mean_values)


# code ends here


