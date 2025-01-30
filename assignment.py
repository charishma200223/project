#reading the excel file
import pandas as pd
pd.set_option('display.max_columns',None)
pd.set_option('display.width',1000)
df=pd.read_excel("C:\\Users\\HP\\Desktop\\student list.xlsx")
print(df)
#reading any one column
value=df.loc[3,'EMAIL'] # to select a row or column
print(value)
# reading a total column
column_values=df['EMAIL']
print(column_values)
# reading a specific rows by range
rows=df.loc[[4,3,2]]
print(rows)
#reading a phone number which has started with 8
phone_number=df[df['PHNO'].astype(str).str.startswith('7')]
print(phone_number)
#filtring
colms=['EMAIL','PHNO','SSC']
if all(col in df.columns for col in colms):
    print("All columns are exist")
else:
    print(" something missing")
#filtering 
filtered_df = df[colms]
print(filtered_df)
#dumping
filtered_df.to_excel('filtered_data.xlsx',index=False)
print('Filtered data dumped')
#error handling
if not all(col in df.columns for col in colms):
    print("error")
