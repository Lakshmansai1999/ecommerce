#!/ .\.venv\Scripts\python.exe
#   Version : Python 3.10.5
#   Author : Pasupunooti Akshay Kumar
#   Platform - Windows
#   Tools - VS Code

import email, smtplib, ssl
import pandas as pd
import psycopg2

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import maskpass

subject = "Automated Testing"
body = "Sucessfully Compared Local File Data and DataBase Data. \n \n Status:-Failure...!!!"
sender_email = "pakshay@stratapps.com"
receiver_email = "dravi@stratapps.com"
password = maskpass.askpass('Enter your Password:')

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
# message["Bcc"] = receiver_email  # Recommended for mass emails

d=pd.read_csv("C:\\Users\\pakshay\\Desktop\\NewPro\\table2.csv")
df=pd.DataFrame(d)
    
conn = psycopg2.connect(host= "138.68.44.49", user= "user_test", password = "StratApps$09", dbname = "TestingDB")
sql_query = pd.read_sql_query(''' select * from store_emp''', conn)
df1=pd.DataFrame(sql_query)
df.compare(df1,keep_shape=True,keep_equal=True)


# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "C:\\Users\\pakshay\\Desktop\\NewPro\\report1.html"
# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)