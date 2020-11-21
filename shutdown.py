import time
import os
while True:
    a = 0
    print("bạn có muốn tắt máy không?")
    a = input("có(c)/không(k)     ")
    if a == "c":
        break
    elif a == "k":
        print('''không tắt máy
đợi 30 giây''')
        time.sleep(30)
    else:
        print("cú pháp không hợp lệ, mời bạn nhập lại!")
        print(" ")
print("tắt máy")
os.system('shutdown /p /f')