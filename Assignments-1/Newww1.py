import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

sender_email = "pakshay@stratapps.com"
receiver_email = "pasupunootiakshay1@gmail.com"
password = getpass.getpass('Password:')

message = MIMEMultipart("alternative")
message["Subject"] = "Automated Testing"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi Sir,
Worked on Testing the Data Sucessfully

Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p>Hi Sir,<br>
       Worked on Automated Data Testing <br>
       Compared the CSV file <br>
       <a href="C:\\Users\\pakshay\\Desktop\\NewPro\\table2.csv">CSV Files </a> 
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )