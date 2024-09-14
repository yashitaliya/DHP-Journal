import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('product_sales.csv')
df["Total_sales"] = df[["JAN","FEB","MAR","APR","MAY","JUN"]].sum(axis=1)
df["Average_sales"] = df[["JAN","FEB","MAR","APR","MAY","JUN"]].mean(axis=1)
print(df)
plt.figure(figsize=(15,7))
plt.plot(df['Prod_name'],df["Total_sales"],label='Total_sales',marker='o',color='blue')
plt.plot(df['Prod_name'],df["Average_sales"],label='Average_sales',marker='o',color='red')
plt.title('product sales analysis')
plt.xlabel('product names')
plt.ylabel('sales')
plt.legend()
plt.show()


