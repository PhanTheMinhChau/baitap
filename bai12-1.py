import random
list1 = []
list2 = []
n = random.randint(50, 1000)
#List các số nguyên ngẫu nhiên trong khoảng [-1000, 1000]
for i in range(n):
    m = random.randint(-1000, 1000)
    list1.append(m)
print(list1)
#List các số thực ngẫu nhiên trong khoảng [-1000.0, 1000.0]
for i in range(n):
    h = random.uniform(-1000.0, 1000.0)
    list2.append(h)
print(list2)