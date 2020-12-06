import os
import random
a = float(input("nhập dung lượng giới hạn(MB): "))*1024
n = int(a//1000) #số file
c = (a%1000)*1024 #dung lượng file cuối(byte)
kytu = '0123456789abcdefghijklmnopqrstuvwxyz '
for i in range(n):
    d = str(i+1)
    os.chdir(os.getcwd())
    f = open("file"+d, "x")
    def chuoi(dodai):
        return ''.join(random.choice(kytu) for i in range(dodai))
    chuoi = chuoi(random.randint(1024000, 1024000))
    f.write(chuoi)
    f.close()
if c != 0: 
    d = str(i+2)
    os.chdir(os.getcwd())
    f = open("file"+d, "x")
    def chuoi(dodai):
        return ''.join(random.choice(kytu) for i in range(dodai))
    chuoi = chuoi(random.randint(c, c))
    f.write(chuoi)
    f.close()
print("kết thúc")