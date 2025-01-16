import pandas as pd

# # Series
# mango = pd.Series([4, 5, 6, 3, 1], index =[0, 1, 2, 3, 4])
# print(mango)

# apple = pd.Series([5, 4, 3, 0, 2], index =[0, 1, 2, 3, 4])
# print(apple)

# banana = pd.Series([2, 3, 5, 2, 7], index =[0, 1, 2, 3, 4])
# print(banana)

# a = [2, 4, 6, 8, 10]

# series_a = pd.Series(a) 
# print(series_a)

# df_a = pd.DataFrame(series_a)
# print(df_a)

#path = "MCI_PY09A21L1\Bai05_pandas\Automobile_data.csv"
df_Automobile = pd.read_csv(r'MCI_PY09A21L1\Bai05_pandas\Automobile_data.csv')
print(df_Automobile)

# Read Excel
df_excel =pd.read_excel('MCI_PY09A21L1\Bai05_pandas\employees.xlsx', sheet_name=0, engine='openpyxl')
print(df_excel)

df = pd.DataFrame(df_excel)
# truy cap phan tu loc
print(df.loc[1,'first_name'])
print(df.loc[2,'hire_date'])

# su dung iloc ( truy cap theo chi so hang cot)
print(df.iloc[1, 2])

# truy cap nhieu hang, nhieu cot
print(df.loc[:, 'first_name'])
print(df.loc[:, ['first_name', 'last_name']])

print(df.iloc[:, 1])

# truy cap phan tu theo dieu kien
print(df[df['emp_id'] > 110])
print(df.loc[df['first_name'] == 'Den'])

# su dung at[], iat[] de truy cap
print(df.at[1, 'first_name'])
print(df.iat[1,2])

# truy cap toan bo gia tri va chuyen thanh mang numpy
print(df['emp_id'].values)

# THAY DOI GIA TRI PHAN TU
df.loc[1, 'first_name'] = 'HaNoi'
print(df)

# truy cap 5 row dau tien
print(df.head())

print(df.columns)
print(df['first_name'])

# Xoa 1 hang 
delete_df = df.drop(index=15)
print(delete_df)

# xoa hang trung nhau
delete_duplicate = df.drop_duplicates(subset='emp_id')
print(delete_duplicate)

print("-------------------------")
# Xu ly gia tri NULL
# axis = 0 ==> xoa hang
# axis = 1 ==> xoa cot
# nan_df = df.dropna(axis= 0)
# print(nan_df)

# fill tat ca gia tri nan values voi gia tri dac biet
new_df = df.fillna('ABC')
print(new_df)
print("-------------------------")
# Sua doi cac phan tu trong khung du lieu ==> apply
df['emp_id'] = df['emp_id'].apply(lambda x: x + 100)
print(df)

# ap dung len tung hang
df['Name'] = df.apply(lambda row: f"{row['first_name']} {row['last_name']}", axis=1)
print(df)

# luu ket qua thanh 1 file excel moi
df.to_csv('new_employees.csv', index= False)