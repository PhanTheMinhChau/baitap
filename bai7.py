import random
import math
a = []
n = int(input("nhập n "))
for i in range(n): #tạo list n phần tử
    a.append(random.random())
m = math.inf
for i in range(n): #giá trị nhỏ nhất
    if a[i] < m:
        m = a[i]
print("giá trị nhỏ nhất trong ", a, "là:",m)