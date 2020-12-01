import os
print("tất cả các tệp và thư mục trong ổ C:")
print(os.listdir('C:\\'))
print("")

print("các thư mục:")
list1 = next(os.walk('C:\\'))[1]
print(list1)
print("")

print("các tệp:")
list2 = next(os.walk('C:\\'))[2]
print(list2)
