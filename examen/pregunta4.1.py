import pandas as pd
df = pd.read_csv("C:/Users/JANETH/Desktop/Nueva carpeta/customer.csv")
b= df[df['Index']>=98]
print(b)
