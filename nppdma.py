import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
#ma trận-----------------------------------------------------------------------
a = np.array([[1, 6,7],[87,5,9],[7,9,0]])
b = np.array([[2,6,7],[8,23,6],[-3,7,12]])
print("tổng hai ma trận là: ")
print(a+b) #tổng hai ma trận
print("")
print("tích hai ma trận là: ")
print(a*b) #tích hai ma trận
print("chuyển vị ma trận a là: ")
print(a.transpose())      #chuyển vị ma trận
print("chuyển vị ma trận b là: ")
print(b.transpose())      #chuyển vị ma trận
#đọc file----------------------------------------------------------------------
#đọc file csv từ máy tính
n = pd.read_csv("test.csv")
n = n.head(10)
print('file từ máy')
print(n)
#đọc file csv từ internet
data = pd.read_csv('https://phantheminhchau.github.io/test/test.csv')
data = data.head(10)
print('file từ internet')
print(data)
#đọc file JSON từ internet
js = pd.read_json('https://phantheminhchau.github.io/test/JSON.json', orient='records')
print("file JSON từ internet")
print(js.head(10))
#đồ thị------------------------------------------------------------------------
name = ["A",'B','C','D']
gt = [70,82,50,60]
gt1 = [86,82,50,40]
gt2 = [34,60,50,25]
gt3 = [63,48,55,40]

mp.barh(name, gt, color='blue')
mp.title("đồ thị hình bar")
mp.xlabel("giá trị")
mp.ylabel("name")
mp.show()

mp.bar(name, gt, color='green')
mp.title("đồ thị hình column")
mp.xlabel("name")
mp.ylabel("giá trị")
mp.show()

mp.plot(name, gt, color='red')
mp.title("đồ thị hình line")
mp.xlabel("name")
mp.ylabel("giá trị")
mp.show()

mp.boxplot([gt,gt1,gt2,gt3], labels=name)
mp.title("đồ thị hình boxplot")
mp.xlabel("name")
mp.ylabel("giá trị")
mp.show()
