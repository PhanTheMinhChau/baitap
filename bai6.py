import random
import math
a = []
n = int(input("nhập n "))
for i in range(n): #tạo list n phần tử
    a.append(random.random())
m = - math.inf
for i in range(n): #giá trị lớn nhất
    if a[i] > m:
        m = a[i]
print("giá trị lớn nhất trong ", a, "là:",m)
