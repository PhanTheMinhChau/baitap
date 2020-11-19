
#vòng lặp while
print("giải phương trình ax+b=0")
n = int(input("số lần lặp: "))
i = 1
while i <= n :
    a = float(input("nhập số a "))
    b = float(input("nhập số b "))
    if a==0 and b==0:
        print("phương trình vô số nghiệm")
    if a==0 and b!=0:
        print("phương trình vô nghiệm")
    if a!=0:
        x = -b/a
        print("nghiệp của phương trình",a,"x+",b,"=0 là", x )
    i = i + 1
    
print("kết thúc")
# vòng lặp for
n=int(input("số lần lặp: "))
for i in range(n):
    a = float(input("nhập số a "))
    b = float(input("nhập số b "))
    if a==0 and b==0:
        print("phương trình vô số nghiệm")
    if a==0 and b!=0:
        print("phương trình vô nghiệm")
    if a!=0:
        x = -b/a
        print("nghiệp của phương trình",a,"x+",b,"=0 là", x )
    
print("kết thúc")
