# # import pdfkit as pdf

# # pdf.from_file('C:\\Users\\pakshay\\Desktop\\NewPro\\report.html', 'Output.pdf')

# import pandas as pd
# import pdfkit
 
# # SAVE CSV TO HTML USING PANDAS
# csv = 'MyCSV.csv'
# html_file = 'tab'[:-3]+'html'
 
# df = pd.read_csv('tab.csv', sep=',')
# df.to_html(html_file)
 
# # INSTALL wkhtmltopdf AND SET PATH IN CONFIGURATION
# # These two Steps could be eliminated By Installing wkhtmltopdf -
# # - and setting it's path to Environment Variables
# path_wkhtmltopdf = r'C:\\Users\\pakshay\\Desktop\\NewPro\\.venv\\Lib\site-packages\\wkhtmltopdf'
# config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
 
# # CONVERT HTML FILE TO PDF WITH PDFKIT
# pdfkit.from_url("MyCSV.html", "FinalOutput.pdf", configuration=config)


import pandas as pd
import pdfkit as pdf
from pdfkit import PDFKit
# from pdfkit import Configuration

csv_file = 'tab.csv'
html_file = csv_file[:-3]+'html'
pdf_file = csv_file[:-3]+'pdf'

df = pd.read_csv(csv_file, sep=',')
df.to_html(html_file)
pdf.from_file(html_file, pdf_file)