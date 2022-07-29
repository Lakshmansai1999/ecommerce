#!/ C:\Users\Akshay\AppData\Local\Programs\Python\Python37

import difflib

first_file='C:\\Users\\pakshay\\Desktop\\NewPro\\table1.csv'
second_file='C:\\Users\\pakshay\\Desktop\\NewPro\\table2.csv'

first_file_lines=open(first_file).readlines()
second_file_lines=open(second_file).readlines()

difference=difflib.HtmlDiff().make_file(first_file_lines,second_file_lines,first_file,second_file)

difference_report=open('C:\\Users\\pakshay\\Desktop\\NewPro\\report1.html','w')

difference_report.write(difference)

difference_report.close()

