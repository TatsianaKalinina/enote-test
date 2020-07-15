#!/usr/bin/env python
# coding: utf-8

# Enote Test Task - Python Script to Upload the data from .csv files to MySQL Database
# Author: Tatsiana Kalinina
# Date: 15.07.2020 

#importing necessary libraries
import pandas as pd
import numpy as np
import datetime
import pymysql

#create dataframe for the person data
df_person = pd.read_csv('BI_assignment_person.csv')
df_person.dropna(subset = ["id_person"], inplace=True)
df_person = df_person.replace(np.nan, '', regex=True)

#function that helps to fix 2-digit dates (panda to_datetime specific issue: )
def fix_date(x):
    print(type(x))
    if x.year > 1999:
        year = x.year - 100
    else:
        year = x.year
    return datetime.date(year,x.month,x.day)

#fix dates as they have different format in .csv
df_person["birth_date"] = pd.to_datetime(df_person["birth_date"])
df_person["birth_date"] = df_person["birth_date"].apply(fix_date)
#fix formats for int columns
df_person["id_person"] = df_person["id_person"].astype(int)
df_person["zip"] = df_person["zip"].astype(int)

#create dataframe for the Transaction data
df_transaction = pd.read_csv('BI_assignment_transaction.csv')
df_transaction.dropna(subset = ["id_transaction"], inplace=True)
df_transaction = df_transaction.replace(np.nan, '', regex=True)

#parse the dates
df_transaction["transaction_date"] = pd.to_datetime(df_transaction["transaction_date"])
df_transaction["transaction_date"] = df_transaction["transaction_date"].dt.date

#create dataframe for the Account data
df_account = pd.read_csv('BI_assignment_account.csv')
df_account.dropna(subset = ["id_account"], inplace=True)
df_account = df_account.replace(np.nan, '', regex=True)

#connect to the mysql database
conn = pymysql.connect(database = 'enote', user = '****', password = '****')
cursor = conn.cursor()
#test
#cursor.execute('Select * from enote.person')

#insert the values into the mysql person table
#create a batch with insert uploads
insert_query_1 = 'INSERT INTO enote.person VALUES '
for i in range(df_person.shape[0]):
    insert_query_1 += '(' 
    
    for j in range(df_person.shape[1]):
        insert_query_1 += "'" + str(df_person[df_person.columns.values[j]][i]).replace("'", "''") + "', "
        #if j == 4:
            #if i > 910 and i < 930:
                #print(str(df_person[df_person.columns.values[j]][i]).replace("'", "''"))
    insert_query_1 = insert_query_1[:-2] + '), ' 
insert_query_1 = insert_query_1[:-2] + ';'

#insert the values into the mysql transaction table
#create a batch with insert uploads
insert_query_2 = 'INSERT INTO enote.transaction VALUES '
for i in range(df_transaction.shape[0]):
    insert_query_2 += '(' 
    
    for j in range(df_transaction.shape[1]):
        insert_query_2 += "'" + str(df_transaction[df_transaction.columns.values[j]][i]).replace("'", "\'") + "', "
    
    insert_query_2 = insert_query_2[:-2] + '), '  
insert_query_2 = insert_query_2[:-2] + ';'
insert_query_2

#insert the values into the mysql account table
#create a batch with insert uploads
insert_query_3 = 'INSERT INTO enote.account VALUES '
for i in range(df_account.shape[0]):
    insert_query_3 += '(' 
    
    for j in range(df_account.shape[1]):
        insert_query_3 += "'" + str(df_account[df_account.columns.values[j]][i]) + "', "
    
    insert_query_3 = insert_query_3[:-2] + '), '
insert_query_3 = insert_query_3[:-2] + ';'
insert_query_3


#executing inserts
cursor.execute(insert_query_1)
conn.commit()
cursor.execute(insert_query_2)
conn.commit()
cursor.execute(insert_query_3)
conn.commit()

#close connection to the database
conn.close()




