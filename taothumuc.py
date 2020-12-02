import os 
add = input("nhập địa chỉ cần tạo thư mục: ")
foldername = input("nhập tên thư mục cần tạo: ")
filename = input("nhập tên file cần tạo: ")
file = os.path.join(add,foldername)
os.mkdir(file)
os.chdir(file)
f = open(filename, "x")
print("tạo thành công file",filename,"trong",add,foldername)