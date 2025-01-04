# # Cau lenh dieu kien If...Else
# a = int(input("Nhập số a:"))
# b = int(input("Nhập số b:"))
# c = int(input("Nhập số c:"))

# if (a>b):
#     print(str(a)+ " là giá trị lớn nhất ")
# else:
#     print(str(b)+ " là giá trị lớn nhất ")

# if(a%2 ==0):
#     print(str(a)+ " là số chẵn")

# #if..elif..else
# if(b > c):
#     print("Giá trị max = ", b)
# elif(b < c):
#     print("Giá trị max = ", c)
# else:
#     print(" a = b")

# #lồng nhau
# if(a>b):
#     if(b>c):
#         print(" Max = ", a)
#     elif(b<c):
#         print(" Max = ", a, "&", c)
# else:
#     print( "a <b ")


# VÒNG LẶP FOR
cars = ["Toyota", "Honda", "Yamaha", "Suzuki", "BMW"]
for value in cars:
    print(value)

numbers = [4, 8, 1, 3, 9, 0, 5]
sum = 0
for n in numbers:
    sum = sum + n

print("Tổng là :", sum)

for i in range(11):
    for j in range(11):
        print(i, "x", j," = ", i*j)
    print("\n")

# vòng lặp while 

#Dân số Việt Nam năm 2017 là 95.5 triệu người. 
#Nếu tốc độ tăng dân số trung bình năm là 1.2% thì 
# đến năm bao nhiêu dân số Việt Nam là 150 triệu
danSo = 95.5
nam = 2017
tocDo_tang = 1.2/100

while (danSo < 150) :
    nam += 1
    danSo *=(1+ tocDo_tang)

print(" Năm dân số đạt 150 triệu là :", nam)

# HÀM
# range(end)
# range(start, end)
for i in range(2,9):
    print(i)

# range(start, end, step)
s = 0
for i in range(0,1001,2):
    s +=i 
print("Tổng các số từ 0 ->1000 :", s)

# hàm zip
x = ("A", "B", "E")
y = ("D", "G", "H")
xy = zip(x, y)
print(xy)

names = ["Duy", "Hoa", "Khang"]
ages = [25, 30, 35]

result = list(zip(names, ages))
print(result)

resultDict = dict(zip(names, ages)) 
print(resultDict)

# giải nén dữ liệu sử dụng hàm zip
zipped = [("Blue", 34), ("Green", 18), ("Yellow", 22)]

colors, rates = zip(*zipped) 
print(colors)
print(ages)

# Hàm enumerate : lặp qua các đối tượng có thể lặp lại ( list, tuple, string,...)

fruits = ['Apple', 'Cherry', "Mango",'Banana',]

for index, value in enumerate(fruits):
    print(f"Index :{index}, Value :{value}")

print(sorted(fruits))

# ví dụ 
# expression for value in collection if conditions ==> được sử dụng để tạo ra danh sách, 
# tập hợp, hoặc từ điển

rst = [x for x in range(1, 11) if x % 2 == 0]
print(rst)

# tương đương
rst2 = []
for x in range(1, 11):
    if(x % 2 == 0):
        rst2.append(x)

print(rst2)

# HÀM TỰ ĐỊNH NGHĨA
# def Ten_ham(argument):
#    câu lệnh

def add(a, b):
    return a + b

rst3 = add(6, 8)
print(f"Tổng là : {rst3}")

def welcome():
    print("Hello, welcome to MCI")

# goi ham
welcome()

# ham voi tham so mac dinh
def rectange_area(length, width = 5):
    return length * width

print(rectange_area(10))
print(rectange_area(10, 10))

# ham tra ve nhieu gia tri
def calculate(a, b):
    return a + b, a - b

# goi ham
sum_result, diff_result = calculate(8, 3)
print(f"Tổng : {sum_result},Hiệu :{diff_result}")

# hàm lambda
square = lambda x: x**2
print(square(4))

# sử dụng hàm như là đối số truyền vào của hàm khác 
def apply_function(func, value):
    return func(value)

# goi ham
rst4 = apply_function(lambda x: x**3, 5)
print(rst4)

# Hàm đệ quy : là hàm gọi lại chính nó
def giaithua(n):
    if n == 0:
        return 1
    return n * giaithua(n -1)

# goi ham
print(giaithua(5))