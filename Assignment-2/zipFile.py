#!/ C:\Users\Akshay\AppData\Local\Programs\Python\Python37
#  Author : Akshay Kumar Pasupunooti
#  OS     : Windows
#  Tool   : VSCode
#  Version: Python3.10.5
#  Date   : 08-07-2022

import threshold

# Shutil module offers high-level operation on a file 
# like a copy, create, and remote operation on the file.
import shutil

source_path = r"testZip.zip"
destination_path = r"C:\\Users\\pakshay\\Desktop\\NewPro"
shutil.move(source_path, destination_path)

