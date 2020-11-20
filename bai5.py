import math
a = (21,4,-5,73,9,1.68,7,99)
n = len(a)
for i in range(n):
    print(a[i])     #in ra các phần tử trong list a
for i in range(n):
    print("logarit của |",a[i],"| là", math.log(abs(a[i])))