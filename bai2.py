# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 20:57:19 2020

@author: Admin
"""

# vòng lặp while
print("giải phương trình ax+b=0")
n = int(input("số lần lặp: "))
i = 1
while i <= n :
    a = float(input("nhập số a "))
    b = float(input("nhập số b "))
    x = -b/a
    print("nghiệp của phương trình",a,"x+",b,"=0 là", x )
    i = i + 1
    
print("kết thúc")
# vòng lặp for
n=int(input("số lần lặp: "))
for i in range(n):
    a = float(input("nhập số a "))
    b = float(input("nhập số b "))
    x = -b/a
    print("nghiệp của phương trình",a,"x+",b,"=0 là", x )
    
print("kết thúc")