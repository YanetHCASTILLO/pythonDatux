import sqlite3
import pandas as pd


df2=pd.read_csv("C:/Users/JANETH/Desktop/Nueva carpeta/customer.csv",index_col=1)
#df2=df.drop('Index', axis=1)
df2.columns = df2.columns.str.strip()

connection = sqlite3.connect('pregun5.db')

df2.to_sql('housing_developments',connection, if_exists='replace')
connection.close()

