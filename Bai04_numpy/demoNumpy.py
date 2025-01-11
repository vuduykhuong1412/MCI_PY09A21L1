# # tao mang numpy
# import numpy as np

# # Tao mảng 1 chiều
# arr = np.array([2, 4, 6, 8, 10])
# print(arr)

# # Tạo mảng 2 chiều
# arr2 = np.array([[4, 5, 6], [7, 8, 9]], dtype=int)
# print(arr2)

# # tao mang 3 chieu
# arr3 = np.array( [[[2, 4, 6], [8, 10, 12]],
#                  [[1, 3, 5], [7, 9, 11]],
#                  [[0, 10, 100], [200, 300, 400]] ])
# print(arr3)

# brr = np.array([1, 2, 3, 4, 5])
# abrr = arr + brr
# print(abrr)

# # Mot so mang dac thu
# # zeros
# arrZeros = np.zeros((3, 4), dtype=int)
# print(arrZeros)

# # ones
# arrOnes = np.ones((2,3,4), dtype= int)
# print(arrOnes)

# # su dung arange taao mang
# arrArrange = np.arange(1, 9, 2)
# print(arrArrange)

# # ma tran full
# arrFull = np.full((2, 3), 8)
# print(arrFull)

# # ma tran eye
# arrEye = np.eye(4, dtype=int)
# print(arrEye)

# # random
# arrRandom = np.random.random((3,3))
# print(arrRandom)

# # Ham randint tao so ngau nhien
# x = np.random.randint(11, size=(3,4))
# print(x)

# # Check thong tin cua mang
# # Muon biet kieu du lieu cua mang
# print(arr.dtype)

# # shape 
# print(arr2.shape)

# # size
# print(arr3.size)

# # Muon biet so chieu
# print(arr3.ndim)

# # truy cap cac phan tu theo chi so index
# print(arr[2])

# # truy cap theo so hang., cot
# print(arr2[1,1])

# # gan gia tri
# arr2[1,1] = 999
# print(arr2)

# # cat mang theo chi muc
# y = np.array([[1, 2, 3, 4],
#              [5, 6, 7, 8],
#              [9, 10, 11, 12]])
# print(y.ndim)
# print(y)

# print(y[:2, 1:3])
# print(y[0, 1])
# print(y[1, :])
# print(y[1:2, :])

# # tinh toan ma tran
# a = np.array([[1, 2], [3, 4]], dtype=np.float64)
# b = np.array([[5, 6], [7, 8]], dtype=np.float64)
# print(a + b)
# print(np.add(a, b))

# print(a - b)
# print(np.subtract(a, b))

# print(a*b)
# print(np.multiply(a, b))

# print(a/b)
# print(np.divide(a, b))

# Ví dụ reshape
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#arr = np.array([2, 4, 6, 8, 10, 12])
print(arr)
# 1D ==> 2D
newarr2= arr.reshape(4, 3)
#newarr2= arr.reshape(2, 3)

print (newarr2)

# 1D ==> 3D
newarr3 = arr.reshape(2, 3, 2)
print (newarr3)

# ví du khác

print(arr.shape)
arr_expand_dim = np.expand_dims(arr, axis= 0)
print(arr_expand_dim.shape)

# thay doi vi tris cua dim bang ham transponse

arr4 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

#before
print(arr4, end ='\n\n')

#after
print(arr4.transpose())

# noi array
x1 = np.array([[1, 2],[3, 4]])
x2 = np.array([[5, 6],[7, 8]])

x12 = np.concatenate((x1, x2), axis= 0)
print(x12)

# hstack, vstack, dstack

x3 = np.array([1, 2, 3])
x4 = np.array([4, 5, 6])

x34 = np.hstack((x3, x4))
print(x34)

x34v = np.vstack((x3, x4))
print(x34v)

x34d = np.dstack((x3, x4))
print(x34d)

#sum
print(np.sum(x3))

# tinh tich cac phan tu
print(np.prod(x3))

# tinh trung binh cac phan tu
print(np.mean(x3))

# tinh do lech chuan
print(np.std(x3))

# tinh phuong sai
print(np.var(x3))

# tim gia tri nho nhat
print(np.min(x3))
print(np.max(x3))

# tim chi so cua gia tri nho nhat
print(np.argmin(x3))
print(np.argmax(x3))

# Tinh trung vi phan tu
print(np.median(x3))

# tinh phan vi cua cac phan tu
print(np.percentile(x3, 5))