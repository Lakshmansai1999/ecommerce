#!/ .\.venv\Scripts\python.exe
#   Version : Python 3.10.5
#   Author : Pasupunooti Akshay Kumar
#   Platform - Windows
#   Tools - VS Code
#   Date - 01-07-2022 

from email import message_from_binary_file
from fileinput import filename
import smtplib, ssl
import pandas as pd
import psycopg2

import getpass

# For starttls    Modern email servers use port 587 for the secure submission of email for delivery
port = 587 
smtp_server = "smtp.gmail.com"
receiver_email =[ "pasupunootiakshay1@gmail.com"]
sender_email = "pakshay@stratapps.com"
password = getpass.getpass('Password:')
# password = input("Type your password and press enter:")

d=pd.read_csv("C:\\Users\\pakshay\\Desktop\\NewPro\\table2.csv")
df=pd.DataFrame(d)
    
conn = psycopg2.connect(host= "138.68.44.49", user= "user_test", password = "StratApps$09", dbname = "TestingDB")
sql_query = pd.read_sql_query(''' select * from store_emp''', conn)
df1=pd.DataFrame(sql_query)
df.compare(df1,keep_shape=True,keep_equal=True)

if df.values.all()==df1.values.all():

    message = """\
        
        Data is Matched 
    """
else:
    message ="""
    \ Data Does not Matched
    """


context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo() 
    server.starttls(context=context) 
    server.ehlo() 
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)