import pandas as pd
from datetime import datetime
data = {  
    'Customer_ID': [1, 2, 3, 4],  
    'Join_Date': ['2023-01-15', '2022-05-20', '2023-03-10', '2023-07-01'],  
    'Total_Purchases': [5, 15, 8, 20],  
    'Avg_Spend': [50, 120, 80, 200],  
    'Region': ['North', 'South', 'North', 'East']  
}  
df = pd.DataFrame(data)  

# Calculate Customer_Tenure (days since joining).
df["Join_Date"] = pd.to_datetime(df["Join_Date"])
Today = datetime.now()
df["Customer_Tenure"] = (Today-df['Join_Date']).dt.days
# Create a Customer_Value score: Total_Purchases * Avg_Spend.
df["Customer_Value"] = df["Total_Purchases"]*df["Avg_Spend"]
# Bin Customer_Value into "Low", "Medium", "High".
bins = [0,1500,3000,4500]
labels = ["Low","Medium","High"]
df["Customer_Value_Labels"] = pd.cut(df['Customer_Value'],bins=bins,labels=labels)

# Optimize memory usage for numerical columns.
#before optimization
# print(df.info(memory_usage='deep'))
df["Customer_ID"] = pd.to_numeric(df["Customer_ID"], downcast='unsigned')
df['Avg_Spend'] = pd.to_numeric(df['Avg_Spend'],downcast="unsigned")
df['Customer_Tenure'] = pd.to_numeric(df['Customer_Tenure'],downcast="unsigned")
df["Total_Purchases"] = pd.to_numeric(df["Total_Purchases"],downcast="unsigned")
df["Customer_Value"] = pd.to_numeric(df["Customer_Value"],downcast="unsigned")

df["Customer_Value_Labels"] = df["Customer_Value_Labels"].astype("category")
df["Region"] = df["Region"].astype("category")
#after
# print(df.info(memory_usage='deep'))
# Pivot the data to show Avg_Spend by Region.
Pivort = df.pivot_table(values="Avg_Spend",index="Region",observed=False)

# Cleaned DataFrame with new features.
print(df)
# Summary table of average customer value by region.
print(Pivort)
