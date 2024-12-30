import pandas as pd
import csv


df = pd.read_csv("sample_stock_data.csv")

print(df.head())
print("\n")

print(df.info())
print("\n")

print(df.shape) # 看数据有几行几列，不包括列索引
print("\n")

print(df['Open'])    # 选择名为 column_name 的列
print(df[['High', 'Low']])  # 选择 High 和 column2 两列
print("\n")


#打印特定列的前几行
# 选择特定列 (假设要选择 'High' 和 'Low')
selected_columns = df[['High', 'Low']]
# 打印前 5 行
print(selected_columns.head(5))


print(df.iloc[0])          # 选择第一行（基于位置索引）
print(df.iloc[1:5])        # 选择第二到第五行

df.to_csv('processed_data.csv', index=False)  # index=False 表示不保存索引
df.to_excel('processed_data.xlsx', index=False)
