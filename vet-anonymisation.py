import os
import pandas as pd
os.chdir(r'C:\Users\VillageVets\Downloads') # Change this to file path to where the .txt file is located

# Import the .txt file
vet = pd.read_table("vet-sales-data.txt", sep = '  ', header = 0, # note the seperator is TWO spaces
                    names = ['client', 'service', 'price', 'branch', 'pay_method', 'service_id', 'date'])
print(vet.head()) # confirm imported correctly

# Anonymise Names
vet['client'] = vet['client'].astype('|S') 
# string with auto max length 
vet['client'] = 'Person' + pd.Series(pd.factorize(vet['client'])[0] + 1).astype(str)
print(vet.head())

# Address inconsistencies in service_id
print(describe(vet['service_id']))
# Note: this dataset had unique rows and had no null values i.e. no other data cleaning was necessary

# Export for Power BI
print(vet.info()) # datatypes need to be changed but cleaning can be done in PowerQuery
vet_BI = vet.to_excel(r'C:\Users\VillageVets\Bradford\vet_BI.csv') 
# Change this to file path where you want to save
# This file path will be recalled in PowerBI!

# Keep this script in a safe place on the system
