# Path: E:\TaskRK\project\testdb
# Machine: windows10 x64
# Author: K.V. Madhu Sudhan
# Tool: Visual Studio Code
# Tool version: 1.68.1
# Python Version: 3.9.12

# ST_CTIME: created time of the file.
# glob is used to return all file paths that match a specific pattern.
# stat: it call on the specified path. It is used to get status of the specified path
import os
import datetime
import os.path
import glob
from stat import ST_CTIME
import sys
from zipfile import ZipFile
from humanize import naturalsize
from datetime import datetime,timedelta
import shutil


# taking initial size of the files as 0.
size=0

# giving the path of the directory/folder in the system.
dir_name = 'A:\\PDFS\\Tableau PDF'

# Get a list of files (file paths) in the given directory 
list_of_files = filter( os.path.isfile,
                        glob.glob(dir_name + '*') )


 # get size
 # os.walk means generate the file names either top-down or bottom-up
for file_path, dir_name, list_of_files in os.walk('A:\\PDFS\\Tableau PDF'):
    # for files in list of files joining the path.
    for f in list_of_files:
        fp = os.path.join(file_path, f)
        # given resulting size of the files.
        size += os.stat(fp).st_size
print("Folder size: " + str(size),'bytes')
# printing the size bytes to kb,mb,gb.
print(naturalsize(size))


os.chdir("A:\\PDFS\\Tableau PDF")
os.getcwd()


#Get datetime object for one week
last_twodays= datetime.now() - timedelta(days=10)
#print(last_week)

# convert the datetime object into timestamp
timestamp=datetime.timestamp(last_twodays)
#print(timestamp)

# get the list of files in current dictionary

files=[ f for f in os.listdir() if os.path.isfile(f) ]

# get the created time for the files in current directory
for file in files:
    created = os.stat(file).st_ctime
# print(created)

# add files to the list if they created more than a week 
abc=[]
for file in files:
    created=os.stat(file).st_ctime
    if created < timestamp:
        abc.append(file)


# add old files to zip
from zipfile import ZipFile

with ZipFile('abc.zip','w') as zipfile:
    for file in abc:
        zipfile.write(file)
        
print("done")

# Moving that zip file to the required location.
source_path = r"abc.zip"
destination_path = r"A:\\PDFS"
shutil.move(source_path, destination_path)