import os
import random
add = os.getcwd()
a = float(input("nhập dung lượng giới hạn(MB): "))*1024
n = int(a//1000) #số file
c = (a%1000)*1024 #dung lượng file cuối(byte)
file = os.path.join("")
os.mkdir("thư mục chứa file")
def chuoi(n):
        return ''.join(random.choice(kytu) for i in range(n))
kytu = '0123456789abcdefghijklmnopqrstuvwxyz '
for i in range(n):
    d = str(i+1)
    os.chdir(add+"\\thư mục chứa file")
    f = open("file"+d, "x")
    f.write(chuoi(1024000))
    f.close()
if c != 0: 
    d = str(i+2)
    os.chdir(add+"\\thư mục chứa file")
    f = open("file"+d, "x")
    f.write(chuoi(int(c)))
    f.close()
print("kết thúc")