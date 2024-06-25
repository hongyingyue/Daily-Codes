import mysql.connector
import pandas as pd


def load_data(file_name):
	#data=r('foreign::read.spss("%s",to.data.frame=True)'%file_name)
	#data=pandas2ri.ri2py(data)
	data=pd.read_csv(file_name,sep=',',error_bad_lines=False,encoding=u'utf-8')
	return data


def create_database(columns):
	mydb=mysql.connector.connect(host='localhost',
		user='root',
		passwd='root',
		#database='',
		charset='utf8')
	mycursor=mydb.cursor()
	mycursor.execute("CREATE DATABASE if not exists NCBS")
	mycursor.execute("USE NCBS")
	mycursor.execute("CREATE TABLE IF NOT EXISTS ncbs "+"("+columns+")")
	mycursor.execute("LOAD DATA LOCAL INFILE 'NCBS_CN_2017.csv' INTO TABLE ncbs FIELDS TERMINATED BY ','")
	#mycurser.execute("unicode()")
	

'''
	mycursor.execute("CREATE TABLE students (name VARCHAR(255),age INTEGAR)")
	sqlformula="INSERT INTO students(name,age) values(%s,%s)"
	student1=("Rachael",22)
	mycursor.execute(sqlformula,student1)

	mycursor.execute("SELECT age from students")
	myresult=mycursor.fetchone()
	for row in myresult:
		print(row)
 '''
data=load_data('NCBS_CN_2017.csv')
columns=','.join([column.replace('.','')+' TINYTEXT' for column in data.columns])
create_database(columns)
print('Done')




