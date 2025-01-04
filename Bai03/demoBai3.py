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