import os
import pandas as pd
import openpyxl
os.chdir(r'C:\Users\VillageVets)\Downloads') # Change this to file path to where the .txt file is located
 
# Import the .txt file
vet = pd.read_table("vet-sales-data.txt", sep = '  ', header = 0, 
                    names = ['client', 'service', 'price', 'branch', 'pay_method', 'UNKNOWN', 'date'])
print(vet.head())
 
# # Investigating UNKNOWN column
# print(vet['UNKNOWN'].unique())
 
# vet962 = vet[(vet['UNKNOWN']==9625482)]
# print(vet962)
 
# vet952 = vet[(vet['UNKNOWN']==9528512)]
# print(vet952) # This subset and previous demonstrate 7 digits have nothing to do with client
# # might be related to price or date
 
# vet476 = vet[(vet['UNKNOWN']==4766371)]
# print(vet476) # comparing this subset and previous ... might be related to branch
# # comparing all 3 subsets so far, it doesn't seem to be related to service or price
 
# vet171 = vet[(vet['UNKNOWN']==1713895)]
# print(vet171) # doesn't seem to be related to service or price
 
vet157 = vet[(vet['UNKNOWN']==1575577)]
# print(vet157) # confirms that it's related to payment method- perhaps related to financial reconcilliation processes
# print(vet157.sort_values(by=['date', 'branch'])) # confirms that it's related to date too perhaps batch-based processing 
# hence, the data may be collected from these transactions at these dates.
# Let's look closer at branches Epsom and Redhill to check processing of cash batches
vet_RE = vet[(vet['branch']=='Epsom') | (vet['branch']=='Redhill')]
print(vet_RE.sort_values(by=['date','branch','pay_method'])) # Epsom and Redhill
 
pd.set_option('display.max_rows', None) # This is not recommended unless nrows is small (as in this case)
print(vet.sort_values(by=['UNKNOWN','pay_method','date','branch'])) 
# Confirms UNKNOWN 7 digits represent batch-processing IDs which indicates
# 1575577 = card transactions across months and branches
# 1713895 = cash transactions in August @ Woking
# 4766371 = cash transactions in December @ Epsom
# 9528512 = cash transactions in December @ Guildford
# 9625482 = cash transactions in October @ Guildford
# Card transactions are processed monthly
# Cash transactions are processed by employees at each branch, ideally more often than recorded here.
 
# There is not enough data to confirm this but for the purpose of the demonstration, this data will be retained. 
