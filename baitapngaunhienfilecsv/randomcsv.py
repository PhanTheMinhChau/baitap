import pandas as pd
data = pd.read_csv("danh-sach-sinh-vien - Trang tính1.csv")
sinhvien = data.sample(7)
sinhvien.to_csv('7sinhvien.csv',index=False)