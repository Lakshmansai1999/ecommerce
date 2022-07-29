#!/ C:\Users\Akshay\AppData\Local\Programs\Python\Python37
#  Author : Akshay Kumar Pasupunooti
#  OS     : Windows
#  Tool   : VSCode
#  Version: Python3.10.5
#  Date   : 08-07-2022


# The datetime module supplies classes for manipulating dates and times
from datetime import datetime,timedelta

# creating and removing a directory (folder), fetching its contents, 
# changing and identifying the current directory
import os

# Standard library module intended to manipulate ZIP files
from zipfile import ZipFile

#  Changing Directory
os.chdir("A:\\PDFS\\SQL pdf")
print(os.getcwd())

# Current Date and Time 
cd=datetime.now()
mon=cd-timedelta(days=20)

#  Creates Timestamp for Month Variable
Timestamp=datetime.timestamp(mon)


# to get list of files in current directory
files=[f for f in os.listdir() if os.path.isfile(f)]

#  Iterates the files in the Folders
for file in files:
# os.stat get status of the specified path
# st_ctime: It represents the time of most recent metadata change on Unix and creation time on Windows. 
# It is expressed in seconds.
    created=os.stat(file).st_ctime
    

#  Creating an Array to Store those files
testZip=[]
for file in files:
    created=os.stat(file).st_ctime
    if created<Timestamp:
        testZip.append(file)

#  Creates the Zip File
with ZipFile('Test1.zip','w')as zipfile:
    for file in testZip:
        zipfile.write(file) 

print('Done')
