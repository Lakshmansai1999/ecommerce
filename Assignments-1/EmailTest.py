import smtplib
from email.message import EmailMessage

msg=EmailMessage()
msg['subject']='Automated Testing Data '
msg['from']='Akshay Kumar'
msg['To']='kprudvi@stratapps.com,pasupunootiakshay1@gmail.com'

with open("C:\\Users\\pakshay\\Desktop\\NewPro\\table1.csv","rb") as f:
    file_data=f.read()
    print("File data in binary",file_data)
    file_name=f.name
    msg.add_attachment(file_data,maintype="application",subtype="csv",filename =file_name)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("pakshay@stratapps.com", "AKShay@stratapps")
    server.send_message(msg,'Sucessfully Tetsed')

print("Email sent !!!")