# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:26:56 2023

@author: Administrator
"""

import pymysql

try:
    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='Password@1')
    if conn:
        cursor=conn.cursor()
        query='select * from adultinfo.adult;'
        cursor.execute(query)
        '''for records in cursor.fetchall():
            worktype = records[0]
            education = records[1]
            occupation = records[2]
            print(worktype,education,occupation)
            print(records)
            print("------")'''
        print(cursor.fetchmany(5))
            
        conn.close()
    else:
        print('Databse is not connected')

except pymysql.err.DatabaseError() as err:
    print('Database error',err)
except Exception() as err:
    print('Exception',err)
    
import pymysql
try:
    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='Password@1',database='adultinfo')
    if conn:
        cursor=conn.cursor()
        query="Insert into adult values ('{}','{}','{}')".format('Public','Phd','Doctor')
        cursor.execute(query)
        print(cursor.rowcount,'Rows inserted')
        conn.commit()
        conn.close()
    else:
        print('Database not connected')

except pymysql.DataError as err:
    print(err)
except pymysql.DatabaseError as err:
    print(err)
except pymysql.OperationalError as err:
    print(err)    
except (pymysql.IntegrityError,pymysql.InternalError) as err:
    print(err)
except Exception() as err:
    print(err)
    
#write a program to read adult.csv and insert workclass,occupation,education columns data to the database  

import pymysql
import csv
path='C:\\Users\\Administrator\\Desktop\\programs\\csvfiles\\adult.csv'

try:
    row_count=0
    with open(path,'r') as fr:
        reader=csv.reader(fr)
        print('FIle is read')
        conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='Password@1',database='adultinfo')
        for line in reader:
            workclass=line[1]
            occupation=line[3]
            education=line[6]
            if conn:
                cursor=conn.cursor()
                query="Insert into adult values ('{}','{}','{}')".format(workclass,occupation,education)
                cursor.execute(query)
                row_count=row_count+cursor.rowcount
                conn.commit()
                
            else:
                print('Database not connected')
        conn.close()
        print(row_count,"Rows Inserted")

except pymysql.DataError as err:
    print(err)
except pymysql.DatabaseError as err:
    print(err)
except pymysql.OperationalError as err:
    print(err)    
except (pymysql.IntegrityError,pymysql.InternalError) as err:
    print(err)
except Exception as err:
    print(err)        
    
#write a program to insert all the records from the database to the excel file
#( excel file should be todays timestamp  : 18_jul_2023.xlsx)
#( check for openpyxl library )

#step1 - create a workbook
#step2 - save the workbook in a filepath with name
#step3 - Load the workbook to start to load the data
#step4 - select a worksheet & make it active (default it'll have one worksheet, 
#        we need specify the woksheet name for multiple worksheets)
#step5 - #append the worksheet - sheet.append()
#step6 - save the workbook

from openpyxl import Workbook
import pymysql
import time
import sys

filename=time.strftime('%d_%b_%Y')+'.xlsx'
print(filename)
wb= Workbook()
worksheet=wb.active

try:
    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='Password@1',database='adultinfo')
    if conn:
        print('DB connected')
        cursor=conn.cursor()
        query='select * from adult'
        cursor.execute(query)
        print('Start to load workbook')
        for line in cursor.fetchall():
            workclass=line[0]
            education=line[1]
            occupation=line[2]
            worksheet.append([workclass,education,occupation])
        wb.save(filename)
        conn.close()
    else:
        print('Not Connected')

except Exception as err:
    print(err)
    print(sys.exc_info())


#write it to csv file

import csv
import pymysql
import sys

try:
    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='Password@1',database='adultinfo')
    if conn:
        print('Database connected')
        cursor=conn.cursor()
        query='select * from adult'
        cursor.execute(query)
        for record in cursor.fetchall():
            workclass=line[0]
            education=line[1]
            occupation=line[2]
            with open('adultdata.csv','w') as fw:
                writer=csv.writer(fw)
                writer.writerows([workclass,education,occupation])
        conn.close()
    else:
        print('Database not connected')
except Exception() as err:
    print(err)
    print(sys.exc_info())


import csv
import sys, traceback
import pymysql

try:
    conn= pymysql.connect(host='127.0.0.1', port=3306, user= 'root', password='Password@1')
    if conn:
        cursor= conn.cursor()
        query= "Select * from adultinfo.adult"
        cursor.execute(query)
        for record in cursor:
            worktype = record[0]
            education = record[1]
            occupation = record[2]            
            with open("datafile.csv", "w") as fileobj:
               writer= csv.writer(fileobj)
               writer.writerow([worktype,education,occupation])
        conn.close()
    else:
        print("Conection is not successful..")
except:
    print(sys.exc_info())
    print(traceback.print_exc())


