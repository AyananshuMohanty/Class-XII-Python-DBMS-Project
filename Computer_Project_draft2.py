# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 20:21:53 2021

@author: Ayananshu Mohanty
"""
import random
import mysql.connector
connection_object=mysql.connector.connect (host="DESKTOP-ANVNLP2", user="Ayananshu", passwd="undergroundSamurai", database="employee_management")
if connection_object.is_connected():
    print('Connection was successful')
else:
    print("Connection was unsuccessful")
cursor=connection_object.cursor()                        #Creates the connection with the SQL Database


def level_one_menu(employee_id,password):
    """ 
    Displays the Level 1 Employee Menu.
    """
    print("ACCESS LEVEL 1")
    print("")
    print("1.VIEW YOUR DETAILS")
    print("2.ALTER PERSONAL INFO")
    print("3.VIEW EMPLOYEE LIST")
    choice=input("Enter your choice: ")
    if choice=="1":
        view_your_details(employee_id)
    elif choice=="2":
        alter_personal_info(employee_id)
    elif choice=="3":
        employee_list()
    else:
        print("Sorry, invalid choice, please try again.")
        print("")
        level_one_menu(employee_id,password)
         

def level_two_menu(employee_id,password):
    """
    Displays the Level 2 Employee Menu.
    """
    print("ACCESS LEVEL 2")
    print("")
    print("1.VIEW YOUR DETAILS")
    print("2.VIEW EMPLOYEE LIST")
    print("3.VIEW DETAILS OF LEVEL 1 EMPLOYEES")
    print("4.REGISTER AN EMPLOYEE")
    print("5.ALTER PERSONAL INFO")
    print("6.ALTER LEVEL 1 EMPLOYEE INFO")
    print("7.DELETE A RECORD OF LEVEL ONE EMPLOYEE")
    choice=input("Enter your choice: ")
    if choice=="1":
        view_your_details(employee_id)
    elif choice=="2":
        employee_list()
    elif choice=="3":
        view_level_one_details()
    elif choice=="4":
        register_employee()
    elif choice=="5":
        alter_personal_info(employee_id)
    elif choice=="6":
        alter_level_one_info()
    elif choice=="7":
        delete_record()
    else:
        print("Sorry, invalid choice, please try again.")
        print("")
        level_two_menu(employee_id,password)
        
        
def view_your_details(employee_id):
    """
    Displays the details of the current user.
    """
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
    print("Password: ", data[0][8])
     
    
def view_level_one_details():
    """
    Displays the details(except password) of all the Level 1 Employees.
    *This function can be accessed by Level 2 Employees only.*
    """
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


def register_employee():
    """
    Registers the details of a new employee and generates a new password.
    (New password is supposed to be used for first time login.
    Employees can modify their password after logging in.)
    *This function can be accessed by Level 2 Employees only.*
    """
    emp_id=input("Enter ID of Employee whose details you want to register: ")   
    emp_name=input("Enter Employee Name: ")
    emp_gen=input("Enter Gender: ")
    emp_level="1"
    emp_dept=input("Enter Department: ")
    emp_salary=int(input("Enter Salary: "))
    emp_age=int(input("Enter Age: "))               
    emp_doj=int(input("Enter Date of joining (YYYYMMDD): "))
    emp_pas="password"+str(random.randint(10000,99999))
    cursor.execute("insert into employee_info values('{}','{}','{}','{}','{}',{},{},{},'{}')".format(emp_id,emp_name,emp_gen,emp_dept,emp_level,emp_salary,emp_age,emp_doj,emp_pas))
    connection_object.commit()
    print("Employee registered successfully with the password:",emp_pas)
    print("") 
               
        
def alter_personal_info(employee_id):
    """
    Allows the user to update their information.
    """
    print("1.DEPARTMENT\n2.PASSWORD")
    ch=int(input("Enter choice of category to change: "))
    if ch==1:
        dept=input("Enter new department: ")
        cursor.execute("update employee_info set Department='{}' where ID='{}'".format(dept,employee_id))
        connection_object.commit()
        print("Department changed successfully")
        print("")
    elif ch==2:
        cursor.execute("select * from employee_info where ID='{}'".format(employee_id))
        data=cursor.fetchall()
        oldpass=data[0][8]
        print("Your old password is: ",oldpass)
        print("")
        change_password()
        

def change_password():
    """
    Allows the user to change their password and checks whether the password meets certain criteria.
    (Password must be greater than 8 characters in length and must have atleast 1 lowercase character,1 uppercase character, 1 number, and 1 special character.)
    """
    print("PASSWORD NAMING RULES")
    print("Password must be greater than 8 characters in length.")
    print("Password must have atleast 1 lowercase character,1 uppercase character, 1 number, and 1 special character.")
    newpass=input("Enter new password: ")
    newpass_undercase=""
    newpass_uppercase=""
    newpass_numbers=""
    newpass_specialchar=""
    newpass_length=len(newpass)
    newpass_error=""
    for i in newpass:
        if i in "abcdefghijklmnopqrstuvwxyz":
            newpass_undercase=newpass_undercase+i
        elif i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            newpass_uppercase=newpass_uppercase+i
        elif i in "1234567890":
            newpass_numbers=newpass_numbers+i
        else:
            newpass_specialchar=newpass_specialchar+i
    if newpass_length<8:
        newpass_error=newpass_error+"1"
    if  len(newpass_undercase)==0:
        newpass_error=newpass_error+"2"
    if  len(newpass_uppercase)==0:
        newpass_error=newpass_error+"3"
    if  len(newpass_numbers)==0:
        newpass_error=newpass_error+"4"
    if  len(newpass_specialchar)==0:
        newpass_error=newpass_error+"5"
    if "1" in newpass_error:
        print("Length of the password is too short.")
    if "2" in newpass_error:
        print("No lowercase characters are present in the password.")
    if "3" in newpass_error:
        print("No uppercase characters are present in the password.")
    if "4" in newpass_error:
        print("No numbers are present in the password.")
    if "5" in newpass_error:
        print("No special characters are present in the password.")
    number_of_errors=len(newpass_error)
    if number_of_errors>0:
        print("INVALID PASSWORD")
        print("")
        change_password()
    if number_of_errors==0:
        password_confirm(newpass)
    
        
def password_confirm(newpass):
    """
    Confirms the validity of the new password entered by the user.
    """
    newpasscon=input("Confirm new password: ")
    if newpass == newpasscon:
        cursor.execute("update employee_info set Password = '{}' where ID='{}'".format(newpass,employee_id))
        connection_object.commit()
        print("Password changed successfully")
        print("")
    else:
        print("Passwords don't match, please try again.")
        print("")
        password_confirm(newpass)


def employee_list():
    """ 
    Displays the Employee ID and Name of all the employees.
    """
    cursor.execute("select * from employee_info order by Name asc")
    data=cursor.fetchall()
    print("Employee ID             Name")
    for i in data:
        print(i[0],"             ",i[1])
        print("")


def alter_level_one_info():
    """
    Allows Level 1 Employees to alter their Department and Salary.
    """
    emp_id=input("Enter ID of employee whose data you want to change: ")
    cursor.execute("select * from employee_info where Level_of_Access=1")
    data=cursor.fetchall()
    data_list=[]
    l=len(data)
    for i in range(l):
        data_list=data_list+[data[i][0]]
    if emp_id in data_list:
        print("1.DEPARTMENT\n2.SALARY")
        ch=int(input("Enter choice of category to change: "))
        if ch==1:
            dept=("Enter new department")
            cursor.execute("update employee_info set Department ='{}' where ID='{}'".format(dept,emp_id))
            connection_object.commit()
            print("Department changed successfully.")
            print("")
        elif ch==2:
            cursor.execute("select * from employee_info where ID=%s" %(emp_id,))
            emp_data=cursor.fetchall()
            sal=emp_data[0][5]
            sal=int(sal*110/100)
            cursor.execute("update employee_info set Salary ={} where ID='{}'".format(sal,emp_id))
            connection_object.commit()
            print("Salary increased by 10% successfully.")
            print("")
    else:
        print("Invalid ID, please try again.")
        alter_level_one_info()


def delete_record():
    """
    Deletes the record of an employee.
    *Can be Accessed by Level 2 Employees only.*
    """
    emp_id=input("Enter ID of employee whose data you want to delete: ")
    cursor.execute("Select ID from employee_info where Level_of_Access=1")
    data=cursor.fetchall()
    data_list=[]
    l=len(data)
    for i in range(l):
        data_list=data_list+[data[i][0]]
    if emp_id in data_list:
        cursor.execute("delete from employee_info where ID='{}'".format(emp_id))
        connection_object.commit()
        print("Record of employee deleted successfully")
        print("")
    else:
        print("Invalid ID, please try again.")
        delete_record()

     
def login():
    """
    Displays the Login Page.
    """
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


login_status,employee_id,password=login()
a="Y"
while a in "Yy":
    if login_status=="1":
        level_one_menu(employee_id,password)
    elif login_status=="2":
        level_two_menu(employee_id,password)
    a=input("Do you want to continue?(Y/N): ")
    print("")
    while a not in "YyNn":
        print("Please enter your choice again.")
        print("")
        a=input("Do you want to continue?(Y/N): ")
        print("")
print("")
print("THANK YOU FOR VISITING")
