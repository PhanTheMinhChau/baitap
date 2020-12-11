import os, random
add = os.getcwd()
a = float(input("nhập dung lượng giới hạn(1-1024MB): "))*1024
while ((a/1024)<1) or ((a/1024)>1024):
    a = float(input("yêu cầu nhập lại (1-1024MB)"))*1024
n = int(a//1000) #số file
c = int((a%1000)*1024) #dung lượng file cuối(byte)
os.mkdir("thư mục chứa file")
for i in range(n):
    os.chdir(add+"\\thư mục chứa file")
    f = open("file"+str(i+1), "x")
    f.write(''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz ') for i in range(1024000)))
if c!=0:
    os.chdir(add+"\\thư mục chứa file")
    f = open("file"+str(i+2), "x")
    f.write(''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz ') for i in range(c)))
print("kết thúc")
