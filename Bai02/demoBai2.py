# khai bao bien
a = 8

if a > 0:
    # hien thi loi chao
    print("Hello Viet Nam")
else:
    print("Hello Cambodia")

# Quy tac dat ten bien
# 9b = 9 : bien khong duoc bat dau bang so
number = 9
color = "Blue"
#if = "Hello" : Ten bien trung voi tu khoa trong python
# def = 12
average_number = 9.5
obj = None
bLight = True | False

khoangcach = 10
quangduong_1ngay = 2 *khoangcach
quangduong_1thang = 25 * quangduong_1ngay
so_litxng_1thang = quangduong_1thang/ 50
tienxang_1thang = so_litxng_1thang *25000

# ==> BIẾN SỐ
# Cú pháp : bienSo = <giá trị>
x = 1
x = 2
x = x + 1
print(x)

# de xoa 1 bien số dùng hàm del
del x

poem ='''Hôm nay trời nắng chang chang
Mèo con đi học chẳng mang thứ gì
Chỉ mang một chiếc bút chì
Và mang một mẩu bánh mỳ con con
'''

print(poem)

str1 = poem.upper()
print(str1)

str2 = str1.lower()
print(str2)

# tach cac tu bang dau phan cach
str3 = str2.split()
print(str3)

numberList = "một, hai, ba, chín, mười hai"
numberList_tach = numberList.split(",")
print(numberList_tach)

str4 = '  HaPPy birthDAY2024  '
str5 = str4.title()
print(str5)

str4 = str4.strip()
print(str4)

# TOÁN TỬ SỐ HỌC
a  = 8
b = 2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)  # chia lấy phần nguyên
print(a%b)   # chia lấy phần dư
print(a**2)
A = (a+b)* 2 - (a/b)**2
print(A)

# TOÁN TỬ SO SÁNH
c = a/b
if(c == 4):
    print("Chia hết")

print(a>b)
print(b>c)

# TOÁN TỬ LOGIC
d = a > b
e = b > c
B = d and e
print(B)
print( not B)
print( not not B)

print( B or e)

# KIỂU DỮ LIỆU TẬP HỢP
fruitList = ['apple', 'banana', 'kiwi', 9, True]
print(fruitList)
print(fruitList[0])
fruitList[0] = 'Blue'
print(fruitList)

# Kiểu dữ liệu tuple
cars =('Toyota', 'Honda', 'Yamaha', 'Toyota')
print(cars)

#cars[0] = "BMW"
#print(cars)

# Kiểu dữ liệu Set
cats = {'Mèo tam thể', 'Mèo mướp', 'Mèo đen', 'Mèo Hoang','Mèo mướp', 'Mèo Hoang'}
print(cats)

# cats[1] = 'Mèo đi hia'
# print(cats)

# Kiểu dữ liệu dictionary
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 2024,
    "color" : "Black"
}
print(thisdict)
print(thisdict["brand"])
thisdict["brand"] = "Toyota"
print(thisdict)

# CHUYỂN ĐỔI KIỂU
t1 = "3"
t2 = 3.4

# chuyen string --> int
print(int(t1))
print(type(int(t1)))

print(int(t2))

# chuyển string, int ==> float
t3 = "3.5"
t4 = 4
print(float(t3))
print(float(t4))

# chuyển đổi thành string ==>str()
print(type(str(t4)))

# chuyển đổi tuple
t5 ="Hà Nội mùa này vắng những cơn mưa"
print(tuple(t5))

# chuyển đổi thành set
print(set(t5))