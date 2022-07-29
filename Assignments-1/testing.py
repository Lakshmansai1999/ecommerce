#!/ C:\Users\pakshay\Desktop\NewPro\Ecomerce_project\testing.py  
# Machine:-Window   Tool:-VSCode  DateTime:29/06/2022  03:42PM 

#  Importing PostgreSQL database to conenct
import psycopg2
# Pandas is an open source Python package that is most widely used 
# for data science/data analysis and machine learning tasks. 
# Pandas package can be referred to as pd instead of pandas
import pandas as pd

#  Here we are connecting to DB using Credentials
# Like Host ID, Username, Password , DBname
# conn = psycopg2.connect(host= "138.68.44.49", user= "user_test", dbname = "TestingDB", password = "StratApps$09", )

#  Here iam fetching Data from the Database 
#  We can also use Joins here 
conn = psycopg2.connect(host= "138.68.44.49", user= "user_test", password = "StratApps$09", dbname = "TestingDB")
sql_query = pd.read_sql_query(''' select * from store_emp''', conn)
df1=pd.DataFrame(sql_query)
# We can download the output in CSV, Excel.. format
# Here iam using to_csv to download the output
# If index=True it creates a Index Column , index=False doesn't creates
sql_query.to_csv(r'C:\\Users\\pakshay\\Desktop\\abhi\\test.csv', index=False)
