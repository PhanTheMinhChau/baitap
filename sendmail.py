import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("phanchau66@gmail.com","minhchau642")
a = int(input("nhập số lần gửi: "))
msg = input("nhập thông điệp: ")
for i in range(a):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("phanchau66@gmail.com","minhchau642")
    server.sendmail("phanchau66@gmail.com", "phanchau357@gmail.com", msg)
    server.quit()
print("gửi thành công")