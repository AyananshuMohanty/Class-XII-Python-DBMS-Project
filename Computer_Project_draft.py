# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 20:21:53 2021

@author: Ayananshu Mohanty
"""
import mysql.connector
connection_object=mysql.connector.connect (host="REDACTED", user="Ayananshu", passwd="REDACTED", database="employee_management")
if connection_object.is_connected():
    print('Successful')
else:
    print("Unsuccessful")
cursor=connection_object.cursor()            #Creates the connection with the SQL Database



def level_one_menu(employee_id,password):   #Access Level 1 Menu
    print("ACCESS LEVEL 1")
    print("")
    print("1.VIEW YOUR DETAILS")
    choice=input("Enter your choice: ")
    if choice=="1":
        view_your_details(employee_id)
    
def level_two_menu(employee_id,password):   #Access Level 2 Menu
    print("ACCESS LEVEL 2")
    print("")
    print("1.VIEW YOUR DETAILS")
    print("2.VIEW DETAILS OF LEVEL 1 EMPLOYEES")
    
    choice=input("Enter your choice: ")
    if choice=="1":
        view_your_details(employee_id)
    elif choice=="2":
        view_level_one_details()

def view_your_details(employee_id):       #Displays Details 
    cursor.execute("select * from employee_info where ID=%s" %(employee_id,))
    data=cursor.fetchall()
    print("ID: ", data[0][0])
    print("Name: ", data[0][1])
    print("Gender: ", data[0][2])
    print("Department: ", data[0][3])
    print("Access Level: ", data[0][4])
    print("Salary: ", data[0][5])
    print("Age: ", data[0][6])
    print("Date of joining: ", data[0][7])
    print("Password ", data[0][8])


def view_level_one_details():     #Displays details of all level 1 employees
    cursor.execute("select * from employee_info where Level_of_Access=1")
    data=cursor.fetchall()
    for i in data:
        print("ID: ", i[0])
        print("Name: ", i[1])
        print("Gender: ", i[2])
        print("Department: ", i[3])
        print("Access Level: ", i[4])
        print("Salary: ", i[5])
        print("Age: ", i[6])
        print("Date of joining: ", i[7])
        print("")
        
    
def login():                                #Login Page
    print("LOGIN")
    employee_id=int(input("Enter Employee ID: "))
    password=input("Enter password: ")
    cursor.execute("select * from employee_info where ID=%s" %(employee_id,))
    data=cursor.fetchall()
    if data==[]:
        print("Employee ID does not exist")
        print("")
        print("")
        login()
    elif data[0][8]==password:
        print("LOGIN SUCCESSFUL")
        return(data[0][4],employee_id,password)
    else:
        print("LOGIN UNSUCCESSFUL")
        print("Employee ID and Password do not match")
        print("RETRY LOGGING IN")
        print("")
        print("")
        login()                             


#MAIN PROGRAM
login_status,employee_id,password=login()
a="Y"
while a in "Yy":
    if login_status=="1":
        level_one_menu(employee_id,password)
    elif login_status=="2":
        level_two_menu(employee_id,password)
    a=input("Do you want to continue?: (Y/N)")
